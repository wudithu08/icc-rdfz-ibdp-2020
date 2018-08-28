'''

import unittest

import random

import itertools


# Given a string (e.g. "What the hell?"), returns a list of the following pattern

# ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',

#  'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']

def input_nput_put_ut_t(input_str: str) -> list:

    raise NotImplementedError()


# add two vectors

def vector_addition(v1: list, v2: list) -> list:

    raise NotImplementedError()


# given two lists of integers, find a slice in list 1 and a slice in list 2 whose sums are equal

# using enumeration is fine

def find_equal_sum_slice(list1: list, list2: list) -> [int, int, int, int]:

    raise NotImplementedError()

# use a sorting algorithm (your choice) to sort a list of ten unsorted integers. Do not use the python 
 
# sort function.

def basic_sort(int_list: list): -> list:

	raise NotImplementedError()
	


# A well-known NP-complete problem

# Given a set of integers, find a non-empty subset (if exists) summing to a given number k

# Note: make use of itertools.combinations. See python documentation online

def subset_sum(s: set or list or tuple, k: int) -> set or list or tuple:

    raise NotImplementedError()


class UnitTest(unittest.TestCase):

    def test_input(self):

        self.assertEqual(input_nput_put_ut_t("What the hell?"),

                         ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',

                          'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']

                         )


    def test_eq_sum_slice(self):

        for i in range(10):

            list1 = [random.randint(0, 150) for i in range(150)]

            list2 = [random.randint(0, 60) for i in range(75)]



            a, b, c, d = find_equal_sum_slice(list1, list2)

            s1, s2 = sum(list1[a:b + 1]), sum(list2[c:d + 1])

            self.assertEqual(s1, s2)


    def test_add_vectors(self):

        self.assertEqual(vector_addition([1, 2, 3], [4, 5, 6]), [5, 7, 9])

        self.assertEqual(vector_addition([1], [-1]), [0])

    def test_basic_sort(self):
	
		    self.assertEqual([1,3,5,7,9,11,13,15,17,10000], basic_sort([3,1,5,7,9,11,15,17,10000,13]))
		

    def test_subset_sum(self):

        s = {random.randint(-200, 200) for i in range(random.randint(100))}

        k = random.randint(-50, 50)

        subset = subset_sum(s, k)

        self.assertTrue(set(subset).issubset(s))

        self.assertEqual(sum(subset), k)


if __name__ == "__main__":

    unittest.main()


'''
