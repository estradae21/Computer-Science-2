from __future__ import print_function
from sys import stdin
import unittest

'''
Description: Tree data 
Author: Ernesto Estrada
Version: 1.0
Help received from: Stack overflow 
Help provided to:
'''


class FamilyTree(object):
    def __init__(self, name, parent=None):
        self.Name = name
        self.left = self.right = None
        self.Parent = parent

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self.Name
        if self.right:
            for node in self.right:
                yield node

    def __str__(self):
        return ','.join(str(node) for node in self)

    def add_below(self, parent, child):
        where = self.find(parent)
        if not where:
            raise ValueError('could not find ' + parent)
        if not where.left:
            where.left = FamilyTree(child, where)
        elif not where.right:
            where.right = FamilyTree(child, where)
        else:
            raise ValueError(' already has the allotted two children')

    def find(self, name):
        if self.Name == name:
            return self
        if self.left:
            left = self.left.find(name)
            if left:
                return left
        if self.right:
            right = self.right.find(name)
            if right:
                return right
        return None

    def parent(self, name):
        search = self.find(name)
        if not search:
            return None
        if not search.Parent:
            return None
        else:
            return search.Parent.Name

    def grandparent(self, name):
        parentname = self.parent(name)
        grandpa_name = self.parent(parentname)
        return grandpa_name

    def generations(self):
        this_level = [self]
        next_level, result, names = [], [], []
        while this_level != []:
            tmp = this_level.pop(0)
            names.append(tmp.Name)
            if tmp.left:
                next_level.append(tmp.left)
            if tmp.right:
                next_level.append(tmp.right)
            if this_level == []:
                this_level = next_level
                result.append(names)
                next_level, names = [], []
        return result

    def inorder(self):
        result = []
        if self.left:
            result += (self.left.inorder())
        result += ([self.Name])
        if self.right:
            result += (self.right.inorder()) # can not append to tree
        return result

    def preorder(self):
        result = []
        result += ([self.Name])
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def postorder(self):
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result += ([self.Name])
        return result


class Family_Tree_Test(unittest.TestCase):
    def test_empty(self):
        self.assertEquals(str(FamilyTree(None)), 'None')

    def setUp(self):
        self.tree = FamilyTree("Grandpa")
        self.tree.add_below("Grandpa", "Homer")
        self.tree.add_below("Grandpa", "Herb")
        self.tree.add_below("Homer", "Bart")
        self.tree.add_below("Homer", "Lisa")

    def test_str(self):
        self.assertEquals(str(self.tree), "Bart,Homer,Lisa,Grandpa,Herb")

    def test_parent(self):
        self.assertEquals(self.tree.parent("Lisa"), "Homer")

    def test_grandparent(self):
        self.assertEquals(self.tree.grandparent("Lisa"), "Grandpa")

    def test_no_grandparent(self):
        self.assertEquals(self.tree.grandparent("Homer"), None)

    def test_generations(self):
        self.assertEquals(self.tree.generations(), \
            [["Grandpa"], ["Homer", "Herb"], ["Bart", "Lisa"]])

    ### MY TEST ###

    def test_inorder(self):
        self.assertEquals(self.tree.inorder(), ['Bart', 'Homer', 'Lisa', 'Grandpa', 'Herb'])

    def test_preorder(self):
        self.assertEquals(self.tree.preorder(), ['Grandpa', 'Homer', 'Bart', 'Lisa', 'Herb'])

    def test_postorder(self):
        self.assertEquals(self.tree.postorder(), ['Bart', 'Lisa', 'Homer', 'Herb', 'Grandpa'])

    def test_add_greatgrand_childs(self):
        self.tree.add_below("Lisa", "John")
        self.tree.add_below("Lisa", "Sarah")
        self.tree.add_below("Herb", "Jimmy")
        self.tree.add_below("Herb", "Jenny")
        self.assertEquals(self.tree.inorder(), ['Bart', 'Homer', 'John', 'Lisa', 'Sarah', 'Grandpa', 'Jimmy', 'Herb', 'Jenny'])


if '__main__' == __name__:

    '''
        Read from standard input a list of relatives. The first line must
        be the ultimate ancestor (the root). The following lines are in the
        form: parent child.
    '''

    for line in stdin:
        a = line.strip().split(" ")
        if len(a) == 1:
            ft = FamilyTree(a[0])
        else:
            ft.add_below(a[0], a[1])
    print(ft.generations())