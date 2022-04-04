
import pygame

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (192, 192, 192)


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
                else:
                    attackingPieces = matrix[y][x].attackedBy
                    if len(attackingPieces) > 0:
                        pygame.draw.rect(self.window, GRAY_COLOR,
                                         (upper_width, upper_height, rect_width, rect_height))

                pygame.draw.rect(self.window, BLACK_COLOR,
                                 (upper_width, upper_height, rect_width, rect_height), rect_border_width)

        pygame.display.update()
