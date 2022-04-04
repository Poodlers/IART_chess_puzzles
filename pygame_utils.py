
import pygame
from a_star import AStarNode

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (192, 192, 192)
GREEN_COLOR = (0, 200, 0)


def setup_pygame_window(window_width, window_height):
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Chess Puzzles")
    return window


class PuzzleDrawer:
    def __init__(self, window_width, window_height) -> None:
        self.window = setup_pygame_window(window_width, window_height)
        self.window_width = window_width
        self.window_height = window_height
        self.show_attacked_squares = True
        self.load_sprites()

    def load_sprites(self):
        queen_sprite = pygame.image.load(
            "piece_sprites/queen_sprite.png").convert_alpha()

        self.sprites = {"Q": queen_sprite}

    def draw(self, board):
        self.draw_board(board)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.KEYUP:
                        self.show_attacked_squares = not self.show_attacked_squares
                        self.draw_board(board)
                    if event.key == pygame.K_RETURN:
                        solution_squares = board.solve()
                        self.draw_solution(board, solution_squares)

    def draw_solution(self, board, solution_squares):
        rect_width = int(self.window_width / board.size)
        rect_height = int(self.window_height / board.size)
        for node in solution_squares:
            node_pos = node.position
            upper_width = node_pos.x * rect_width
            upper_height = node_pos.y * rect_height
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
                textRep = matrix[y][x].textRepresentation
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
