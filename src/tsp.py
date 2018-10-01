from heapq import *
from operator import attrgetter

# DEFAULT_CITY_NUM = 10
# DEFAULT_MAX_WEIGHT = 15
# DEFAULT_MAX_CONNECTION = 3


class RSP:
    rsp_map = {}
    memory = {}
    space_size = 0

    def __init__(self):
        example = RSP.example_input()
        self.rsp_map = RSP.generate_map(example)
        self.memory = RSP.initialize_memory(self.rsp_map)
        self.space_size = RSP.get_space_size(self.rsp_map)

    def __init__with_input(self, input_data):
        self.rsp_map = RSP.generate_map(input_data)
        self.start_state = RSP.get_start_state()
        self.memory = RSP.initialize_memory(self.rsp_map)
        self.space_size = RSP.get_space_size(self.rsp_map)

    def get_state_neighbors(self, state):
        return self.rsp_map[state.id]

    def get_next_key(self):
        limits = []
        keys = []
        for key in self.memory.keys():
            limits.append(self.get_state_limit(key))
            keys.append(key)
        index = limits.index(min(limits, key=attrgetter('cost')))
        return keys[index]

    def get_state_limit(self, key):
        return self.memory[key][0]

    def get_state_pool(self, key):
        return self.memory[key][1]

    def is_success(self, key):
        pool = self.get_state_pool(key)
        for state in pool:
            path = state.path
            if len(path) == self.space_size:
                return state
        return None

    def update_memory(self, key):
        limit = self.get_state_limit(key)
        next_state = limit.state
        pool = self.get_state_pool(key)
        self.__update_pool(pool, next_state)
        limit = Limit(pool[0], pool[0].cost)
        entry = [limit, pool]
        self.memory[key] = entry

    def __update_pool(self, pool, state):
        neighbors = self.get_state_neighbors(state)
        path = state.path
        pool.remove(state)
        heapify(pool)
        for n in neighbors:
            n_id = n[0]
            n_weight = n[1]
            if n_id in path:
                continue
            n_path = state.path + [n_id]
            n_cost = state.cost + n_weight
            new_state = State(n_id, n_weight, n_path, n_cost)
            heappush(pool, new_state)


    @staticmethod
    def is_same_state(state1, state2):
        return state1 == state2

    @staticmethod
    def example_input():
        # example_map = {
        #     0: [(1, 2), (2, 5), (3, 4)],
        #     1: [(0, 2), (3, 3)],
        #     2: [(0, 5)],
        #     3: [(0, 4), (1, 3)]
        # }
        example_map = {
            0: [(1, 2), (2, 5), (3, 4)],
            1: [(0, 2), (4, 3)],
            2: [(0, 5), (3, 2), (4, 1), (5, 3)],
            3: [(0, 4), (2, 2)],
            4: [(1, 3), (2, 1), (5, 2)],
            5: [(2, 3), (4, 2)]
        }
        return example_map

    @staticmethod
    def initialize_memory(rsp_map):
        memory = {}
        for key in rsp_map.keys():
            neighbors = rsp_map[key]
            pool = []
            for nb in neighbors:
                nb_id = nb[0]
                nb_weight = nb[1]
                nb_path = [key, nb_id]
                nb_cost = nb_weight
                state = State(nb_id, nb_weight, nb_path, nb_cost)
                heappush(pool, state)
            min_state = pool[0]
            limit = Limit(min_state, min_state.cost)
            memory_entry = [limit, pool]
            memory[key] = memory_entry
        return memory

    @staticmethod
    def generate_map(example_map):
        rsp_map = example_map
        return rsp_map

    @staticmethod
    def get_space_size(rsp_map):
        return len(rsp_map)


class State:
    def __init__(self, sid, weight, path, cost):
        self.id = sid
        self.weight = weight
        self.path = path
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class Limit:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
