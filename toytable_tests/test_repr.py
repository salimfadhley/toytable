import unittest
from toytable import Table


class TestRepr(unittest.TestCase):

    def test_repr_headers(self):
        t = Table([('A', int), 'B', ('C', float)])
        self.assertEquals(
            repr(t),
            "| A (int) | B | C (float) |"
        )

    def test_repr(self):
        t = Table([('A', int), 'B', ('C', float)])
        t.extend([
            [1, "hello", 1.1],
            [2, "goodbye", 2.2],
        ])
        print repr(t)

    def test_column_descriptions_on_join(self):
        p = Table([('Owner Id', int), 'Pokemon', ('Level', int)])
        p.extend([
            [1, 'Pikachu', 18],
        ])
        o = Table([('Owner Id', int), ('Name', str)])
        o.append([1, 'Ash Ketchum'])
        j = p.left_join(
            keys=('Owner Id',),
            other = o
        )

        self.assertEquals(
            ['Owner Id (int)', 'Pokemon', 'Level (int)', 'Name (str)'],
            j._column_descriptions
        )

    def test_get_maximum_column_widths_for_join(self):
        p = Table([('Owner Id', int), 'Pokemon', ('Level', int)])
        p.extend([
            [1, 'Pikachu', 18],
        ])
        o = Table([('Owner Id', int), ('Name', str)])
        o.append([1, 'Ash Ketchum'])
        j = p.left_join(
            keys=('Owner Id',),
            other = o
        )
        expected = [
            len(j._get_column('Owner Id').description),
            len(j._get_column('Pokemon').description),
            len(j._get_column('Level').description),
            len('Ash Ketchum'),
        ]

        widths = j._get_column_widths()
        self.assertEquals(
            expected,
            widths
        )

    def test_repr_joined_table(self):
        p = Table([('Owner Id', int), 'Pokemon', ('Level', int)])
        p.extend([
            [1, 'Pikachu', 18],
        ])
        o = Table([('Owner Id', int), ('Name', str)])
        o.append([1, 'Ash Ketchum'])
        j = p.left_join(
            keys=('Owner Id',),
            other = o
        )

        expected = [
            "| Owner Id (int) | Pokemon | Level (int) | Name (str)  |",
            "| 1              | Pikachu | 18          | Ash Ketchum |"
        ]

        for resultrow, expectedrow in zip(
            repr(j).split('\n'),
                expected):
                self.assertEquals(
                    resultrow,
                    expectedrow
                )


if __name__ == '__main__':
    unittest.main()