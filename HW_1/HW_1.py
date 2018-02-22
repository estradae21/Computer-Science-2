from __future__ import print_function
import unittest

'''Ernesto Estrada
received help from father and Mike Roach'''


class LinkedList(object):
    class Node(object):
        # pylint: disable=too-few-public-methods
        """ no need for get or set, we only access the values inside the
            LinkedList class. and really, never have setters. """

        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial=None):
        #if initial == tuple:
        #    self.initial = self.__str__(initial)
        #else:
        self.initial.__str__ = initial
        self.front = self.back = self.current = None

    def empty(self):
        return self.front == self.back is None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()

    def push_front(self, value):
        new = self.Node(value, self.front)
        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

    def __str__(self):
        return str(self.initial)

    def __repr__(self):
        string = "LinkedList("
        if self.initial is not None:
            string += repr(self.initial)
            while self.current:
                string += "," + repr(self.initial.next_node)
        string += ")"
        return string

    def push_back(self, value):
        new = self.Node(value, self.back)
        if self.empty():
            self.back = self.front = new
        else:
            self.back.next_node = new
            self.back = new

    def pop_front(self):
        if self.empty():
            raise RuntimeError
        if self.front == self.back:
            tmp = self.front.value
            self.front = self.back = None
            return tmp
        tmp = self.front.value
        self.front = self.front.next_node
        return tmp

    def pop_back(self):
        if self.empty():
            raise RuntimeError
        if self.back == self.front:
            tmp = self.front.value
            self.front = self.back = None
            return tmp
        val = self.back.value
        tmp = self.front
        while tmp.next_node != self.back:
            tmp = tmp.next_node
        self.back = tmp
        self.back.next_node = None
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


''' B-level work '''


class TestInitialization(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("one", 2, 3.141592))
        #linked_list = LinkedList()
        #linked_list.push_front("one")
        #linked_list.push_front(2)
        #linked_list.push_front(3.141592)
        self.assertEqual(linked_list.pop_back(), "one")
        self.assertEqual(linked_list.pop_back(), "2")
        self.assertEqual(linked_list.pop_back(), "3.141592")


class TestStr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1,2,3))
        self.assertEqual(linked_list.__str__(), "(1, 2, 3)")


''' A-level work '''


class TestRepr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')


class TestErrors(unittest.TestCase):
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())

    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())

