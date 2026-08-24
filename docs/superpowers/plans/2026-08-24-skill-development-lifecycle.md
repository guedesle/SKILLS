# Skill Development Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar uma fábrica governada de skills que constrói, valida, avalia, audita portabilidade, promove e distribui skills gerais com low-HITL.

**Architecture:** A meta-skill `chatgpt-governed-workflow` delega desenvolvimento de skills para `skill-development-lifecycle`, que compõe seis skills especializadas. Validações determinísticas são implementadas em scripts Python compartilhados e executadas localmente/CI antes do gate GitHub.

**Tech Stack:** Markdown Agent Skills, Python 3.12, PyYAML 6.x, `unittest`, GitHub Actions, JSON registry, ZIP bundles.

**Spec:** `docs/superpowers/specs/2026-08-24-skill-development-lifecycle-design.md`

## Global Constraints

- `guedesle/SKILLS` permanece fonte canônica.
- Novas skills usam `skills/<nome>/SKILL.md`, kebab-case e SemVer.
- PyYAML deve ser `>=6,<7`; não adicionar framework de testes adicional.
- Falha determinística é corrigida e revalidada sem novo HITL.
- Não promover literalmente dependências específicas de projeto.
- Não alegar execução de eval LLM ou instalação em host que não foi observada.
- O roteamento Luna/Terra/Sol continua centralizado em `AGENTS.md` + `adaptive-model-routing`.

---

### Task 1: Biblioteca de validação canônica com YAML real

**Files:**
- Create: `requirements-dev.txt`
- Create: `scripts/skill_validation.py`
- Create: `tests/test_skill_validation.py`
- Modify: `scripts/sync_skills.py`
- Modify: `scripts/package_chatgpt_skills.py`

**Interfaces:**
- Produces: `load_frontmatter(path: Path) -> dict`, `validate_skill_record(root: Path, skill: dict) -> list[str]`, `extract_catalog_versions(markdown: str) -> dict[str, str]`.
- Consumes: `registry.json`, `README.md`, `general-skills-status.md`.

- [ ] **Step 1: Write failing tests for malformed YAML and per-skill version drift**

```python
from pathlib import Path
import tempfile
import unittest

from scripts.skill_validation import load_frontmatter, extract_catalog_versions

class SkillValidationTests(unittest.TestCase):
    def test_invalid_yaml_raises_validation_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            path.write_text("---\nname: sample\ndescription: broken: scalar\n---\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_frontmatter(path)

    def test_versions_are_bound_to_skill_rows(self):
        markdown = "| `alpha` | **1.0.0** | X |\n| `beta` | **2.0.0** | X |"
        versions = extract_catalog_versions(markdown)
        self.assertEqual(versions["alpha"], "1.0.0")
        self.assertEqual(versions["beta"], "2.0.0")
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python -m unittest tests.test_skill_validation -v`
Expected: import/module failure because `scripts/skill_validation.py` does not exist.

- [ ] **Step 3: Add PyYAML and minimal validation library**

`requirements-dev.txt`:

```text
PyYAML>=6,<7
```

Implement `load_frontmatter` with `yaml.safe_load`; reject missing closing delimiter, non-mapping frontmatter, syntax errors, duplicate/malformed core values. Implement row-aware README/status version extraction.

- [ ] **Step 4: Replace manual frontmatter parsing in existing scripts**

`sync_skills.py` and `package_chatgpt_skills.py` import the common library. `sync_skills.py` compares the registered version to the same skill's README/status entry rather than searching for the version string globally.

- [ ] **Step 5: Run unit and legacy gates GREEN**

Run:

```bash
python -m unittest tests.test_skill_validation -v
python scripts/sync_skills.py --check
python scripts/package_chatgpt_skills.py --check
python -m py_compile scripts/skill_validation.py scripts/sync_skills.py scripts/package_chatgpt_skills.py
```

Expected: all PASS.

### Task 2: Evals declarativos e validador

**Files:**
- Create: `scripts/validate_skill_evals.py`
- Create: `tests/test_skill_evals.py`

**Interfaces:**
- Produces: `validate_eval_document(path: Path, expected_kind: str) -> list[str]`, CLI `python scripts/validate_skill_evals.py [--skill NAME]`.
- Schema: top-level `schema_version: 1`, `skill`, `kind`, `cases`; each case has non-empty `id`, `input` and kind-specific expectations.

- [ ] **Step 1: Write failing eval schema tests**

```python
import tempfile
import unittest
from pathlib import Path
from scripts.validate_skill_evals import validate_eval_document

class SkillEvalTests(unittest.TestCase):
    def test_duplicate_case_ids_fail(self):
        body = """schema_version: 1
skill: sample
kind: trigger_positive
cases:
  - id: same
    input: first
  - id: same
    input: second
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "trigger-positive.yaml"
            path.write_text(body, encoding="utf-8")
            self.assertTrue(any("duplicado" in e for e in validate_eval_document(path, "trigger_positive")))
```

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_skill_evals -v`
Expected: module missing.

- [ ] **Step 3: Implement schema validation**

Accept kinds `trigger_positive`, `trigger_negative`, `behavior`, `portability`. Reject malformed YAML, wrong skill/kind, duplicate IDs, empty cases, missing input and unsupported keys that alter semantics.

- [ ] **Step 4: Add repository CLI discovery**

Discover `skills/*/evals/*.yaml`; validate naming convention against declared `kind`; `--skill` limits scope; no eval directory is allowed for legacy skills, but malformed present evals fail.

- [ ] **Step 5: Verify GREEN**

Run:

```bash
python -m unittest tests.test_skill_evals -v
python scripts/validate_skill_evals.py
python -m py_compile scripts/validate_skill_evals.py
```

Expected: PASS.

### Task 3: Auditoria determinística de portabilidade

**Files:**
- Create: `scripts/audit_skill_portability.py`
- Create: `tests/test_skill_portability.py`

**Interfaces:**
- Produces: `audit_text(text: str) -> dict` with `classification`, `blockers`, `signals`; CLI `python scripts/audit_skill_portability.py PATH`.
- Classifications: `PROJECT_ONLY`, `GENERALIZABLE`, `GENERAL_WITH_ADAPTER`, `GLOBAL_READY`.

- [ ] **Step 1: Write RED tests for local path/project token and portable skill**

```python
import unittest
from scripts.audit_skill_portability import audit_text

class PortabilityTests(unittest.TestCase):
    def test_windows_absolute_path_blocks_global_ready(self):
        result = audit_text(r"Use C:\\projetos\\siedoe\\schema.json sempre.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertTrue(result["blockers"])

    def test_generic_contract_is_global_ready(self):
        result = audit_text("Validate a canonical skill directory and its declared metadata.")
        self.assertEqual(result["classification"], "GLOBAL_READY")
```

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_skill_portability -v`
Expected: module missing.

- [ ] **Step 3: Implement conservative heuristics**

Detect absolute Windows/POSIX paths, localhost/internal hostnames, repository-specific `.agents/skills` assumptions, likely IDs/tokens, explicit project-only declarations and adapter markers. Never classify based on user identity or secrets.

- [ ] **Step 4: Verify GREEN**

Run:

```bash
python -m unittest tests.test_skill_portability -v
python -m py_compile scripts/audit_skill_portability.py
```

Expected: PASS.

### Task 4: Criar as seis skills especializadas com evals

**Files:**
- Create: `skills/skill-authoring/SKILL.md`
- Create: `skills/skill-validator/SKILL.md`
- Create: `skills/skill-evaluator/SKILL.md`
- Create: `skills/skill-portability-audit/SKILL.md`
- Create: `skills/skill-promotion/SKILL.md`
- Create: `skills/skill-distribution/SKILL.md`
- Create: `skills/<cada-nova-skill>/evals/trigger-positive.yaml`
- Create: `skills/<cada-nova-skill>/evals/trigger-negative.yaml`
- Create: `skills/<cada-nova-skill>/evals/behavior.yaml`

**Interfaces:**
- Each skill owns one lifecycle responsibility and delegates cross-cutting governance to existing low-HITL skills.
- New descriptions must be mutually discriminative enough to avoid trigger overlap.

- [ ] **Step 1: Add trigger-positive and trigger-negative evals first**

Each new skill gets at least 3 positive and 3 negative cases. Negative cases include nearest-neighbor skills to expose trigger collision.

- [ ] **Step 2: Run eval validator RED**

Run: `python scripts/validate_skill_evals.py --skill skill-authoring` before creating its `SKILL.md`/complete eval set.
Expected: fail because eval skill target is absent/incomplete.

- [ ] **Step 3: Implement six SKILL.md contracts**

Each file states responsibility, inputs, workflow, stop/escalation conditions, deterministic checks, composition dependencies and output contract. Do not duplicate Luna/Terra/Sol table.

- [ ] **Step 4: Add behavior evals**

At least 2 behavior cases per skill, including one failure/escalation invariant.

- [ ] **Step 5: Validate files**

Run: `python scripts/validate_skill_evals.py` and unit tests.
Expected: PASS for all new evals.

### Task 5: Criar meta-skills de lifecycle e workflow governado

**Files:**
- Create: `skills/skill-development-lifecycle/SKILL.md`
- Create: `skills/chatgpt-governed-workflow/SKILL.md`
- Create: evals for both meta-skills
- Modify: `skills/skills-central-governance/SKILL.md`
- Modify: `AGENTS.md`

**Interfaces:**
- `chatgpt-governed-workflow` selects repository workflow vs skill lifecycle.
- `skill-development-lifecycle` composes authoring → validation/evals → portability → promotion → distribution → repository gate.
- `skills-central-governance` remains policy/source-of-truth governance, not the implementation engine.

- [ ] **Step 1: Add meta-skill evals with collision cases**

Include positive cases for end-to-end skill creation/promotion and negative cases for simple repository QA or direct paragraph editing.

- [ ] **Step 2: Verify incomplete meta-skill evals fail**

Run validator before completing corresponding `SKILL.md`.
Expected: FAIL for missing target.

- [ ] **Step 3: Implement meta-skill contracts**

Explicitly define low-HITL state machine:
`AUTO_CONTINUE -> deterministic fix/revalidate -> HUMAN_REVIEW_REQUIRED only for material decision -> repository gate -> merge`.

- [ ] **Step 4: Update central governance**

Bump `skills-central-governance` from 1.2.0 to 1.3.0 because delegation to the lifecycle is a backward-compatible capability addition. Remove any duplicated concrete model table if present; reference central routing policy.

- [ ] **Step 5: Validate evals**

Run `python scripts/validate_skill_evals.py`.
Expected: PASS.

### Task 6: Registrar e documentar as oito novas skills

**Files:**
- Modify: `registry.json`
- Modify: `README.md`
- Modify: `general-skills-status.md`
- Modify: `CHATGPT.md`

**Interfaces:**
- Registry is canonical machine-readable inventory.
- README/status rows must bind exact skill → version.

- [ ] **Step 1: Add eight `1.0.0` records and bump central governance to `1.3.0`**

Categories:
- `skill-development-lifecycle`: `skill-management`
- `skill-authoring`: `skill-management`
- `skill-validator`: `skill-management`
- `skill-evaluator`: `skill-management`
- `skill-portability-audit`: `skill-management`
- `skill-promotion`: `skill-management`
- `skill-distribution`: `skill-management`
- `chatgpt-governed-workflow`: `workflow-orchestration`

- [ ] **Step 2: Update README index/details/history and status table**

Every registered version must appear on the row for the same skill.

- [ ] **Step 3: Update ChatGPT/Codex distribution guidance**

Preserve ChatGPT bundle flow; state that availability and installation are host-dependent. Keep Codex USER path `$HOME/.agents/skills` and distinguish reusable plugin distribution from personal directory installation.

- [ ] **Step 4: Run catalog checks**

Run:

```bash
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
```

Expected: PASS.

### Task 7: Integrar testes e gates ao CI

**Files:**
- Modify: `.github/workflows/sync-skills.yml`

**Interfaces:**
- CI installs `requirements-dev.txt`, runs unit tests before catalog/package checks, and preserves existing mirror/package smoke tests.

- [ ] **Step 1: Add dependency install and unit-test stage**

Commands:

```yaml
- name: Install validation dependencies
  run: python -m pip install -r requirements-dev.txt
- name: Run unit tests
  run: python -m unittest discover -s tests -p "test_*.py" -v
- name: Validate skill evals
  run: python scripts/validate_skill_evals.py
```

- [ ] **Step 2: Expand path triggers**

Include `tests/**`, `requirements-dev.txt`, new validation/audit scripts and eval files through existing `skills/**` trigger.

- [ ] **Step 3: Run full local-equivalent batch gate**

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
python -m py_compile scripts/*.py
```

Expected: PASS.

### Task 8: Repository gate, review and merge

**Files:** no new production file required.

**Interfaces:**
- Consumes all prior outputs.
- Produces merged `main` with post-merge verification.

- [ ] **Step 1: Compare branch against main**

Verify changed files are restricted to spec/plan, validation scripts/tests/dependency, eight new skill packages, governance/docs/registry and CI.

- [ ] **Step 2: Open one PR**

Title: `feat(skills): add governed skill development lifecycle`.
Body records architecture, eight new skills, validator hardening, evals, portability, distribution and low-HITL gate results.

- [ ] **Step 3: Require CI/review evidence**

Inspect commit status and workflow runs. Treat deterministic P1/P2 review findings as repairable when they do not alter approved architecture; fix, re-run and re-check automatically.

- [ ] **Step 4: Final merge**

Merge only when branch is current/mergeable, batch gate is green and there is no unresolved material blocker. Use expected head SHA to avoid merging a moved PR.

- [ ] **Step 5: Post-merge verification**

Confirm `main` SHA equals merge result lineage, fetch `registry.json`/new meta-skills from `main`, and verify CI status. Report any host-level installation that cannot be performed automatically as distribution-ready rather than installed.
