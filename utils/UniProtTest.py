import unittest

from utils.uni_prot import protein_sequence


class UniProtTest(unittest.TestCase):

    def test_protein_sequence(self):
        expected_sequence = 'MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAPGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYALLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATAMAFISWFALAPSCVLNFWSMASR'
        actual_sequence = protein_sequence('A2Z669')
        self.assertEqual(expected_sequence, actual_sequence)

    def test_unknown_sequence(self):
        self.assertRaises(Exception, protein_sequence, 'UNKNOWN_ID')
