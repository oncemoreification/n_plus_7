from substitution import find_subs
from substitution import perf_subs
from unittest import TestCase


class TestSubsitutionFunctions(TestCase):
    @classmethod
    def setUpClass(cls):
        words = open('words')
        cls.word_list = sorted(words.read().splitlines())
        words.close()
        cls.sample_targets = frozenset(["sky", "Zyzzogeton", "skylarker",])

    def test_find_subs(self):
        """It should return a result map with word -> word + 7, wrapping around the dictionary
        if need be.

        """
        res_gen = find_subs(self.sample_targets, self.word_list, 7)
        res_map = {}

        for target, replacement in res_gen:
            res_map[target] = replacement

        self.assertEqual(res_map["Zyzzogeton"], "aardwolf")
        self.assertEqual(res_map["sky"], "skylarker")
        self.assertEqual(res_map["skylarker"], "skyphos")

    def test_perf_subs(self):
        """It should return a text with the appropriate replacements, and one replacement per word.

        """
        res_gen = [("sky", "skylarker"), ("skylarker", "skyphos"),]

        res = perf_subs("The sky is a skylarker.", res_gen)
        self.assertEqual(res, "The skylarker is a skyphos.")


if __name__ == '__main__':
    from unittest import main

    main()
