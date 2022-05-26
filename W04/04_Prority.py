"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

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
        new_node = Priority_Queue.Node(priority, value)
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
        result = result[:-2]
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Input 2 nodes. (a with 13 prio, b with 2 prio)
# The enqueue function shall add a node to the back of the queue.
# Expected Result: the last added node should be printed [a (Prio: 13), b (Prio: 2)]
print("Test 1")
nodes = Priority_Queue()
nodes.enqueue(13, 'a')
nodes.enqueue(2, 'b')
print(nodes)

# Defect(s) Found: 
# none

print("=================")

# Test 2
# Scenario: input 3 nodes with different priorities, mix the priority values. (a with 13 prio, b with 2 prio, c with 20 prio)
# The dequeue function shall remove the node with the highest priority and return its value.
# Expected Result: c will be return because it has the highest prio, it should also be removed from the list [a (Prio: 13), b (Prio: 2)]
print("Test 2")
nodes = Priority_Queue()
nodes.enqueue(13, 'a')
nodes.enqueue(2, 'b')
nodes.enqueue(20, 'c')
print(nodes.dequeue())
print(nodes)
# Defect(s) Found: 
# The dequeue function was not removing the node with the highest prio

print("=================")

# Test 3
# Scenario: input b and c with the same highest prio in the queue.
# If there are more than one node with the highest priority, 
# then the item closest to the front of the queue will be removed and its value returned.
# Expected Result: b should be returned and removed because it enter the queue first.
print("Test 3")
nodes = Priority_Queue()
nodes.enqueue(13, 'a')
nodes.enqueue(20, 'b')
nodes.enqueue(20, 'c')
nodes.enqueue(2, 'd')
print(nodes.dequeue())
print(nodes)

# Defect(s) Found: 
# If there is a node with the same prio, the latter one will be removed. We dont want that we want the first one.

print("=================")
# Test 4
# Scenario: call dequeue before adding anything to the queue
# If the queue is empty, then an error message will be displayed.
# Expected Result: error message.
print("Test 4")
nodes = Priority_Queue()
nodes.dequeue()

# Defect(s) Found: 
# None
print("=================")
