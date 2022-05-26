"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

from lib2to3.pytree import Node


class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index]
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Create one queue instance, add two nodes to the queue and the last node should be 
# added to the end of the queue
# The enqueue function shall add a node to the back of the queue.
# Expected Result: [3 (Pri:First), 4 (Pri:Second)]
print("Test 1")

queue = Priority_Queue()
queue.enqueue('First', 3)
queue.enqueue('Second', 4)
print(queue)

# Defect(s) Found: 
# None

print("=================")

# Test 2
# Scenario: Create 3 nodes and enqueue both, call the dequeue function to remove
# the one that has the highest priority.
# The dequeue function shall remove the node with the highest priority and return its value.
# Expected Result: [3 (Pri:First), 2 (Pri:Third)]
print("Test 2")

queue = Priority_Queue()
queue.enqueue('First', 3)
queue.enqueue('Second', 4)
queue.enqueue('Third', 2)
print(queue.dequeue())
print(queue)
# Defect(s) Found: 
# Dequeue function returns the highest prio item but not removing it.

print("=================")
# Test 3
# Scenario: 
# If there are more than one node with the highest priority, 
# then the item closest to the front of the queue will be removed and its value returned.
# Expected Result: [First (Pri:3), Third (Pri:4), Forth (Pri:2), ]

print("Test 3")

queue = Priority_Queue()
queue.enqueue('First',3)
queue.enqueue('Second',4)
queue.enqueue('Third',4)
queue.enqueue('Forth',2)
print(queue.dequeue())
print(queue)
# Defect(s) Found: 
# With the same prio, the latter one is returned and removed.

print("=================")
# Test 4
# Scenario: Create a queue and call dequeue without any item in the queue
# If the queue is empty, then an error message will be displayed.
# Expected Result: The queue is empty.

print("Test 4")
queue = Priority_Queue()
queue.dequeue()
# Defect(s) Found: 
# None
print("=================")
