import sys

class Robot:
    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.table_size = 5

    def place(self, x, y, facing):
        if 0 <= x < self.table_size and 0 <= y < self.table_size and facing in self.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing

    def move(self):
        if self.x is None or self.y is None or self.facing is None:
            return
        if self.facing == 'NORTH' and self.y + 1 < self.table_size:
            self.y += 1
        elif self.facing == 'SOUTH' and self.y - 1 >= 0:
            self.y -= 1
        elif self.facing == 'EAST' and self.x + 1 < self.table_size:
            self.x += 1
        elif self.facing == 'WEST' and self.x - 1 >= 0:
            self.x -= 1

    def left(self):
        if self.facing is None:
            return
        self.facing = self.DIRECTIONS[(self.DIRECTIONS.index(self.facing) - 1) % 4]

    def right(self):
        if self.facing is None:
            return
        self.facing = self.DIRECTIONS[(self.DIRECTIONS.index(self.facing) + 1) % 4]

    def report(self):
        if self.x is not None and self.y is not None and self.facing is not None:
            print(f"{self.x},{self.y},{self.facing}")
        else:
            print("Robot is not on the table.")


class ToyRobotSimulator:
    def __init__(self):
        self.robot = Robot()

    def execute_command(self, command):
        parts = command.strip().split()

        if parts[0] == "PLACE" and len(parts) == 2:
            x, y, facing = parts[1].split(',')
            self.robot.place(int(x), int(y), facing)

        elif parts[0] == "MOVE":
            self.robot.move()

        elif parts[0] == "LEFT":
            self.robot.left()

        elif parts[0] == "RIGHT":
            self.robot.right()

        elif parts[0] == "REPORT":
            self.robot.report()

    def run_interactive(self):
        print("Toy Robot Simulator - Interactive Mode")
        print("Enter commands (e.g., PLACE 0,0,NORTH, MOVE, LEFT, RIGHT, REPORT)")
        print("Type 'EXIT' to stop.")
        while True:
            command = input("> ").strip()
            if command == "EXIT":
                print("Exiting...")
                break
            self.execute_command(command)


def run_simulation(input_stream):
    simulator = ToyRobotSimulator()
    for command in input_stream:
        simulator.execute_command(command.strip())

if __name__ == "__main__":
    # Check if there is any input stream provided (via file or piping)
    if sys.stdin.isatty():  # If no input is piped, switch to interactive mode
        ToyRobotSimulator().run_interactive()
    else:  # Otherwise, read from stdin (piped input from a file or tests)
        run_simulation(sys.stdin)
