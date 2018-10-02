import queue

# sample_input = {
#     0: [1, 2, 3],
#     1: [4],
#     2: [5],
#     3: [],
#     4: [5],
#     5: []
# }

sample_input = {
    0: [1, 2, 3],
    1: [4],
    2: [5, 6],
    3: [5],
    4: [6],
    5: [4],
    6: [7],
    7: [3, 8],
    8: [6]
}


class DirectedGraph:
    def __init__(self, graph):
        self.directed_graph = graph
        self.start_point = self.get_start_point()
        self.end_point = self.get_end_point()
        self.path = None

    def __init_with_input(self, graph):
        self.directed_graph = graph
        self.start_point = self.get_start_point()
        self.end_point = self.get_end_point()
        self.path = None

    def get_start_point(self):
        keys = list(self.directed_graph.keys())
        return keys[0]

    def get_end_point(self):
        size = len(self.directed_graph)
        keys = list(self.directed_graph.keys())
        return keys[size - 1]

    def find_path(self):
        self.path = DirectedGraph.bfs(self.directed_graph, self.start_point, self.end_point)
        return self.path

    @staticmethod
    def generate_graph():
        return sample_input

    @staticmethod
    def bfs(graph, start, end):
        sq = queue.Queue()
        start_point = Point(start, [start])
        sq.put(start_point)
        visited = [start]
        while not sq.empty():
            size = sq.qsize()
            for n in range(0, size):
                cur = sq.get()
                path = cur.path
                if cur.id == end:
                    return list(path)
                next_neighbors = graph.get(cur.id)
                for n_nb in next_neighbors:
                    if n_nb in visited:
                        continue
                    n_point = Point(n_nb, path + [n_nb])
                    sq.put(n_point)
                    visited.append(n_nb)
        return None


class Point:
    def __init__(self, pid, path):
        self.id = pid
        self.path = path
