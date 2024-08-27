#!/bin/bash

# Run test case 1
echo "Running Test Case 1"
cat test_case_1.txt | python3 main.py
echo ""

# Run test case 2
echo "Running Test Case 2"
cat test_case_2.txt | python3 main.py
echo ""

# Run test case 3
echo "Running Test Case 3"
cat test_case_3.txt | python3 main.py
echo ""

# Run test case 4
echo "Running test case 4: Robot not placed yet"
cat test_case_robot_not_placed.txt | python3 main.py
echo ""

# Run test case 5
echo "Running  Test Case  5 : At the north edge"
cat test_case_at_edge_north.txt | python3 main.py
echo ""

# Run test case 6
echo "Running Test Case 6 : At the west edge"
cat test_case_at_edge_west.txt | python3 main.py
echo ""

# Run test case 7
echo "Running Test Case 7 : At the south edge"
cat test_case_at_edge_south.txt | python3 main.py
echo ""

# Run test case 8
echo "Running Test Case 8 : At the east edge"
cat test_case_at_edge_east.txt | python3 main.py
echo ""

# Run test case 9
echo "Running Test Case 9 : Invalid PLACE commands"
cat test_case_invalid_place.txt | python3 main.py
echo ""

# Run test case 10
echo "Running Test Case 10 : Multiple moves at edge"
cat test_case_multiple_moves_at_edge.txt | python3 main.py
echo ""

# Run test case 11
echo "Running Test Case 11 : Out of bounds PLACE commands"
cat test_case_invalid_place_out_of_bounds.txt | python3 main.py
echo ""
