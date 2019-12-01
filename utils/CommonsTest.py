import unittest

from utils.common import reverse_complement, reverse_complement_2, int_list, gc_content, float_list


class CommonsTest(unittest.TestCase):

    def test_reverse_complement(self):
        dna = 'ATGAGCTACACG'
        expected_complement = 'CGTGTAGCTCAT'
        self.assertEqual(expected_complement, reverse_complement(dna))
        self.assertEqual(expected_complement, reverse_complement_2(dna))

    def test_gc_content(self):
        self.assertEqual(0.5, gc_content('ACTGTTGGCCAA'))

    def test_int_list(self):
        self.assertListEqual([9, 7, 5, 3, 1], int_list('9 7 5 3 1'))

    def test_float_list(self):
        self.assertListEqual([9.1, 7.3, 5.5, 3.7, 1.9], float_list('9.1 7.3 5.5 3.7 1.9'))
