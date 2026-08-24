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
            errors = validate_eval_document(path, "trigger_positive")
            self.assertTrue(any("duplicado" in error for error in errors))

    def test_wrong_kind_fails(self):
        body = """schema_version: 1
skill: sample
kind: behavior
cases:
  - id: one
    input: do it
    expect: preserve scope
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "trigger-positive.yaml"
            path.write_text(body, encoding="utf-8")
            errors = validate_eval_document(path, "trigger_positive")
            self.assertTrue(any("kind" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
