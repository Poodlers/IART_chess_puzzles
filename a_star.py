from time import sleep
from chess_piece import ChessPiece
from position import Position
from itertools import combinations
from node import Node
from solver import Solver


def combine(arr, s):
    return list(combinations(arr, s))


def calculate_snake_ineq_heuristic(snake, board, chess_pieces):
    attacking_pieces = {}
    for i in chess_pieces:
        attacking_pieces[i.textRepresentation] = 0
    for pos in snake:
        for piece in board[pos.x][pos.y].getAttackingPieces():
            attacking_pieces[piece.textRepresentation] += 1

    """ 
    print("Snake is: ")
    print("[ ", end="")
    for pos in snake:
        print(pos)
    print(" ]")
    print(attacking_pieces)
    """
    combinations = combine(attacking_pieces.keys(), 2)
    final_result = 0
    for combination in combinations:
        final_result += abs(attacking_pieces[combination[0]] -
                            attacking_pieces[combination[1]])
    return final_result


class AStarNode(Node):
    def __init__(self, snake, h_value, g_value) -> None:
        super().__init__(snake)
        self.h = h_value
        self.g = g_value
        self.f = self.h + self.g

    def get_node_sucessors(self, board_size, board, chess_pieces):
        successors = []

        sucessor_generation = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for suc in sucessor_generation:
            suc_x = self.snake[-1].x + suc[0]
            suc_y = self.snake[-1].y + suc[1]
            suc_pos = Position(suc_x, suc_y)
            if suc_x >= 0 and suc_x < board_size and suc_y >= 0 and suc_y < board_size and suc_pos not in self.snake and self.not_adjacent_to_snake(suc_pos) and type(board[suc_pos.x][suc_pos.y]) != ChessPiece:
                new_snake = self.snake + [suc_pos]
                suc_g = self.g + 1
                suc_h = calculate_snake_ineq_heuristic(new_snake,
                                                       board, chess_pieces)
                sucessor = AStarNode(new_snake, suc_h, suc_g)
                successors.append(sucessor)
        return successors


class AStarSolver(Solver):
    def __init__(self, initial_node, final_pos, board_size, board, chess_pieces) -> None:
        super().__init__(initial_node, final_pos, board_size, board, chess_pieces)

    def get_next_node(self, open_list):
        least_f_node = None
        least_f_value = 9999
        longest_snake_size = -1
        for node in open_list:
            if len(node.snake) > longest_snake_size or (len(node.snake) == longest_snake_size and node.f < least_f_value):
                least_f_node = node
                least_f_value = node.f
                longest_snake_size = len(node.snake)

        return least_f_node

    def solve(self):
        open_list = [self.initial_node]
        closed_list = []
        nodes_num = 0

        def check_better_node_in_list(node, node_list):
            for open_node in node_list:
                if open_node.snake == node.snake and open_node.f <= node.f:
                    return True
            return False

        while len(open_list) > 0:
            node_to_explore = self.get_next_node(open_list)
            open_list.remove(node_to_explore)
            node_sucessors = node_to_explore.get_node_sucessors(
                self.board_size, self.matrix, self.chess_pieces)
            nodes_num += 1
            # draw here open nodes and closed ones

            #puzzle_drawer.draw_intermediate( open_list, closed_list, self.board_size)
            for node in node_sucessors:
                #print("node H, at : ", node.h, node.snake[-1])
                if node.snake[-1] == self.final_pos and node.h == 0:
                    print("num_of_visited nodes: ", nodes_num)
                    return node.snake
                if check_better_node_in_list(node, open_list):

                    continue
                if check_better_node_in_list(node, closed_list):

                    continue
                open_list.append(node)

            closed_list.append(node_to_explore)
