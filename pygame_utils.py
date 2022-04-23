
import pygame
import time
from a_star import AStarNode

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (192, 192, 192)
GREEN_COLOR = (0, 200, 0)
BLUE_COLOR = (0, 0, 255)
RED_COLOR = (255, 0, 0)


def setup_pygame_window(window_width, window_height):
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Chess Puzzles")
    return window


class Drawer:
    def __init__(self, window_width, window_height) -> None:
        self.window = setup_pygame_window(window_width, window_height)
        self.window_width = window_width
        self.window_height = window_height
        self.show_attacked_squares = True
        self.load_sprites()

    def toggle_attacked_squares(self):
        self.show_attacked_squares = not self.show_attacked_squares

    def load_sprites(self):
        king_sprite = pygame.image.load(
            "piece_sprites/king_sprite.png").convert_alpha()

        queen_sprite = pygame.image.load(
            "piece_sprites/queen_sprite.png").convert_alpha()

        rook_sprite = pygame.image.load(
            "piece_sprites/rook_sprite.png").convert_alpha()

        knight_sprite = pygame.image.load(
            "piece_sprites/knight_sprite.png").convert_alpha()

        self.sprites = {"K": king_sprite,
                        "Q": queen_sprite,
                        "R": rook_sprite,
                        "k": knight_sprite}

    def draw_solution(self, board, solution_squares):
        rect_border_width = 2
        rect_width = int(self.window_width / board.size)
        rect_height = int(self.window_height / board.size)
        for node_pos in solution_squares:
            upper_width = node_pos.y * rect_width
            upper_height = node_pos.x * rect_height
            pygame.draw.rect(self.window, BLUE_COLOR,
                             (upper_width, upper_height, rect_width, rect_height))
            pygame.draw.rect(self.window, BLACK_COLOR,
                             (upper_width, upper_height, rect_width, rect_height), rect_border_width)

        pygame.display.update()

    def draw_intermediate(self, open_list, closed_list, board_size):
        rect_width = int(self.window_width / board_size)
        rect_height = int(self.window_height / board_size)
        for node in closed_list:
            y = node.snake[-1].x
            x = node.snake[-1].y
            upper_width = x * rect_width
            upper_height = y * rect_height
            pygame.draw.rect(self.window, RED_COLOR,
                             (upper_width, upper_height, rect_width, rect_height))
        for node in open_list:
            y = node.snake[-1].x
            x = node.snake[-1].y
            upper_width = x * rect_width
            upper_height = y * rect_height
            pygame.draw.rect(self.window, GREEN_COLOR,
                             (upper_width, upper_height, rect_width, rect_height))

        pygame.display.update()

    def draw_board(self, board):
        self.window.fill(WHITE_COLOR)
        rect_border_width = 2
        matrix = board.matrix
        rect_width = int(self.window_width / board.size)
        rect_height = int(self.window_height / board.size)
        for x in range(board.size):
            upper_width = x * rect_width
            for y in range(board.size):
                upper_height = y * rect_height
                textRep = matrix[y][x].textRepresentation[0]
                if textRep != " ":
                    scaled_sprite = pygame.transform.scale(
                        self.sprites[textRep], (rect_width, rect_height))
                    self.window.blit(
                        scaled_sprite, (upper_width, upper_height, rect_width, rect_height))
                elif self.show_attacked_squares:
                    attackingPieces = matrix[y][x].attackedBy
                    if len(attackingPieces) > 0:
                        pygame.draw.rect(self.window, GRAY_COLOR,
                                         (upper_width, upper_height, rect_width, rect_height))

                pygame.draw.rect(self.window, BLACK_COLOR,
                                 (upper_width, upper_height, rect_width, rect_height), rect_border_width)

        # draw initial and final_squares

        initial_y = board.size - 1
        initial_x = 0
        upper_width = initial_x * rect_width
        upper_height = initial_y * rect_height
        pygame.draw.rect(self.window, BLACK_COLOR,
                         (upper_width, upper_height, rect_width, rect_height))
        pygame.draw.rect(self.window, BLACK_COLOR,
                         (upper_height, upper_width, rect_width, rect_height))

        pygame.display.update()

    def draw_initial_menu(self):
        self.window.fill(GRAY_COLOR)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GeeksForGeeks', True, WHITE_COLOR)
        textRect = text.get_rect()

        textRect.center = (self.window_width // 2, self.window_height // 2)
        self.window.blit(text, textRect)
        pygame.display.update()
