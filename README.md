# myagent

깊이 있는 리서치, 원문 기반 종합, 명료한 한국어 및 다국어 설명을 위한 에이전트 설정 저장소입니다. Antigravity, Claude Code, Codex에서 공통으로 사용할 수 있도록 구성되어 있습니다.

## 구성 파일

| 경로 | 역할 |
| --- | --- |
| `GEMINI.md` | 핵심 추론, 근거 검증, 문체 및 응답 구조 규칙 |
| `CLAUDE.md` | Claude Code에서 `GEMINI.md`를 자동으로 불러오는 참조 파일 |
| `.agents/skills/faithful-synthesis/` | 제공된 자료의 논증 재구성, 조건 보존, 비교 및 검토 워크플로 |
| `.agents/skills/deep-research/` | 새로운 근거 탐색, 대안 가설 비교, 장기 리서치 기록 워크플로 |
| `.agents/skills/deep-research/scripts/check_records.py` | 장기 리서치 산출물의 구조 무결성 검사 스크립트 |
| `.agents/agents/evidence-reviewer.md` | Antigravity용 읽기 전용 원문 대조 하위 에이전트 |
| `.claude/agents/evidence-reviewer.md` | Claude Code용 읽기 전용 원문 대조 하위 에이전트 |

## 설치 및 사용 방법

### 1. 이미 연 현재 폴더에 바로 설치하기

에이전트에서 새 폴더를 연 상태로 설치할 때는 현재 폴더 안에서 아래 명령을 실행합니다. 폴더 안에 숨김 파일이 이미 있어도 충돌 없이 설치됩니다.

```bash
git init -b main
git remote add origin https://github.com/Nuanox/myagent.git
git fetch origin
git checkout -t origin/main -f
```

### 2. 새 폴더로 복제해서 사용하기

터미널에서 새 폴더를 만들며 복제할 때는 아래 명령을 실행한 뒤 해당 폴더를 에이전트에서 엽니다.

```bash
git clone https://github.com/Nuanox/myagent.git
cd myagent
```

- Antigravity: 폴더를 열면 `GEMINI.md`와 `.agents/` 아래의 스킬 및 하위 에이전트가 자동으로 로드됩니다.
- Claude Code: 폴더를 열면 `CLAUDE.md`를 통해 `GEMINI.md`가 로드되고, `.claude/agents/evidence-reviewer.md` 하위 에이전트가 등록됩니다.
- Codex: 폴더 안에서 아래 명령으로 심볼릭 링크를 만들면 Antigravity와 중복 로드 충돌 없이 `AGENTS.md`를 인식합니다.

```bash
# macOS / Linux
ln -s GEMINI.md AGENTS.md
```

### 2. 맥 또는 윈도우에서 변경 사항 동기화하기

설정을 수정한 뒤 올릴 때:

```bash
git add -A
git commit -m "Update agent rules"
git push
```

다른 기기에서 최신 설정을 내려받을 때:

```bash
git pull
```

### 3. 유지보수 시 참고 사항

Antigravity는 단일 규칙 파일을 최대 24,000바이트까지만 읽습니다. `GEMINI.md`를 수정할 때는 파일 크기가 24,000바이트를 넘지 않도록 유지하고, 세부 절차는 `.agents/skills/` 아래의 스킬 문서에 작성하는 것이 안전합니다.
