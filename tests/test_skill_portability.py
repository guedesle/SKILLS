import unittest

from scripts.audit_skill_portability import audit_text


class PortabilityTests(unittest.TestCase):
    def test_windows_backslash_absolute_path_blocks_global_ready(self):
        result = audit_text(r"Use C:\projetos\siedoe\schema.json sempre.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertTrue(result["blockers"])

    def test_windows_slash_absolute_path_blocks_global_ready(self):
        result = audit_text("Use C:/projects/acme/schema.json sempre.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertIn("absolute-windows-path", result["blockers"])

    def test_workspace_posix_absolute_path_blocks_global_ready(self):
        result = audit_text("Load /workspace/acme/schema.json before running.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertIn("absolute-posix-path", result["blockers"])

    def test_root_posix_absolute_path_blocks_global_ready(self):
        result = audit_text("Read /root/acme/schema.json.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertIn("absolute-posix-path", result["blockers"])

    def test_usr_local_posix_absolute_path_blocks_global_ready(self):
        result = audit_text("Execute /usr/local/acme/tool.sh.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertIn("absolute-posix-path", result["blockers"])

    def test_current_directory_relative_path_is_not_absolute(self):
        result = audit_text("Read ./references/schema.json before drafting.")
        self.assertEqual(result["classification"], "GLOBAL_READY")
        self.assertNotIn("absolute-posix-path", result["blockers"])

    def test_parent_directory_relative_path_is_not_absolute(self):
        result = audit_text("Use ../design-paragraphs/references/paragraph-typology.md.")
        self.assertEqual(result["classification"], "GLOBAL_READY")
        self.assertNotIn("absolute-posix-path", result["blockers"])

    def test_url_path_does_not_count_as_local_absolute_path(self):
        result = audit_text("Use https://example.com/mcp for the remote service.")
        self.assertEqual(result["classification"], "GLOBAL_READY")

    def test_generic_contract_is_global_ready(self):
        result = audit_text("Validate a canonical skill directory and its declared metadata.")
        self.assertEqual(result["classification"], "GLOBAL_READY")

    def test_generic_discussion_of_adapter_does_not_require_adapter(self):
        result = audit_text("A promotion workflow may preserve a local adapter when a project needs one.")
        self.assertEqual(result["classification"], "GLOBAL_READY")


if __name__ == "__main__":
    unittest.main()
