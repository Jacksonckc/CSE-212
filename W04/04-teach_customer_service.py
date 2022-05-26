"""
CSE212 
(c) BYU-Idaho
04-Teach - Problem 2 

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Customer_Service:
    """
    Maintain a Customer Service Queue.  Allows new customers to be 
    added and allows customers to be serviced.
    """

    class Customer:
        """
        Defines a Customer record for the service queue.
        This is an inner class.  Its real name is CustomerService.Customer
        """

        def __init__(self, name, account_id, problem):
            """
            Initialize the Customer Record
            """
            self.name = name
            self.account_id = account_id
            self.problem = problem

        def __str__(self):
            """
            Return a string representing the record so we can print it out later
            """
            return self.name + " (" + self.account_id + ") : " + self.problem

    def __init__(self, max_size):
        """
        Initialize the empty queue using a Python List.  The maximum size of the 
        queue is defined by parameter passed in by the user.  If the size is 
        invalid (less than or equal to 0) then the size will default to 10.
        """
        self.queue = []
        if max_size <= 0:
            self.max_size = 10  # Default value if max size is invalid
        else:
            self.max_size = max_size
        print(self.queue)
        print(self.max_size)

    def add_new_customer(self):
        """
        Prompt the user for the customer and problem information.  Put the 
        new record into the queue.
        """
        # Verify there is room in the service queue
        if len(self.queue) >= self.max_size:
            print("Maximum Number of Customers in Queue.")
            return

        name = input("Customer Name: ")
        account_id = input("Account Id: ")
        problem = input("Problem: ")

        # Create the customer object and add it to the queue
        customer = Customer_Service.Customer(name, account_id, problem)
        self.queue.append(customer)

    def serve_customer(self):
        """
        Dequeue the next customer and display the information.
        """
        if len(self.queue) > 0:
            customer = self.queue[0]
            del self.queue[0]
            print(customer)
        else:
            print("No customers baby")

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        customer service queue.  This is useful for debugging.  If you have a 
        Customer_Service object called cs, then you run print(cs) to see the 
        contents.
        """
        result = "[size=" + str(len(self.queue)) + " max_size=" + str(self.max_size) +" => "
        for customer in self.queue:
            result += "{"+str(customer)+"}"  # Uses the __str__ from Customer class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: 
# Expected Result: 
# The user shall specify the maximum size of the Customer Service Queue 
# when it is created. If the size is invalid (less than or equal to 0) 
# then the size shall default to 10.
print("Test 1")
new_customer_service = Customer_Service(0)

# Defect(s) Found: 

print("=================")

# Test 2
# Scenario: 
# Expected Result: 
# The add_new_customer function shall enqueue a new customer into the queue.
# If the queue is full when trying to add a customer, then an error message will be displayed.
print("Test 2")
new_customer_service = Customer_Service(3)
# new_customer_service.add_new_customer()
# new_customer_service.add_new_customer()
# new_customer_service.add_new_customer()
new_customer_service.serve_customer()

# Defect(s) Found: 
# The add_new_customer function worked even when the queue is longer than the max_size.

print("=================")

# Add more Test Cases As Needed Below
# The serve_customer function shall dequeue the next customer from the queue and display the details.
# Defect(s) Found: 
# Deleting the customer before storing.


# If the queue is empty when trying to serve a customer, then an error message will be displayed.
