
class Node:

    def __init__(self, id: int):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return str(self.__id) + ""


class Edge:

    def __init__(self, from_node: Node, to_node: Node, weight: int):

        self.__from_node = from_node
        self.__to_node = to_node
        self.__weight = weight

    @property
    def from_node(self):
        return self.__from_node

    @property
    def to_node(self):
        return self.__to_node

    def __str__(self):
        return f"{self.__from_node}->{self.__to_node} weight:{self.__weight}"


class Graph:

    def __init__(self):
        self.__nodes = {}  # dictionary of nodes -> (key: id) (value: node)
        self.__adjacencyList = {}  # dictionary of adjacent -> (key: node) (value: edge)

    @property
    def nodes(self):
        return self.__nodes

    @property
    def adjacency_list(self):
        return self.__adjacencyList

    def add_node(self, id: int):

        temp = self.nodes.get(id)
        if temp is not None:
            return

        new_node = Node(id)
        self.nodes[id] = new_node
        self.adjacency_list[new_node] = []

    def add_edge(self, from_id, to_id, weight: int):
        from_node: Node = self.nodes.get(from_id)
        to_node: Node = self.nodes.get(to_id)

        if from_node is Node or to_node is None:
            raise Exception("there is no Node with this id")

        for edge in self.adjacency_list.get(from_node):
            if edge.to_node == to_node:
                return

        from_list: list = self.adjacency_list.get(from_node)
        to_list: list = self.adjacency_list.get(to_node)

        from_list.append(Edge(from_node, to_node, weight))
        to_list.append(Edge(to_node, from_node, weight))

    def remove_node(self, node_id):
        target = self.nodes.get(node_id)

        if node_id not in self.nodes.keys():
            return

        for node in self.adjacency_list.keys():
            if node != target:
                edges = self.adjacency_list.get(node)
                for edge in edges:
                    if edge.to_node == target:
                        edges.remove(edge)

        self.adjacency_list.pop(target)
        self.nodes.pop(node_id)


    def remove_edge(self, from_id, to_id):

        if from_id not in self.nodes.keys() or to_id not in self.nodes.keys():
            return

        from_node = self.nodes.get(from_id)
        to_node = self.nodes.get(to_id)

        for edge in self.adjacency_list.get(from_node):
            if edge.to_node == to_node:
                self.adjacency_list.get(from_node).remove(edge)

        for edge in self.adjacency_list.get(to_node):
            if edge.to_node == from_node:
                self.adjacency_list.get(to_node).remove(edge)


    def depth_first_traverse(self, node_id):

        root = self.nodes.get(node_id)
        if root is None:
            raise Exception("There is No Node with this id")
        offer = []
        self.__depth_first_traversal(0, root, offer, "")
        return [list(map(int, item.split("-")[1:])) for item in offer]


    def __depth_first_traversal(self, counter: int, root: Node, offer: list, temp: str):

        if counter > 5:
            return

        temp += "-" + str(root)
        offer.append(temp)

        for edge in self.adjacency_list.get(root):
            edge: Edge
            node = edge.to_node
            counter += 1
            self.__depth_first_traversal(counter, node, offer, temp)

    def get_graph(self):

        for node in self.adjacency_list.keys():
            edges = self.adjacency_list.get(node)
            for e in edges:
                print(e, end="\t")
            print()
