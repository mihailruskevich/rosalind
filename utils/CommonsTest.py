import unittest

from utils.common import reverse_complement, reverse_complement_2


class CommonsTest(unittest.TestCase):

    def test_reverse_complement(self):
        dna = 'ATGAGCTACACG'
        expected_complement = 'CGTGTAGCTCAT'
        self.assertEqual(expected_complement, reverse_complement(dna))
        self.assertEqual(expected_complement, reverse_complement_2(dna))
