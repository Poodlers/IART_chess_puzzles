from time import sleep
from position import Position


class AStarNode:
    def __init__(self, position, h_value, g_value, parent_node) -> None:
        self.position = position
        self.h = h_value
        self.g = g_value
        self.parent_node = parent_node
        self.f = self.h + self.g

    def get_all_antecessor_nodes(self, initial_point, antecessor_nodes):
        if self.parent_node.position == initial_point.position:
            return
        antecessor_nodes.append(self.parent_node)
        self.parent_node.get_all_antecessor_nodes(
            initial_point, antecessor_nodes)

    def get_node_sucessors(self, board_size, final_point):
        successors = []

        sucessor_generation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for suc in sucessor_generation:
            suc_x = self.position.x + suc[0]
            suc_y = self.position.y + suc[1]
            suc_pos = Position(suc_x, suc_y)
            if suc_x >= 0 and suc_x < board_size and suc_y >= 0 and suc_y < board_size:
                suc_g = self.g + \
                    suc_pos.get_manhattan_distance_between(self.position)
                suc_h = suc_pos.get_manhattan_distance_between(
                    final_point.position)
                sucessor = AStarNode(suc_pos, suc_h, suc_g, self)
                successors.append(sucessor)
        return successors


class AStarSolver:
    def __init__(self, initial_point, final_point, board_size) -> None:
        self.initial_point = initial_point
        self.final_point = final_point
        self.board_size = board_size

    def get_least_f(self, open_list):
        least_f_node = None
        least_f_value = 9999
        for node in open_list:
            if node.f < least_f_value:
                least_f_node = node
                least_f_value = node.f
        return least_f_node

    def solve(self):
        open_list = [self.initial_point]
        closed_list = []

        def check_better_node_in_list(node, node_list):
            for open_node in node_list:
                if open_node.position == node.position and open_node.f <= node.f:
                    return True
            return False

        while len(open_list) > 0:
            node_to_explore = self.get_least_f(open_list)
            open_list.remove(node_to_explore)
            node_sucessors = node_to_explore.get_node_sucessors(
                self.board_size, self.final_point)
            print(node_to_explore.position)

            for node in node_sucessors:
                if node.position == self.final_point.position:
                    node_antecessors = []
                    node.get_all_antecessor_nodes(
                        self.initial_point, node_antecessors)
                    return node_antecessors
                if check_better_node_in_list(node, open_list):
                    continue
                if check_better_node_in_list(node, closed_list):
                    continue
                open_list.append(node)

            closed_list.append(node_to_explore)
