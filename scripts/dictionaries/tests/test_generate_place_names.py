import copy
import sys
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIRECTORY))

import generate_place_names  # noqa: E402


class PlaceNameGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.corpus = generate_place_names.load_corpus()

    def test_repository_corpus_is_valid_and_rendered_deterministically(self):
        kotlin = generate_place_names.render_kotlin(self.corpus)
        markdown = generate_place_names.render_markdown(self.corpus)

        self.assertIn('"六安" to listOf("lù", "ān")', kotlin)
        self.assertIn("| 铅山 | `yán shān` |", markdown)
        self.assertEqual(kotlin, generate_place_names.render_kotlin(self.corpus))

    def test_duplicate_place_name_is_rejected(self):
        corpus = copy.deepcopy(self.corpus)
        corpus["entries"].append(copy.deepcopy(corpus["entries"][0]))

        with self.assertRaisesRegex(generate_place_names.CorpusError, "duplicate place name"):
            generate_place_names.validate_corpus(corpus)

    def test_wrong_syllable_count_is_rejected(self):
        corpus = copy.deepcopy(self.corpus)
        corpus["entries"][0]["pinyin"] = ["lù"]

        with self.assertRaisesRegex(generate_place_names.CorpusError, "one syllable per character"):
            generate_place_names.validate_corpus(corpus)

    def test_unknown_source_is_rejected(self):
        corpus = copy.deepcopy(self.corpus)
        corpus["entries"][0]["sourceIds"] = ["missing-source"]

        with self.assertRaisesRegex(generate_place_names.CorpusError, "unknown sources"):
            generate_place_names.validate_corpus(corpus)


if __name__ == "__main__":
    unittest.main()
