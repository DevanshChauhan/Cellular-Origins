# Cellular-Origins
This repository contains the files for the Coding challenge  Solutions

---

# Toy Robot Simulator

This is a simulation of a toy robot moving on a 5x5 square tabletop based on a series of commands (`PLACE`, `MOVE`, `LEFT`, `RIGHT`, and `REPORT`). The robot moves within the bounds of the tabletop and must avoid falling off.

## Features

- The robot can be placed at a valid position on the tabletop using the `PLACE` command.
- The robot can move one unit at a time in the direction it is facing using the `MOVE` command.
- The robot can rotate 90 degrees left or right using the `LEFT` and `RIGHT` commands.
- The `REPORT` command outputs the robot's current position and facing direction.
- The robot does not respond to commands until a valid `PLACE` command is executed.
- Commands that would move the robot off the table are ignored, ensuring the robot remains within bounds.

## Edge Cases Handled

1. **Robot not placed on the table**: 
   - The robot ignores all commands until a valid `PLACE` command is issued.
   - Example: Before a valid `PLACE` command, `MOVE`, `LEFT`, `RIGHT`, and `REPORT` will be ignored.
   
2. **Robot at the edge of the table**: 
   - If the robot is placed at the edge of the table and is commanded to move off the table, the move is ignored.
   - Example: If the robot is at (0, 4) facing north, a `MOVE` command will be ignored to prevent the robot from falling off the table.

3. **Invalid PLACE commands**: 
   - Commands with out-of-bounds positions like `PLACE 6,6,EAST` or `PLACE -1,0,NORTH` are ignored.

4. **Multiple moves at the boundary**: 
   - Even if multiple `MOVE` commands are issued at the boundary, they are ignored, keeping the robot within the table.

## Test Cases

Several test cases are provided to validate the behavior of the robot:

- **Test Case: Robot not placed yet**: Tests the behavior before a valid `PLACE` command.
- **Test Case: Edge boundaries**: Tests moving the robot at the north, south, east, and west edges of the table.
- **Test Case: Invalid PLACE commands**: Tests how the robot handles invalid placement commands.
- **Test Case: Multiple moves at edge**: Ensures the robot doesn't move off the table when at the boundary.

## Directory Structure

```
/toy_robot_simulation
    ├── main.py            # Main robot simulation code
    ├── test.py            # Script that generates test case files
    ├── run_tests.sh       # Script that automates running the test cases
    ├── text Cases 
    └── README.md          # This file
```

## How to Run the Code

Follow these steps to run the code on a new system:

### Prerequisites

Ensure you have Python installed on your system. You can check by running:

```bash
python3 --version
```

If Python is not installed, you can install it from the [official Python website](https://www.python.org/).

### Step 1: Clone the Repository

To clone this repository to your local machine, use the following command in your terminal:

```bash
git clone https://github.com/DevanshChauhan/Cellular-Origins
```

Then navigate to the project folder:

```bash
cd Cellular-Origins
```

### Step 2: Run the Test Case Generator

Generate the test case files by running the `test.py` script:

```bash
python3 test.py
```

This will create several test case files like `test_case_1.txt`, `test_case_2.txt`, etc.

### Step 3: Run the Tests

To run all the test cases automatically, you can use the provided `run_tests.sh` script. This will pipe the commands from the test files into `main.py` and display the results in the terminal:

```bash
./run_tests.sh
```

Make sure the script is executable by running the following command (if needed):

```bash
chmod +x run_tests.sh
```

### Step 4: Analyze the Output

The output of each test case will be displayed in the terminal. For example:

```
Running Test Case 1
Robot is not on the table.
Robot is not on the table.

Running Test Case 2
0,4,NORTH

Running Test Case 3
4,0,EAST

Running Test Case 4
Robot is not on the table.
```

### Adding New Test Cases

1. **Modify `test.py`**: To add more test cases, simply edit the `test.py` file. Write the commands for the new test cases in the format:

```python
# Example: New Test Case
commands = [
    "PLACE 1,1,NORTH\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_new.txt", "w") as f:
    f.writelines(commands)
```

2. **Run `test.py`**: Execute the `test.py` script again to generate the new test case file.

```bash
python3 test.py
```

3. **Update `run_tests.sh`**: Add the following lines to the `run_tests.sh` file to ensure your new test case is executed:

```bash
echo "Running New Test Case"
cat test_case_new.txt | python3 main.py
echo ""
```

4. **Run the tests**:

```bash
./run_tests.sh
```

The output of the new test case will be displayed along with the others.
### Running the Code in User interative mode
```bash
python3 main.py
```
This would allow the user to interact with robot and give step by step instructions for the same
The user can type in the location and various commands.
This mode can be exited by typing the word  EXIT in the command line.


---

## License

This project is licensed under the MIT License.

---

By following the steps above, you will be able to set up, run, and test the Toy Robot Simulator on any system. Feel free to extend the project with more test cases or features, and don't forget to run the tests after any changes!
