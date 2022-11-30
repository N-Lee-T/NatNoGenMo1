import unittest
from novel import find_sentences

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(True)

    def test2(self):
        text2 = 'Hippocampus, '
        self.assertIsNotNone(find_sentences(text2))

    def test3(self):
        text3 = 1890.4
        self.assertIsNone(text3)

    def test4(self):
        example1 = "New test. Let's try? \
                   Maybe so!! It's good. \
                   Really. \"Now we're good.\""
        expected = {"New test": ["New", "test"],
                    "Maybe so!!": ["It's", "good"],
                    "Really.": ["Really"],
                    "Now we're good": ["Now", "we're", "good.\""]}
        self.assertEqual(find_sentences(example1), expected)
