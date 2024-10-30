from math import expm1
from unittest import expectedFailure
import data
import hw2
import unittest
from hw2 import create_rectangle


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_hw2_create_rectangle_1(self):
        input1 = data.Point(5,5)
        input2 = data.Point(1,1)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(1,5),data.Point(5,1))
        self.assertEqual(expected,result)

    def test_hw2_create_rectangle_2(self):
        input1 = data.Point(3, 18)
        input2 = data.Point(5, 10)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(3, 18), data.Point(5, 10))
        self.assertEqual(expected, result)

    # Part 2
    def test_hw2_short_duration_than_1(self):
        input1 = data.Duration(5,30)
        input2 = data.Duration(2,40)
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(expected,result)

    def test_hw2_short_duration_than_2(self):
        input1 = data.Duration(4, 35)
        input2 = data.Duration(4, 45)
        result = hw2.shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(expected, result)

    # Part 3
    def test_hw2_songs_shorter_than_1(self):
        input1 = [
            data.Song("hello kitty", "bubble gum", data.Duration(3,20)),
            data.Song("naruto", "hello world", data.Duration(6,15)),
            data.Song("superman", "good day", data.Duration(2, 43)),
            data.Song("batman", "nice guy", data.Duration(5, 21))]
        input2 = data.Duration(4,20)
        result = hw2.song_shorter_than(input1, input2)
        expected = [
            data.Song("hello kitty", "bubble gum", data.Duration(3,20)),
            data.Song("superman", "good day", data.Duration(2, 43))]

    def test_hw2_songs_shorter_than_2(self):
        input1 = [
            data.Song("stop sign", "bro stop", data.Duration(5, 43)),
            data.Song("eat world", "starlight", data.Duration(6, 15)),
            data.Song("nark", "moon drops", data.Duration(5, 43)),
            data.Song("train master", "italy", data.Duration(5, 21))]
        input2 = data.Duration(5, 43)
        result = hw2.song_shorter_than(input1, input2)
        expected = [data.Song("train master", "italy", data.Duration(5, 21))]
        self.assertEqual(expected, result)
    # Part 4
    def test_hw2_running_time_1(self):
        input1 = [
            data.Song("stop sign", "bro stop", data.Duration(5, 43)),
            data.Song("eat world", "starlight", data.Duration(6, 15)),
            data.Song("nark", "moon drops", data.Duration(5, 43)),
            data.Song("train master", "italy", data.Duration(5, 21))]
        input2 = [0,1,1,2,3]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(29, 17)
        self.assertEqual(expected,result)

    def test_hw2_running_time_2(self):
        input1 = [
            data.Song("hello kitty", "bubble gum", data.Duration(3, 20)),
            data.Song("naruto", "hello world", data.Duration(6, 15)),
            data.Song("superman", "good day", data.Duration(2, 43)),
            data.Song("batman", "nice guy", data.Duration(5, 21))]
        input2 = [0, 1, 1, 2, 3]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(23, 54)
        self.assertEqual(expected, result)

    # Part 5
    def test_hw2_validate_route_1(self):
        input1 = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
            ]
        input2 = ['san luis obispo','santa margarita', 'atascadero','creston']
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(expected, result)

    def test_hw2_validate_route_2(self):
        input1 = [
            ['home', 'work'],
            ['home', 'school'],
            ['school', 'office'],
            ['work', 'office']
        ]
        input2 = ['home','school','office','work']
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(expected, result)

    def test_hw2_validate_route_3(self):
        input1 = [
            ['home', 'work'],
            ['home', 'school'],
            ['school', 'office'],
            ['work', 'office']
        ]
        input2 = ['office']
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(expected, result)

# Part 6
    def test_longest_repetition_1(self):
        input = [1, 1, 2, 2, 1, 1, 1, 3, 1]
        result = hw2.longest_repetition(input)
        expected = 4
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        input = [1,1,2,2,3,1,5,3,9,9,9,9,1]
        result = hw2.longest_repetition(input)
        expected = 8
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
