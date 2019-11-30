import unittest

from utils.fasta import fasta_sequences


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.fasta_file = open('test.fas')
        self.sequences = [
            ('Seq_1', 'ACTGACCTGCAAAAAAA'),
            ('Seq_2', 'ATGCATG'),
            ('Seq_3', 'ACTGTGTGTG')
        ]

    def tearDown(self):
        self.fasta_file.close()

    def test_fasta_sequences(self):
        actual_sequences = [pair for pair in fasta_sequences(self.fasta_file)]
        self.assertListEqual(self.sequences, actual_sequences)
