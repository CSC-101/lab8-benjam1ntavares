import unittest
import group

class TestGroup(unittest.TestCase):

    def test_groups_of_3(self):
        l = [1,2,3,4,5,6,7,8,9]
        expected = [[1,2,3], [4,5,6], [7,8,9]]
        actual = group.groups_of_three(l)
        self.assertEqual(expected, actual)

    def test_groups_of_3_2(self):
        l = [1,2,3,4,5,6,7,8]
        expected = [[1,2,3], [4,5,6], [7,8]]
        actual = group.groups_of_three(l)
        self.assertEqual(expected, actual)


# these tests are for the list comprehension version

    def test_groups_of_three(self):
        l = [1,2,3,4,5,6,7,8,9]
        expected = [[1,2,3], [4,5,6], [7,8,9]]
        actual = group.groups_of_three(l)
        self.assertEqual(expected, actual)

    def test_groups_of_three2(self):
        l = [1,2,3,4,5,6,7,8]
        expected = [[1,2,3], [4,5,6], [7,8]]
        actual = group.groups_of_three(l)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
