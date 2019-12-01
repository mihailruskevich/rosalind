import unittest
from find_protein_motif.motif import matches


class MotifTest(unittest.TestCase):

    def test_protein_sequence(self):
        self.assertTrue(matches('NNTS'))
