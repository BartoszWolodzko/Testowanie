import random


class MazeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[None for _ in range(width)] for _ in range(height)]
        self.obstacles = set()
        self.generate_maze()
        self.start = self.find_empty()
        self.end = self.find_empty(exclude=[self.start])
        self.obstacles = set()
        self.generate_obstacles()
        self.player_pos = None
        self.generate_start()
        self.generate_end()

    def generate_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or y == 0 or x == self.width-1 or y == self.height-1:
                    self.maze[y][x] = 'X'
                else:
                    self.maze[y][x] = ' '

    def generate_obstacles(self):
        obstacles = set()
        while len(obstacles) < 5:
            obstacle = self.find_empty()
            if obstacle not in [self.start, self.end]:
                obstacles.add(obstacle)
        self.obstacles = obstacles

        for obstacle in obstacles:
            x, y = obstacle
            self.maze[y][x] = 'X'

    def generate_start(self):
        self.player_pos = self.start
        x, y = self.start
        self.maze[y][x] = 'A'

    def generate_end(self):
        x, y = self.end
        self.maze[y][x] = 'B'

    def find_empty(self, exclude=None):
        exclude = exclude or []
        while True:
            x = random.randint(1, self.width-2)
            y = random.randint(1, self.height-2)
            if (x, y) not in exclude and self.maze[y][x] == ' ':
                return x, y

    def move_player(self, direction):
        x, y = self.player_pos
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        else:
            raise ValueError(f"Invalid direction: {direction}")

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"Player out of bounds: {x}, {y}")

        if (x, y) in self.obstacles:
            raise ValueError(f"Player hit obstacle: {x}, {y}")

        if self.maze[y][x] == 'X':
            raise ValueError(f"Player hit wall: {x}, {y}")

        if self.maze[y][x] == '*':
            raise ValueError(f"Player have been there: {x}, {y}")

        self.maze[self.player_pos[1]][self.player_pos[0]] = '*'
        self.maze[y][x] = 'O'
        self.player_pos = x, y

    def display(self):
        for row in self.maze:
            print(' '.join(row))


if __name__ == '__main__':
    game = MazeGame(10, 10)
    game.display()
    while game.player_pos != game.end:
        direction = input("Enter direction (up/down/left/right): ")
        try:
            game.move_player(direction)
        except ValueError as e:
            print(e)
        game.display()
    print("You won!")