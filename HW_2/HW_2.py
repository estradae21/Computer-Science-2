from __future__ import print_function
import unittest

'''
Description:
Author: Ernesto Estrada 
Version:
Help received from: Rodolfo Estrada
'''


class dictionary:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return self.__count

    def __flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return iter(self.__flattened())

    def __str__(self):
        return str(self.__flattened())

    def half_hash(self):
        self.__flattened()
        OldItems = self.__items
        OldLimit = self.__limit
        self.__limit //= 2
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        Hash = 0
        print("New limit " + str(self.__limit))
        while Hash < OldLimit:
            if len(OldItems[Hash]) is 2:
                OldKey = OldItems[Hash][0]
                OldValue = OldItems[Hash][1]
                self.__setitem__(OldKey, OldValue)
            Hash += 1

    def rehash(self):
        self.__flattened()
        OldItems = self.__items
        OldLimit = self.__limit
        self.__limit *= 2
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        Hash = 0
        while Hash < OldLimit:
            if len(OldItems[Hash]) is 2:
                OldKey = OldItems[Hash][0]
                OldValue = OldItems[Hash][1]
                self.__setitem__(OldKey, OldValue)
            Hash += 1
        print("New limit " + str(self.__limit))

    def __myPrivateHash(self, key):
        if isinstance(key, int):
            Hash = key % self.__limit
        else:
            Hash = 0
        return Hash

    def __setitem__(self, key, value):
        if self.__contains__(key):
            return
        Hash = self.__myPrivateHash(key)
        while self.TakenSlot(Hash):
            Hash = Hash + 1
        self.__items[Hash].append(key)
        self.__items[Hash].append(value)
        self.__count += 1
        if self.__count / self.__limit >= .75:
            print("Current count " + str(self.__count))
            print("Current limit " + str(self.__limit))
            print("starting rehash")
            self.rehash()

    def TakenSlot(self, hashed_location):
        if len(self.__items[hashed_location]) == 0:
            return False
        else:
            return True

    def __contains__(self, key):
        for index in range(self.__limit):
            if self.TakenSlot(index):
                StoredKey = self.__items[index][0]
                if StoredKey == key:
                    return True
        return False

    def __getitem__(self, key):
        hash = self.__myPrivateHash(key)
        while self.TakenSlot(hash):
            StoredKey = self.__items[hash][0]
            StoredValue = self.__items[hash][1]
            if StoredKey == key:
                print("getitem() return value = ", StoredValue)
                return StoredValue
            hash += 1
        raise KeyError("No [key, value] pair ", key)

    def __delitem__(self, key):
        if not self.__contains__(key):
            raise KeyError("DELETION OF NON-EXISTENT", key)
        hash = self.__myPrivateHash(key)
        while self.TakenSlot(hash):
            StoredKey = self.__items[hash][0]
            StoredValue = self.__items[hash][1]
            if StoredKey == key:
                del self.__items[hash]
                self.__count -= 1
                if self.__count > 0 and self.__count / self.__limit <= .25:
                    print("Current count " + str(self.__count))
                    print("Current limit " + str(self.__limit))
                    print("starting half hash")
                    self.half_hash()
                return
            #print("New limit " + str(self.__limit))
            hash += 1
        raise KeyError("__contains__ Method reported This key/value pair, but __delitem__ could not find it!", key)


class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")


class test_add_twice(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")


class test_store_false(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertTrue(1 in s)
        self.assertFalse(s[1])


class test_store_none(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)


class test_none_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)


class test_False_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)


class TestCollide(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)


class TestRehash(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        s[6] = "six"
        s[7] = "seven"
        s[8] = "eight"
        s[9] = "nine"
        s[11] = "eleven"
        self.assertEqual(len(s), 12)
        expected = \
            '''[[0, 'zero'], [1, 'one'], [2, 'two'], [3, 'three'], \
            [4, 'four'], [5, 'five'], [6, 'six'], [7, 'seven'], \
            [8, 'eight'], [9, 'nine'], [10, 'ten'], [11, 'eleven']]'''
        self.assertNotEqual(str(s), expected)


class TestDelete(unittest.TestCase):
    def test(self):
        s = dictionary()
        s['a'] = "alpha"
        del s['a']

        self.assertEqual(len(s), 0)


class TestHalving(unittest.TestCase):
    def test(self):
        s = dictionary()
        s['a'] = "alpha"
        s['b'] = "bravo"
        s['c'] = "charlie"
        s['d'] = "delta"
        s['e'] = "echo"
        s['f'] = "foxtrot"
        s['g'] = "golf"
        s['h'] = "hotel"
        s['i'] = "india"
        s['j'] = "echo"
        s['k'] = "kilo"
        s['l'] = "lima"
        s['m'] = "mike"
        s['n'] = "november"
        self.assertEqual(len(s), 14)
        del s['a']
        del s['m']
        del s['l']
        del s['c']
        del s['e']
        del s['h']
        del s['n']
        del s['f']
        del s['b']
        self.assertEqual(len(s), 5)


class TestKeys(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        s[6] = "six"
        s[7] = "seven"
        s[8] = "eight"
        s[9] = "nine"
        s[11] = "eleven"
        self.assertTrue(0 in s)
        self.assertEqual(s[0], "zero")
        self.assertTrue(10 in s)
        self.assertEqual(s[10], "ten")


class TestValue(unittest.TestCase):
    def test(self):
        s = dictionary()
        s['a'] = "alpha"
        s['b'] = "bravo"
        s['c'] = "charlie"
        s['d'] = "delta"
        s['e'] = "echo"
        s['f'] = "foxtrot"
        s['g'] = "golf"
        s['h'] = "hotel"
        s['i'] = "india"
        s['j'] = "echo"
        s['k'] = "kilo"
        s['l'] = "lima"
        s['m'] = "mike"
        s['n'] = "november"
        s['o'] = "oscar"
        s['p'] = "papa"
        s['q'] = "quebec"
        s['r'] = "romeo"
        s['s'] = "sierra"
        s['t'] = "tango"
        s['u'] = "uniform"
        s['v'] = "victor"
        s['w'] = "whiskey"
        s['x'] = "x-ray"
        s['y'] = "yankee"
        s['z'] = "zulu"
        s[1] = 1775
        self.assertEqual(len(s), 27)
        self.assertEqual(s['w'], "whiskey")
        self.assertEqual(s['t'], "tango")
        self.assertEqual(s['f'], "foxtrot")
        self.assertEqual(s[1], 1775)


if __name__ == " __main__":
    unittest.main()
