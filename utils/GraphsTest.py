from unittest import TestCase

from utils.graphs import adjacency_list, degree_list, edge_list


class GraphsTest(TestCase):

    def setUp(self):
        self.edge_list = open('test_graph.txt')

    def tearDown(self):
        self.edge_list.close()

    def test_edge_list(self):
        expected_edges = [(1, 2), (2, 3), (4, 3), (2, 4)]
        v_count, e_count, edges = edge_list(self.edge_list)
        self.assertEqual(v_count, 5)
        self.assertEqual(e_count, 4)
        self.assertEqual(edges, expected_edges)

    def test_degree_list(self):
        v_count, _, edges = edge_list(self.edge_list)
        actual_list = degree_list(edges, v_count)
        self.assertListEqual([1, 3, 2, 2, 0], actual_list)

    def test_adjacency_list(self):
        v_count, _, edges = edge_list(self.edge_list)
        expected_list = [[2], [1, 3, 4], [2, 4], [3, 2], []]
        actual_list = adjacency_list(edges, v_count)
        self.assertListEqual(expected_list, actual_list)
