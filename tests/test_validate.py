from pathlib import Path
import tempfile
import unittest

from scripts.validate import validate_links, validate_skill


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.skill = self.root / "skills/demo"
        (self.skill / "agents").mkdir(parents=True)
        self.document = self.skill / "SKILL.md"
        self.document.write_text(
            "---\nname: demo\ndescription: A useful demo skill.\n---\n# Demo\n",
            encoding="utf-8",
        )
        (self.skill / "agents/openai.yaml").write_text(
            "interface:\n  display_name: Demo\n"
            "  short_description: A useful isolated demonstration skill\n"
            "  default_prompt: Use $demo for this task.\n",
            encoding="utf-8",
        )

    def test_valid_isolated_skill(self):
        self.assertEqual(validate_skill(self.skill), [])

    def test_invalid_yaml_is_reported(self):
        self.document.write_text("---\nname: [\n---\nBody\n", encoding="utf-8")
        self.assertTrue(validate_skill(self.skill))

    def test_name_must_match_install_folder(self):
        self.document.write_text(
            "---\nname: another\ndescription: Demo\n---\nBody\n", encoding="utf-8"
        )
        self.assertTrue(any("name must match" in e for e in validate_skill(self.skill)))

    def test_missing_interface_is_reported(self):
        (self.skill / "agents/openai.yaml").unlink()
        self.assertTrue(validate_skill(self.skill))

    def test_local_asset_must_exist(self):
        self.document.write_text("[template](assets/intent.md)\n", encoding="utf-8")
        self.assertTrue(validate_links(self.document, self.root))
        (self.skill / "assets").mkdir()
        (self.skill / "assets/intent.md").write_text("# Intent\n", encoding="utf-8")
        self.assertEqual(validate_links(self.document, self.root), [])

    def test_existing_repo_file_is_not_a_portable_skill_dependency(self):
        (self.root / "README.md").write_text("# Readme\n", encoding="utf-8")
        self.document.write_text("[dependency](../../README.md)\n", encoding="utf-8")
        self.assertTrue(any("escapes" in e for e in validate_links(self.document, self.root)))

    def test_symlink_cannot_escape_skill(self):
        (self.root / "outside.md").write_text("# Outside\n", encoding="utf-8")
        (self.skill / "linked.md").symlink_to(self.root / "outside.md")
        self.document.write_text("[dependency](linked.md)\n", encoding="utf-8")
        self.assertTrue(any("escapes" in e for e in validate_links(self.document, self.root)))

    def test_external_links_anchors_and_fenced_examples_are_ignored(self):
        self.document.write_text(
            "[site](https://example.org)\n[heading](#demo)\n"
            "```md\n[example](missing.md)\n```\n", encoding="utf-8"
        )
        self.assertEqual(validate_links(self.document, self.root), [])

    def test_encoded_filename_and_fragment_resolve(self):
        (self.skill / "two words.md").write_text("# Target\n", encoding="utf-8")
        self.document.write_text("[target](two%20words.md#target)\n", encoding="utf-8")
        self.assertEqual(validate_links(self.document, self.root), [])


if __name__ == "__main__":
    unittest.main()
