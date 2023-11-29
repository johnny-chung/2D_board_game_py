#    Main Author(s): Wai Tan Wong (18540710)
#    Main Reviewer(s): Chi Ching Cheung, Wai Yin Chung


# A basic Stack implementation using a dynamic array
class Stack:

	# stack : The underlying data structure to store stack elements
	# cap : Capacity of the stack. It doubles when limit is reached
	# top : Index of the topmost element in the stack. Initialized to -1 indicating an empty stack
	# Initializes a new Stack object with a specified capacity
	def __init__(self, cap=10):
		self.stack = [None] * cap
		self.cap = cap
		self.top = -1

	# Returns the current capacity of the stack
	# return | The current capacity of the stack
	def capacity(self):
		return self.cap

	# Pushes an element onto the top, doubling capacity and reordering if full
	# arg | data: The element to be pushed onto the stack
	def push(self, data):

		# if the stack reaches its capacity, create a temporary stack with twice the size
		# copy elements from original deque to temporary one
		if self.top + 1 == self.cap:
			self.cap *= 2
			tmp_stack = [None] * self.cap
			for i in range(self.top + 1):
				tmp_stack[i] = self.stack[i]
			self.stack = tmp_stack

		self.top += 1
		self.stack[self.top] = data

	# Pops and returns the topmost element of the stack
	# return | The topmost element of the stack
	def pop(self):

		# if call an empty stack raise IndexError
		if self.top == -1:
			raise IndexError('pop() used on empty stack')

		data = self.stack[self.top]
		self.stack[self.top] = None
		self.top -= 1
		return data

	# Retrieves the topmost element of the stack without removing it
	# return | The topmost element if the stack is not empty, otherwise None
	def get_top(self):
		return self.stack[self.top] if self.top >= 0 else None

	# Checks if the stack is empty
	# return | bool : True if the stack is empty, otherwise False
	def is_empty(self):
		return self.top == -1

	# Returns the number of elements currently in the stack
	# return | The size of the stack
	def __len__(self):
		return self.top + 1

# A dynamic-size queue data structure
class Queue:

	# queue : Underlying data structure to hold the queue elements.
	# cap : Maximum capacity of the queue.
	# front : Index pointing to the front of the queue.
	# back : Index pointing to the back of the queue.
	# size : Current number of elements in the queue.
	# Initializes a new Queue object with a specified capacity
	def __init__(self, cap=10):
		self.queue = [None] * cap
		self.cap = cap
		self.front = 0
		self.back = 0
		self.size = 0

	# Returns the current capacity of the queue.
	# return | The capacity of the queue.
	def capacity(self):
		return self.cap

	# Inserts an element at the back of the queue, doubling capacity and reordering if full
	# arg | data: The element to be inserted into the queue
	def enqueue(self, data):
		if self.size == self.cap:
			self.cap *= 2

			# if the queue reaches its capacity, create a temporary queue with twice the size
			# copy elements from original deque to temporary one
			tmp_queue = [None] * self.cap
			for i in range(self.size):
				# Transfer elements using ring structure and modulus for correct order
				tmp_queue[i] = self.queue[(self.front + i) % self.size]

			self.front = 0
			self.back = self.size
			self.queue = tmp_queue

		# assign new data to the back of the queue
		self.queue[self.back] = data

		# Update the back pointer in a circular fashion by using modulus operation
		self.back = (self.back + 1) % self.cap
		self.size += 1

	# Removes and returns the front element of the queue
	# return | The frontmost element of the queue
	def dequeue(self):

		# if call an empty queue raise IndexError
		if self.size < 1:
			raise IndexError('dequeue() used on empty queue')

		data = self.queue[self.front]
		self.queue[self.front] = None
		# Update the front pointer in a circular fashion by using modulus operation
		self.front = (self.front + 1) % self.cap
		self.size -= 1
		return data

	# Retrieves the front element of the queue without removing it
	# return | The frontmost element if the queue is not empty, otherwise None
	def get_front(self):
		return self.queue[self.front] if self.size > 0 else None

	# Checks if the queue is empty
	# return | bool : True if the queue is empty, otherwise False
	def is_empty(self):
		return self.size < 1

	# Returns the number of elements currently in the queue
	# return | The size of the queue
	def __len__(self):
		return self.size

# a double-ended queue that allows items to be added and removed from both the front and rear
class Deque:

	# deque : A list to store the elements.
	# cap : The current capacity of the deque.
	# front : The index of the first element in the deque.
	# back : The index of the last element in the deque.
	# size : The number of elements currently in the deque.
	# Initializes a new Deque object with a specified capacity
	def __init__(self, cap=10):
		self.deque = [None] * cap
		self.cap = cap
		self.front = 0
		self.back = 0
		self.size = 0

	# Returns the current capacity of the deque.
	# return | The capacity of the deque.
	def capacity(self):
		return self.cap

	# Inserts an element at the front, doubling capacity and reordering if full
	# arg | data: The element to be inserted into the deque at the front.
	def push_front(self, data):

		# if the deque reaches its capacity, create a temporary deque with twice the size
		# copy elements from original deque to temporary one
		if self.size == self.cap:
			self.cap *= 2
			tmp_deque = [None] * self.cap
			for i in range(self.size):
				# Transfer elements using ring structure and modulus for correct order
				tmp_deque[i + 1] = self.deque[(self.front + i) % self.size]

			self.front = 1
			self.back = self.size
			self.deque = tmp_deque

		if self.size > 0:
			# Adjust the front index in a circular fashion using modulus operation
			# even when the front is at the last index
			self.front = (self.front - 1) % self.cap

		self.deque[self.front] = data
		self.size += 1

	# Inserts an element at the back, doubling capacity and reordering if full
	# arg | data: The element to be inserted into the deque at the back.
	def push_back(self, data):

		# if the deque reaches its capacity, create a temporary deque with twice the size
		# copy elements from original deque to temporary one
		if self.size == self.cap:
			self.cap *= 2
			tmp_deque = [None] * self.cap
			for i in range(self.size):
				# Transfer elements using ring structure and modulus for correct order
				tmp_deque[i] = self.deque[(self.front + i) % self.size]

			self.front = 0
			self.back = self.size - 1
			self.deque = tmp_deque

		if self.size > 0:
			# Adjust the back index in a circular fashion using modulus operation
			# even when the back is at the first index
			self.back = (self.back + 1) % self.cap

		self.deque[self.back] = data
		self.size += 1

	# Removes and returns the front element of the deque.
	# return | The frontmost element of the deque.
	def pop_front(self):
		# If called on an empty deque, raises IndexError.
		if self.size < 1:
			raise IndexError('pop_front() used on empty deque')

		# assign the element to data and remove it from the deque
		data = self.deque[self.front]
		self.deque[self.front] = None

		# Adjust the front index in a circular fashion using modulus operation
		# even when the front is at the last index
		self.front = (self.front + 1) % self.cap
		self.size -= 1
		return data

	# Removes and returns the back element of the deque.
	# return | The rearmost element of the deque.
	def pop_back(self):
		# If called on an empty deque, raises IndexError.
		if self.size < 1:
			raise IndexError('pop_back() used on empty deque')

		# assign the element to data and remove it from the deque
		data = self.deque[self.back]
		self.deque[self.back] = None

		# Adjust the back index in a circular fashion using modulus operation
		# even when the back is at the first index
		self.back = (self.back - 1) % self.cap
		self.size -= 1
		return data

	# Retrieves the front element of the deque without removing it.
	# return | The frontmost element if the deque is not empty, otherwise None.
	def get_front(self):
		return self.deque[self.front] if self.size > 0 else None

	# Retrieves the back element of the deque without removing it.
	# return | The rearmost element if the deque is not empty, otherwise None.
	def get_back(self):
		return self.deque[self.back] if self.size > 0 else None

	# Checks if the deque is empty
	# return | bool : True if the deque is empty, otherwise False
	def is_empty(self):
		return self.size < 1

	# Retrieves the number of elements currently in the deque
	# return | The size of the deque
	def __len__(self):
		return self.size

	# Retrieves the 'k'th element from front using ring structure indexing
	# arg | k: The index to access.
	# return | The element at index k.
	def __getitem__(self, k):
		# raises IndexError If k is out of bounds
		if k >= self.cap:
			raise IndexError('Index out of range')
		# Retreive the kth element in a circular fashion using modulus operation
		return self.deque[(self.front + k) % self.cap]

