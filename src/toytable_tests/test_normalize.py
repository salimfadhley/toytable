import unittest
from toytable import TableTestMixin
from toytable import table_literal
from toytable import Table


class TestNormalize(unittest.TestCase, TableTestMixin):

    def setUp(self):
        self.s = [
            ('A', int),
            ('B', float),
            ('C', str),
        ]
        self.t = Table(self.s)

        self.t.extend([
            [1, 0.0, 'x'],
            [2, 5.0, 'y'],
            [2, 10.0, 'z'],
        ])

    def test_basic_normalize(self):
        t = self.t.normalize({"B":1.0})
        self.assertEqual(list(t.B), [0, 0.5, 1])

    def test_repr_of_normalized_table(self):
        t = self.t.normalize({"B":1.0})

        expected = table_literal("""
        | A (int) | B (float) | C (str) |
        | 1       | 0         | x       |
        | 2       | 0.5       | y       |
        | 3       | 1.0       | z       |
        """)

        self.assertTablesEqual(t, expected)

if __name__ == '__main__':
    unittest.main()
