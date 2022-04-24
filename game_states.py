import pygame
from pygame_utils import Drawer
from game_levels import easy_game_board_init, hard_game_board_init

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


class Game:
    def __init__(self) -> None:
        self.game_state = Initial_State(self)
        self.run = True

    def change_state(self, new_state):
        self.game_state = new_state

    def play(self):
        self.game_state.draw()
        while self.game_state.execute() != -1:
            pass
        pygame.quit()


class Game_State:
    def __init__(self, game) -> None:
        self.game = game
        self.drawer = Drawer(WINDOW_WIDTH, WINDOW_HEIGHT)

    def draw(self):
        pass

    def execute(self):
        pass


class Puzzle_State(Game_State):
    def __init__(self, game, board) -> None:
        super().__init__(game)
        self.board = board

    def draw(self):
        return self.drawer.draw_board(self.board)

    def execute(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    new_state = Initial_State(
                        self.game)
                    new_state.draw()
                    self.game.change_state(new_state)
                if event.key == pygame.K_1:
                    self.drawer.toggle_attacked_squares()
                    self.drawer.draw_board(self.board)
                if event.key == pygame.K_2:
                    solution_squares = self.board.solve()
                    self.drawer.draw_solution(self.board, solution_squares)


class Initial_State(Game_State):
    def __init__(self, game) -> None:
        super().__init__(game)

    def draw(self):
        return self.drawer.draw_initial_menu()

    def execute(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    new_state = Puzzle_State(
                        self.game, easy_game_board_init())
                    new_state.draw()
                    self.game.change_state(new_state)

                elif event.key == pygame.K_2:
                    new_state = Puzzle_State(
                        self.game, hard_game_board_init())
                    new_state.draw()
                    self.game.change_state(new_state)
                elif event.key == pygame.K_3:
                    return -1
