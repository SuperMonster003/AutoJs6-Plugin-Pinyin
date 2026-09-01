import gzip
import sys
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIRECTORY))

import manage_dictionaries  # noqa: E402


class DictionaryManagementTest(unittest.TestCase):

    def test_committed_assets_match_lock_and_sqlite_contracts(self):
        lock = manage_dictionaries.load_lock()
        summaries = manage_dictionaries.verify_locked_assets(lock)

        self.assertEqual(["characters", "phrases", "words", "hmm"], [item["asset"] for item in summaries])
        self.assertEqual(41244, summaries[0]["rows"])
        self.assertEqual(127820, summaries[1]["rows"])
        self.assertEqual(349045, summaries[2]["rows"])
        self.assertEqual(35228, summaries[3]["rows"])

    def test_character_parser_preserves_candidate_order(self):
        rows = manage_dictionaries.parse_character_source(
            'dict[0x4e2d] = "zhōng,zhòng"; /* 中 */\n'.encode(),
        )

        self.assertEqual([(0x4E2D, "zhōng,zhòng")], rows)

    def test_phrase_parser_flattens_slots_and_candidates_in_order(self):
        source = b'const phrases_dict = {"A": [["a1", "a2"], ["b"]],};\n'

        self.assertEqual(
            [("A", "a1", 1), ("A", "a2", 1), ("A", "b", 2)],
            manage_dictionaries.parse_phrase_source(source),
        )

    def test_deterministic_gzip_has_stable_bytes_and_timestamp(self):
        first = manage_dictionaries.deterministic_gzip(b"dictionary")
        second = manage_dictionaries.deterministic_gzip(b"dictionary")

        self.assertEqual(first, second)
        self.assertEqual(b"dictionary", gzip.decompress(first))
        self.assertEqual(b"\x00\x00\x00\x00", first[4:8])


if __name__ == "__main__":
    unittest.main()
