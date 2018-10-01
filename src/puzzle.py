import random

DIRECTION_UP = 1
DIRECTION_RIGHT = 2
DIRECTION_DOWN = 3
DIRECTION_LEFT = 4


class Puzzle:
    size = 0
    cur_state = None
    state_history = []
    target_pos = None
    path = [DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT]

    def __init__(self):
        self.size = 3
        self.cur_state = Puzzle.random_sate(self.size)
        self.target_pos = self.__get_target_pos()
        self.state_history.append(self.cur_state)
        return

    def __init__with_state(self, init_state):
        self.size = 3
        self.cur_state = init_state
        self.target_pos = self.__get_target_pos()
        self.state_history.append(self.cur_state)

    def __init__with_state_size(self, init_state, size):
        self.size = size
        self.cur_state = init_state
        self.target_pos = self.__get_target_pos()
        self.state_history.append(self.cur_state)

    def __new_state(self, direction):
        if direction == DIRECTION_UP:
            return self.__single_move(1, 0)
        elif direction == DIRECTION_RIGHT:
            return self.__single_move(0, -1)
        elif direction == DIRECTION_DOWN:
            return self.__single_move(-1, 0)
        elif direction == DIRECTION_LEFT:
            return self.__single_move(0, 1)
        else:
            return None

    def __single_move(self, dx, dy):
        x = self.target_pos[0]
        y = self.target_pos[1]
        if x + dx < 0 or x + dx >= self.size:
            return None
        if y + dy < 0 or y + dy >= self.size:
            return None
        new_state = self.cur_state.copy()
        new_state[x][y] = new_state[x + dx][y + dy]
        new_state[x + dx][y + dy] = 0
        return new_state

    def __get_target_pos(self):
        if self.cur_state is None:
            return None
        cell = []
        size = self.size
        for i in range(0, size):
            for j in range(0, size):
                if self.cur_state[i][j] != 0:
                    continue
                cell.append(i)
                cell.append(j)
                return cell
        return None

    def __next_state(self, direction):
        if self.cur_state is None or self.target_pos is None:
            return None
        return self.__new_state(self, direction)

    def get_current_state(self):
        return self.cur_state

    def update_state(self, state):
        self.cur_state = state

    def get_next_states(self):
        states = []
        for direction in self.path:
            states.append(self.__next_state(direction))
        return states

    def is_success(self):
        start = 1
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.cur_state[i][j] != start:
                    return False
                start += 1
        return True

    @staticmethod
    def is_same_state(state1, state2):
        if state1.size != state2.size:
            return False
        size = state1.size
        for i in range(0, size):
            for j in range(0, size):
                if state1[i][j] != state2[i][j]:
                    return False
        return True

    @staticmethod
    def random_sate(size):
        rand_state = []
        nums = Puzzle.get_rand_list(size)
        for i in range(0, size):
            rand_state.append([])
            for j in range(0, size):
                rand = Puzzle.get_random(nums)
                nums.remove(rand)
                rand_state[i].append(rand)
        return rand_state

    @staticmethod
    def get_rand_list(size):
        num_range = size * size
        nums = []
        start = 0
        for i in range(0, num_range):
            nums.append(start)
            start += 1
        return nums

    @staticmethod
    def get_random(nums):
        size = len(nums)
        index = random.randint(0, size - 1)
        return nums[index]
