import random
import pytest


class TestMaze:
    def setup_class(cls):
        # inicjalizacja planszy i ustawień testowych
        cls.width = 7
        cls.height = 10
        cls.start = (0, random.randint(1, cls.height - 2))
        cls.end = (cls.width - 1, random.randint(1, cls.height - 2))
        cls.maze = [[0 for _ in range(cls.width)] for _ in range(cls.height)]
        cls.maze[cls.start[1]][cls.start[0]] = 'A'
        cls.maze[cls.end[1]][cls.end[0]] = 'B'
        cls.obstacles = []
        while len(cls.obstacles) < 5:
            x, y = random.randint(1, cls.width - 2), random.randint(1, cls.height - 2)
            if (x, y) not in (cls.start, cls.end) and (x, y) not in cls.obstacles:
                cls.obstacles.append((x, y))
                cls.maze[y][x] = 'X'

    def teardown_class(cls):
        # sprzątanie po testach
        pass

    def setup_method(self):
        # inicjalizacja pozycji startowej gracza
        self.player_pos = self.start

    def teardown_method(self):
        # sprzątanie po teście
        pass

    def test_generate_maze(self):
        # test generowania planszy
        assert len(self.maze) == self.height
        assert all(len(row) == self.width for row in self.maze)

    def test_obstacles(self):
        # test poprawności generowania przeszkód
        assert len(self.obstacles) == 5
        assert all(isinstance(pos, tuple) and len(pos) == 2 for pos in self.obstacles)
        assert all(pos not in (self.start, self.end) for pos in self.obstacles)

    @pytest.mark.parametrize("direction,expected", [
        ('up', (0, 0)),
        ('down', (0, 2)),
        ('left', (0, 1)),
        ('right', (2, 1)),
    ])
    def test_move_player(self, direction, expected):
        # test poruszania się gracza w różnych kierunkach
        if direction == 'up' and self.player_pos[1] == 0:
            pytest.skip("Cannot move up from top row")
        elif direction == 'down' and self.player_pos[1] == self.height - 1:
            pytest.skip("Cannot move down from bottom row")
        elif direction == 'left' and self.player_pos[0] == 0:
            pytest.skip("Cannot move left from leftmost column")
        elif direction == 'right' and self.player_pos[0] == self.width - 1:
            pytest.skip("Cannot move right from rightmost column")
        elif (expected[0], expected[1]) in self.obstacles:
            pytest.xfail("Cannot move onto an obstacle")
        else:
            self.player_pos = expected
            assert self.maze[self.player_pos[1]][self.player_pos[0]] != 'X'

    def test_win(self):
        assert self.player_pos != self.end
        self.player_pos = self.end
        assert self.player_pos == self.end
