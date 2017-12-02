import unittest
from . import search


class TestDBSearch(unittest.TestCase):
    def test_can_find_room(self):
        res = search('Dr. Mueller', 'test.db')
        self.assertListEqual(res, ['001'])


if __name__ == '__main__':
    unittest.main()
