# a) Write a program that takes in an input file and prints out a list with the final order of who’s in the queue.

"""Each line in the txt file contains JUMP" or "JOIN", followed by a name. "JUMP" means the person goes to the front of the queue "JOIN" means the person joins at the back of the queue. The goal is to print out the final order of the queue.

# Python’s collections module has several container data types. I have chosen to use deque (double-ended queue) as it will be suitable for adding and removing elements from both ends efficiently, approximately the same O(1) performance in either direction"""

from collections import deque

def jumping_queue(filepath):
    queue = deque()

    with open(filepath, 'r') as file:
        for line in file:
            action, name = line.strip().split()
            if action == 'JUMP':
                queue.appendleft(name)
            elif action == 'JOIN':
                queue.append(name)

    return list(queue)

# Call the function and print the result
final_queue = jumping_queue('homework3/hw3_q1.txt')
print(final_queue)


# b) What is the time and space complexity of your solution? If you are making any assumptions, list them.

"""Time and Space complexities help us understand how efficient a program is regarding time and memory, particularly as we deal with larger amounts of data."""

"""Let's assume the number of lines in `hw3_q1.txt` as \( n \).The cost of string operations (like `split()`) is assumed to be linear in the size of the string, which is relatively small and fixed in this context (commands like "JUMP" and "JOIN"). The time complexity of appending to and popping from a `deque` (from either end) is \( O(1) \). The space complexity is primarily governed by the space needed to store the queue. In the worst case, every line in the file results in a new name being added to the queue. Thus, if there are \( n \) lines, the queue can have up to \( n \) elements in it.
Overall the space complexity is \( O(n) \), where \( n \) is the number of lines in the file.
"""

