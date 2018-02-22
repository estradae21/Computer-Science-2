# Michael Roach 9/12/2016
#  Complete the following singly-linked list program --
#  you need to implement those methods that say "pass".
#  Recieved Help from: Instructor Steve Beaty,

from __future__ import print_function
import unittest


class LinkedList:
    class node:
        def __init__(self, value, next):
            self.value = value
            self.next = next

    # do not put in getters and setters as they are not needed

    def __init__(self, initial=None):

        self.initial = initial  # for extra credit, add in the elements of initial
        self.front = self.back = None

    def empty(self):
        return self.front == None == self.back is None  # if the list is empty we and to return that both s.f and
        # s.b have no values and equal none  not self.empty

    def __iter__(self):
        self.current = self.front
        return self

    def next(self):
        return self.__next__()  # * not getting any errors with or without this block of
        # code * see discussion board

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next
            return tmp
        else:
            raise StopIteration()

    def __str__(self):
        return ",".join(str(node) for node in self)

    def __repr__(self):
        return "<linked list>" % self  # extra credit return self

    def push_front(self, value):
        new = self.node(value, self.front)  # ?? I speculate that this is the case where we have more than 2 nodes and
        if self.empty():  # we want to insert a new node in the front of the list ??
            self.front = self.back = new  #
        else:
            self.front = new  #

    def push_back(self, value):  #
        new = self.node(value, None)  # ** I speculate that we want none so that we create a new empty node with
        # no value attached to it ** not self.node(value, self.back)
        if self.empty():
            self.back = self.front = new  #
        else:
            self.back.next = new  # *** we want to set self.back.next to new first  *** not self.back = new
            self.back = new  # *** then set self.back to new in order to have a new back value  ***
            # not self.back.next = new

    def pop_front(self):

        if self.empty():
            raise RuntimeError  #
        if self.front == self.back:  #
            tmp = self.front.value  #
            self.front = self.back = None  #
            return tmp
        tmp = self.front.value
        self.front = self.front.next
        return tmp

    def pop_back(self):
        if self.empty():  # when the list is empty raise a runtime error as there is nothing to return
            raise RuntimeError
        if self.back == self.front:
            tmp = self.front.value  # error in pycharm
            ''' when there is one value stored self.back and self.front are equal, set
                                            tmp = to self.back and self.front in order
                                            to retrieve the value'''
            self.front = self.back = None  # set the stored value to nothing
            return tmp  # and return the value
        val = self.back.value  # set a the value at the end of the list to val in order to retreive it
        tmp = self.front  # set self.front to temp in order to iterate through the linked list
        while tmp.next != self.back:  # while loop to ensure we are not at the last link list value
            tmp = tmp.next  # set tmp = to tmp.next in order to iterate through the list
        self.back = tmp  # when self.back = tmp = tmp.next
        self.back.next = None  # set self.back.next to None and return the value in self.back
        return val


class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertTrue(LinkedList().empty())


class TestPushFrontPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3)
        self.assertTrue(linked_list.empty())


class TestPushFrontPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertTrue(linked_list.empty())


class TestPushBackPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertTrue(linked_list.empty())


class TestPushBackPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back("foo")
        linked_list.push_back([3, 2, 1])
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), [3, 2, 1])
        self.assertEqual(linked_list.pop_back(), "foo")
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertTrue(linked_list.empty())


class TestStr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__str__(), '1, 2, 3')
''' B-level work '''


class TestInitialization(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("one", 2, 3.141592))
        self.assertEqual(linked_list.pop_back(), "one")
        self.assertEqual(linked_list.pop_back(), "2")
        self.assertEqual(linked_list.pop_back(), "3.141592")


class factorial:
    def fact(self, a):
        if a < 0: raise ValueError("Less than zero")
        if a == 0 or a == 1: return 1

        stack = LinkedList()
        while a > 1:
            stack.push_front(a)
            a -= 1

        result = 1
        while not stack.empty():
            result *= stack.pop_front()

        return result
        # print "factorial"


class test_factorial(unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: factorial().fact(-1))

    def test_zero(self):
        self.assertEquals(factorial().fact(0), 1)

    def test_one(self):
        self.assertEquals(factorial().fact(1), 1)

    def test_two(self):
        self.assertEquals(factorial().fact(2), 2 * 1)

    def test_10(self):
        self.assertEquals(factorial().fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)


if __name__ == "__main__":
    print(factorial().fact(1))
    print(factorial().fact(2))
    print(factorial().fact(100))
