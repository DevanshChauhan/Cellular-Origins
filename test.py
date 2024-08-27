# Test case 1
print("Test case 1")
commands = [
    "PLACE 0,0,NORTH\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_1.txt", "w") as f:
    f.writelines(commands)

# Test case 2
print("Test case 2")
commands = [
    "PLACE 0,0,NORTH\n",
    "LEFT\n",
    "REPORT\n"
]

with open("test_case_2.txt", "w") as f:
    f.writelines(commands)

# Test case 3
print("Test case 3")
commands = [
    "PLACE 1,2,EAST\n",
    "MOVE\n",
    "MOVE\n",
    "LEFT\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_3.txt", "w") as f:
    f.writelines(commands)

# Test case: Robot not placed yet, ignoring all commands
commands = [
    "MOVE\n",
    "LEFT\n",
    "REPORT\n",
    "RIGHT\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_robot_not_placed.txt", "w") as f:
    f.writelines(commands)

# Test case: Robot at the north edge, trying to move off
commands = [
    "PLACE 0,4,NORTH\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_at_edge_north.txt", "w") as f:
    f.writelines(commands)

# Test case: Robot at the west edge, trying to move off
commands = [
    "PLACE 0,0,WEST\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_at_edge_west.txt", "w") as f:
    f.writelines(commands)

# Test case: Robot at the south edge, trying to move off
commands = [
    "PLACE 0,0,SOUTH\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_at_edge_south.txt", "w") as f:
    f.writelines(commands)

# Test case: Robot at the east edge, trying to move off
commands = [
    "PLACE 4,0,EAST\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_at_edge_east.txt", "w") as f:
    f.writelines(commands)

# Test case: Invalid PLACE commands
commands = [
    "PLACE 2,2,NORTH\n",
    "PLACE 6,6,SOUTH\n",
    "REPORT\n"
]

with open("test_case_invalid_place.txt", "w") as f:
    f.writelines(commands)

# Test case: Multiple moves at the edge
commands = [
    "PLACE 0,4,NORTH\n",
    "MOVE\n",
    "MOVE\n",
    "MOVE\n",
    "REPORT\n"
]

with open("test_case_multiple_moves_at_edge.txt", "w") as f:
    f.writelines(commands)

# Test case: Invalid PLACE commands (out of bounds)
commands = [
    "PLACE 5,5,EAST\n",
    "REPORT\n",
    "PLACE -1,0,SOUTH\n",
    "REPORT\n",
    "PLACE 0,-1,NORTH\n",
    "REPORT\n"
]

with open("test_case_invalid_place_out_of_bounds.txt", "w") as f:
    f.writelines(commands)