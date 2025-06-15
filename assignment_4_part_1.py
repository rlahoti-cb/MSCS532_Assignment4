import random
import time

def heapify(inp, n, i):
    maximum = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and inp[left] > inp[maximum]:
        maximum = left

    if right < n and inp[right] > inp[maximum]:
        maximum = right
    
    if maximum != i:
        inp[i], inp[maximum] = inp[maximum], inp[i]
        heapify(inp, n, maximum)

def heapsort(inp):
    n = len(inp)

    for x in range(n // 2-1, -1, -1):
        heapify(inp, n, x)
    
    for x in range(n - 1, 0, -1):
        inp[0], inp[x] = inp[x], inp[0]
        heapify(inp, x, 0)

# generate random data based on set input size
def generate_random_data(size):
    out = [random.randint(0, size) for x in range(size)]
    return out

# generate sorted data based on set input size
def generate_sorted_data(size):
    out = list(range(size))
    return out

# generate reversed sorted data based on set input size
def generate_reversed_sorted_data(size):
    out = list(range(size, 0, -1))
    return out

def part_1_analysis():
    for size in (10000, 100000, 1000000):
        random_data = generate_random_data(size)
        sorted_data = generate_sorted_data(size)
        reversed_sorted_data = generate_reversed_sorted_data(size)

        start_time = time.time()
        heapsort(random_data)
        end_time = time.time()
        print("Applying heapsort to " + str(size) + " random elements took " + str(end_time - start_time) + "\n")

        start_time = time.time()
        heapsort(sorted_data)
        end_time = time.time()
        print("Applying heapsort to " + str(size) + " sorted elements took " + str(end_time - start_time) + "\n")

        start_time = time.time()
        heapsort(sorted_data)
        end_time = time.time()
        print("Applying heapsort to " + str(size) + " reversed sorted elements took " + str(end_time - start_time) + "\n")

if __name__ == "__main__":
    part_1_analysis()
