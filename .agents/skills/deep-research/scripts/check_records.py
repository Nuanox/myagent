"""Read-only integrity checks. This does not verify research truth or quality."""
import argparse
import json
import sys
from pathlib import Path


def check(run):
    errors, warnings = [], []
    def err(message):
        errors.append(message)
    for name in ('brief.md', 'evidence.json', 'report.md', 'audit.md'):
        path = run / name
        if not path.is_file() or not path.read_text(encoding='utf-8-sig').strip():
            err(f'Missing or empty {name}')
    if errors:
        return errors, warnings
    try:
        data = json.loads((run / 'evidence.json').read_text(encoding='utf-8-sig'))
    except (ValueError, OSError) as exc:
        return [f'Cannot read evidence.json: {exc}'], warnings
    if not isinstance(data, dict):
        return ['evidence.json must be an object'], warnings
    if data.get('version') != 1:
        err('Unsupported or missing version; expected 1')
    def records(key):
        items = data.get(key)
        if not isinstance(items, list):
            err(f'{key} must be an array')
            return {}
        mapped = {}
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                err(f'{key}[{index}] must be an object')
                continue
            ident = item.get('id')
            if not isinstance(ident, str) or not ident.strip():
                err(f'{key}[{index}] requires an id')
            elif ident in mapped:
                err(f'Duplicate {key} id {ident}')
            else:
                mapped[ident] = item
        return mapped
    questions, sources, claims = (records(k) for k in ('questions', 'sources', 'claims'))
    def text(item, fields, label):
        for field in fields:
            if not isinstance(item.get(field), str) or not item[field].strip():
                err(f'{label}: missing text field {field}')
    def refs(item, key, targets, label):
        ids = item.get(key)
        if not isinstance(ids, list) or any(not isinstance(x, str) for x in ids):
            err(f'{label}: {key} must be an array of ids')
            return []
        for ident in ids:
            if ident not in targets:
                err(f'{label}: unknown {key} reference {ident}')
        return ids
    report = (run / 'report.md').read_text(encoding='utf-8-sig')
    def linked(item, key, ident):
        value = item.get(key)
        return isinstance(value, list) and ident in value
    for ident, source in sources.items():
        text(source, ('title', 'locator', 'source_family', 'note'), ident)
        if source.get('access') not in ('full', 'excerpt', 'snippet', 'unavailable'):
            err(f'{ident}: invalid access')
    for ident, question in questions.items():
        text(question, ('question',), ident)
        ids = refs(question, 'claim_ids', claims, ident)
        if question.get('status') not in ('answered', 'partial', 'unresolved', 'out_of_scope'):
            err(f'{ident}: invalid question status')
        if question.get('status') == 'answered' and not ids:
            err(f'{ident}: answered question has no claims')
        if question.get('status') != 'answered':
            text(question, ('gap',), ident)
        for cid in ids:
            if cid in claims and not linked(claims[cid], 'question_ids', ident):
                err(f'{ident}/{cid}: question link is not reciprocal')
    for ident, claim in claims.items():
        text(claim, ('text', 'report_anchor', 'verification'), ident)
        if claim.get('kind') not in ('source_claim', 'verified', 'inference', 'hypothesis', 'unknown'):
            err(f'{ident}: invalid claim kind')
        qids = refs(claim, 'question_ids', questions, ident)
        if not qids:
            err(f'{ident}: no question links')
        for qid in qids:
            if qid in questions and not linked(questions[qid], 'claim_ids', ident):
                err(f'{ident}/{qid}: claim link is not reciprocal')
        anchor = claim.get('report_anchor')
        if isinstance(anchor, str) and anchor.strip() and anchor not in report:
            err(f'{ident}: report_anchor not found verbatim in report.md')
        evidence = claim.get('evidence')
        if not isinstance(evidence, list):
            err(f'{ident}: evidence must be an array')
            continue
        has_support = False
        for index, link in enumerate(evidence):
            label = f'{ident}/evidence[{index}]'
            if not isinstance(link, dict):
                err(f'{label}: must be an object')
                continue
            sid = link.get('source_id')
            if not isinstance(sid, str) or sid not in sources:
                err(f'{label}: unknown source_id')
            text(link, ('passage', 'locator'), label)
            relation = link.get('relation')
            if relation not in ('supports', 'challenges', 'context'):
                err(f'{label}: invalid relation')
            if relation == 'supports':
                has_support = True
                if isinstance(sid, str) and sid in sources and sources[sid].get('access') in ('snippet', 'unavailable'):
                    warnings.append(f'{ident}: support relies on {sources[sid]["access"]} source {sid}; review scope')
        if claim.get('kind') in ('source_claim', 'verified', 'inference') and not has_support:
            err(f'{ident}: evidence-backed claim has no supporting record')
        if claim.get('kind') in ('hypothesis', 'unknown'):
            text(claim, ('limits',), ident)
    if not questions:
        err('No research questions recorded')
    if not claims:
        warnings.append('No claims recorded; report may only describe unresolved questions')
    warnings.append('Integrity checks do not verify truth, citation entailment, coverage, independence, or logical relations.')
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path, help='Directory containing the four research records')
    args = parser.parse_args()
    try:
        errors, warnings = check(args.run)
    except (OSError, UnicodeError) as exc:
        errors, warnings = [f'Cannot read records: {exc}'], []
    print(json.dumps({'integrity': 'fail' if errors else 'pass', 'errors': errors,
                      'warnings': warnings, 'semantic_verification': 'not_performed'}, ensure_ascii=True, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
