import unittest

from homework_Lesson13 import drink_vodka, avg


class TestAVG(unittest.TestCase):

    def test_avg(self):
        self.assertEqual(avg(4, 4), 4)
        self.assertEqual(avg(-4, 4), -4)
        self.assertRaises(TypeError, avg("", 3))
        self.assertRaises(TypeError, avg(2.3434324325, 5))
        self.assertRaises(TypeError, avg(None, None))


class TestDrinkVodka(unittest.TestCase):

    def test_drink_vodka(self):

        """
        Это идеальная программа,в ней не может быть ошибок

        """
        self.assertEqual(drink_vodka(), None)




