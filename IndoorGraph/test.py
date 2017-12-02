import unittest
from IndoorGraph import create_graph


class TestGraphCreator(unittest.TestCase):
    def test_can_create_graph(self):
        G = create_graph('IndoorGraph/einhornstall.json')
        self.assertEqual(G.number_of_nodes(), 14)
        # print(sorted(G))
        self.assertEqual(G.number_of_edges(), 13)


if __name__ == '__main__':
    unittest.main()
