import time
import random

# class that represents a task and its
# various attributes
class Task:
    def __init__(self, id, priority, arrival_time=0, deadline=0):
        self.id = id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

# class that implements the task simulation
class TaskHandler:
    def __init__(self):
        self.heap = []
    
    # static method to handle heapify operation
    # this is based on part 1 implementation but modified
    # for this task priority simulation
    def heapify(inp, n, i):
        maximum, left, right = i, 2 * i + 1, 2 * i + 2

        # max heap approach since tasks with higher priority
        # are moved up towards the root of the heap
        if left < n and inp[left].priority > inp[maximum].priority:
            maximum = left
        
        if right < n and inp[right].priority > inp[maximum].priority:
            maximum = right
        
        if maximum != i:
            inp[i], inp[maximum] = inp[maximum], inp[i]
            TaskHandler.heapify(inp, n, maximum)
    
    # insert a task into the heap
    def insert(self, task):
        self.heap.append(task)
        i = len(self.heap) - 1
        while i != 0:
            parent = (i - 1) // 2
            if self.heap[i].priority > self.heap[parent].priority:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            else:
                break
    
    # extract the task with the highest priority
    # essentially extracting the root of the heap
    # and then modify the heap once this task is removed
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        TaskHandler.heapify(self.heap, len(self.heap), 0)
        return root
    
    # operation to check to see if the heap is empty
    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False
    
    # operation to increase the priority of a given task
    # to the new priority
    def increase_key(self, idx, new_prio):
        if idx < 0 or idx >= len(self.heap):
            return
        self.heap[idx].priority = new_prio
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx].priority > self.heap[parent].priority:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

def part_2_analysis():
    # run experiment for priority queue for two heap sizes
    for heap_size in (100000, 1000000):
        th = TaskHandler()

        # populate tasks so we don't count the time taken
        # as part of the operations of the heap that we
        # are analyzing
        tasks = []
        for i in range(0, heap_size):
            tasks.append(generate_task(heap_size))


        # analyze insertion time complexity
        insert_start = time.time()
        for i in range(0, heap_size):
            th.insert(tasks[i])
        insert_end = time.time()

        # analyze extraction time complexity
        extraction_start = time.time()
        for _ in range(0, heap_size):
            th.extract_max()
        extraction_end = time.time()

        # expect heap to be empty after all extractions
        # otherwise raise a runtime error
        if not th.is_empty():
            raise RuntimeError("Expected heap to be empty but is not")

        # repopulate the heap so we can analyze increase task
        for i in range(0, heap_size):
            th.insert(tasks[i])
        
        # analyze increase_key time complexity
        increase_key_start = time.time()
        for i in range(0, heap_size):
            # increases the task's priority randomly from 0 to 10 priority
            th.increase_key(i, tasks[i].priority + random.randint(0, 10))
        increase_key_end = time.time()

        print(">>>")
        print("Priority queue time complexity with heap size of " + str(heap_size))
        print("Insert Time: " + str(insert_end - insert_start))
        print("Extraction Time: " + str(extraction_end - extraction_start))
        print("Increase Key Time: " + str(increase_key_end - increase_key_start))
        print("\n")

# generate a task given the heap size so we can guarantee an
# id that is going to be unique
def generate_task(heap_size):
    arrival_time, deadline = generate_arrival_time(), generate_deadline()
    id = str(random.randint(0, heap_size - 1))
    priority = random.randint(0, 1000)
    return Task(id, priority, arrival_time, deadline)

# generates timestamps for arrival time
def generate_arrival_time():
    return time.time()

# generates timestamp for deadline which is 1 hour later
def generate_deadline():
    return time.time() + 3600

if __name__ == "__main__":
    part_2_analysis()