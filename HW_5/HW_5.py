from __future__ import print_function
from sys import stdin
import unittest

'''
Description: Dijkstras Implementation to find min distance from start to finish
Author: Michael Roach
Version:
Help received from: John Roach
Help provided to:
'''

# set to True if your result includes the track
track_prev = True


class weighted_digraph:
    class __edge(object):
        def __init__(self, to_node, weight):
            self.to_node = to_node
            self.weight = weight

    class __node(object):
        def __init__(self, value):
            self.value = value  # value is the name or id of a node it is NOT the node it is just a string!
            self.edges = []
            self.distance = float('inf')
            self.previous = None
            # previous is the adjacent vertex with the currently known least
            # cost path to this node. If we follow previous back from current
            # node to next node, to next node etc back to source it will provide
            # us with the least cost path to this node.

        def __str__(self):
            result = str(self.value)
            for edge in self.edges:
                result += "->" + str(edge.to_node.value) + \
                          "(" + str(edge.weight) + ")"
            return (result)

        def add_edge(self, new_edge):
            if not self.is_adjacent(new_edge.to_node):
                self.edges.append(new_edge)

        def remove_edge(self, to_node):
            for edge in self.edges:
                if edge.to_node == to_node:
                    self.edges.remove(edge)

        def is_adjacent(self, node):
            for edge in self.edges:
                if edge.to_node == node:
                    return (True)
            return (False)

    def __init__(self, directed=True):
        self.__nodes = []
        self.__directed = directed

    def __len__(self):
        return (len(self.__nodes))

    def __str__(self):
        result = ""
        for node in self.__nodes:
            result += str(node) + '\n'
        return (result)

    def get_edges(self, node):
        return self.__node.edges[:]

    def get_nodes(self):  # return ALL of the nodes in the graph
        return self.__nodes[:]

    def find(self, value):
        for node in self.__nodes:
            if node.value == value:
                return (node)

        return (None)

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_node(self, value):
        if not self.find(value):
            self.__nodes.append(self.__node(value))

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])

    """ Add an edge between two values. If the nodes
            for those values aren't already in the graph,
            add those. """

    def add_edge(self, from_value, to_value, weight):
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        if not from_node:
            self.add_node(from_value)
            from_node = self.find(from_value)
        if not to_node:
            self.add_node(to_value)
            to_node = self.find(to_value)

        from_node.add_edge(self.__edge(to_node, weight))
        if not self.__directed:
            to_node.add_edge(self.__edge(from_node, weight))

    def remove_edge(self, from_value, to_value, weight):
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        from_node.remove_edge(to_node)
        if not self.directed:
            to_node.remove_edge(from_node)

    def are_adjacent(self, value1, value2):
        return (self.find(value1).is_adjacent(self.find(value2)))

    def debugDumpNodeInfo(self, node):
        ''' print out a formatted listing of node attributes '''
        print("debug node = ", self.__node.value,
              " debug distance = ", self.__node.distance)
        self.debugDumpEdgeInfo(self.__node.edges)

    def debugDumpEdgeInfo(self, node):
        print("Debug data: Edge data:")
        edgeList = self.get_edges(self.__node)
        for edge in edgeList:
            print(".....EdgeDebug: to_node=", edge.to_node)
            print(".....EdgeDebug: weight=", edge.weight)

    def min_node_dist(self, nodelist):
        # return  the node with the lowest cost distance or
        # return None if no nodes are in the list
        small_node_dist = None
        set_min_dist = float('inf')
        for nodetmp in nodelist:
            if (nodetmp.distance < set_min_dist):
                print("debug min_node_dist() found new lower cost_valueid=", nodetmp.value)
                small_node_dist = nodetmp
                set_min_dist = small_node_dist.distance
                print("!!!debug min_node_dist()finished using valueid =", small_node_dist.value)
                # print ("-----------", small_node_dist.value, small_node_dist.distance)
        return small_node_dist

    def dijkstra(self, start):
        ''' For all the nodes in the graph, set distance
            equal to infinity and previous equal to none '''

        ''' Set the source to the start, and start's distance to zero '''
        sourceNode = self.find(start)
        sourceNode.distance = 0
        ''' Create a todo set and add source to it '''

        visited = []  # will hold nodes who's minimum distance has been determined
        unvisited = []  # will hold adjacent nodes that need to be processed
        unvisited.append(sourceNode)  # directly from algorithm on pg 198 in book

        something_to_do = True

        while something_to_do:
            small_node_dist = self.min_node_dist(unvisited)
            # print("Debug source node valueid=", sourceNode.value)

            if small_node_dist is None:
                print("debug get_small_node_dist(unvisited) RETURNED NONE!")

            '''else:
                print ("small_node_dist returned node with id=", small_node_dist.value)
                print ("small_node_dist returned node with distance=", small_node_dist.distance)
                print ("Debug source node value_id=", sourceNode.value)'''
            something_to_do = False
            break
            visited.append(small_node_dist)
            unvisited.remove(small_node_dist)

            adj_node_edge = small_node_dist.edges

            for edge in adj_node_edge:
                adj_node_value = edge.to_node.value
                adj_node = self.find(adj_node_value)
                adj_node_dist = edge.weight
                print("Debug: edge adjacent to small_dist Node", small_node_dist.value)
                print("Debug: ", str(edge.to_node.value), str(edge.weight))
                print("this is what is in unvis", unvisited, "this is what is in visited", visited)

                adj_node = small_node_dist.distance + edge.weight

                if adj_node < small_node_dist.distance:
                    # set the current distance to the adj_node_dist.distance
                    small_node_dist.distance = adj_node_dist
                    self.__node.previous = adj_node.value
                    visited.append(adj_node)

        result = []

        for node in self.get_nodes():

            if not track_prev:
                result.append([node.distance, node.value])
                ''' For each node, create a list where the first element
                is the total distance and the second is the value '''
                print(result)

            else:
                ''' For each node, create a list where the first element
                is the total distance and the following values are the
                nodes traversed from end to start '''
                pass
        return result

        '''
            to_node and weight



            While there is something to do
            Find the node with the minimum distance
            Remove it from the todo (visited) set

            For each of the edges in the minimum distance node
            Calculate a possible new distance to the adjacent
            node

            If the new distance is less than the previous
            distance
            Set the distance to the newly calculated
            distance and set the previous reference to the
            node we just choose
            Add the node to the todo set'''

        '''
            1 remove the current node with smallest distance from unvisited
            and add it to the visited list

            2 for all nodes that are adjacent check to see if they are in the visited list or not

            3 if a node is in the visited list do nothing it already has its shortest distance
             to the adjacent node

            4 if the node is not in the visited list compute the distance to this node by traversing
             its edge and edge weight '''


        # if not track_prev:
        # ''' For each node, create a list where the first element
        # is the total distance and the second is the value '''
        # pass
        # else:
        # ''' For each node, create a list where the first element
        # is the total distance and the following values are the
        # nodes traversed from end to start '''
        # pass
        # return (result)


class test_weighted_digraph(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(weighted_digraph()), 0)

    def test_one(self):
        g = weighted_digraph()
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_duplicate(self):
        g = weighted_digraph()
        g.add_node(1)
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_two(self):
        g = weighted_digraph()
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(len(g), 2)

    def test_edge(self):
        g = weighted_digraph()
        g.add_node(1)
        g.add_node(2)
        g.add_edge(1, 2, 3)
        self.assertEqual(str(g), '1->2(3)\n2\n')

    def test_adding_ints(self):
        g = weighted_digraph()
        g.add_nodes([1, 2])
        g.add_edges([(1, 2, 3), (2, 1, 3)])
        self.assertEqual(str(g), '1->2(3)\n2->1(3)\n')

    def test_adding_strings(self):
        g = weighted_digraph()
        g.add_nodes(['Denver', 'Boston'])
        g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(g), 'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

    def test_are_adjacent(self):
        g = weighted_digraph()
        g.add_nodes(['Denver', 'Boston'])
        g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertTrue(g.are_adjacent('Denver', 'Boston'))

    def test_arent_adjacent(self):
        g = weighted_digraph()
        g.add_nodes(['Denver', 'Boston', 'Milano'])
        g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertFalse(g.are_adjacent('Denver', 'Milano'))

    def test_arent_adjacent_directed(self):
        g = weighted_digraph()
        g.add_edges([('Denver', 'Boston', 1971.8)])
        self.assertFalse(g.are_adjacent('Denver', 'Milano'))
        self.assertFalse(g.are_adjacent('Boston', 'Denver'))
        self.assertTrue(g.are_adjacent('Denver', 'Boston'))

    def test_arent_adjacent_undirected(self):
        g = weighted_digraph(False)
        g.add_edges([('Denver', 'Boston', 1971.8)])
        self.assertTrue(g.are_adjacent('Boston', 'Denver'))
        self.assertTrue(g.are_adjacent('Denver', 'Boston'))

    def test_add_edges_without_nodes(self):
        g = weighted_digraph()
        g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(g), \
                         'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

    def test_dijkstra(self):
        g = weighted_digraph()
        g.add_edges([(1, 2, 2), (1, 3, 1), (2, 3, 1), (2, 4, 1), \
                     (2, 5, 2), (3, 5, 5), (4, 5, 3), (4, 6, 6), (5, 6, 1)])
        if track_prev:
            self.assertEquals(g.dijkstra(1), [[0, 1], [2, 2], [1, 3], \
                                              [3, 4], [4, 5], [5, 6]])
        else:
            self.assertEquals(g.dijkstra(1), [[0, 1], [2, 2, 1], [1, 3, 1], \
                                              [3, 4, 2, 1], [4, 5, 2, 1], [5, 6, 5, 2, 1]])

    def test_dijkstra_with_cities(self):  # an additional dijkstra test extra credit?
        print("running dijkstra with cities Denver, Boston, etc")
        g = weighted_digraph()
        g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        g.add_edges([('Denver', 'Boston', 1971.8), ('Denver', 'Chicago', 975), ('Chicago', 'Boston', 800),
                     ('Denver', 'St Louis', 850), ('St Louis', 'Boston', 800), ])
        self.assertEquals(g.dijkstra('Denver'), [[0, 1], [2, 2, 1], [1, 3, 1], \
                                                 [3, 4, 2, 1], [4, 5, 2, 1], [5, 6, 5, 2, 1]])


#################### run unit tests  ################
print(" ---- starting unit tests ")
unittest.main()

if '__main__' == __name__:
    g = weighted_digraph(False)
    stdin = open("Highways.txt")
    for line in stdin:
        a = line.strip().split(" ")
        g.add_edge(a[0], a[1], int(a[2]))
    result = g.dijkstra("Denver")
    for city in result:
        print(city[1], "is", city[0], 'miles from Denver')
        if track_prev:
            for path in city[2:]:
                print("     ", path)
