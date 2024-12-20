import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=248, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(arr):
    return len(arr) == len(set(arr))

def measure_time(func, arr):
    start_time = time.perf_counter()
    result = func(arr)
    exec_time = (time.perf_counter() - start_time) * 1e6
    return exec_time, result

n_values = [100, 150, 200, 250, 300, 350, 400, 500]

worst_case_times = []
average_case_times = []

for n in n_values:
    total_time = 0
    worst_time = 0

    for _ in range(10):
        array = generate_array(n)
        exec_time, is_unique_result = measure_time(is_unique, array)

        total_time += exec_time
        worst_time = max(worst_time, exec_time)

    average_case_times.append(total_time / 10)
    worst_case_times.append(worst_time)

with open("worst_avg.txt", "w", encoding="utf-8") as file:
    file.write("Array Size (n), Worst Case (μs), Average Case (μs), Unique\n")
    for n in n_values:
        array = generate_array(n)
        _, is_unique_result = measure_time(is_unique, array)
        unique_status = "Yes" if is_unique_result else "No"
        file.write(f"{n}, {worst_case_times[n_values.index(n)]:.2f}, {average_case_times[n_values.index(n)]:.2f}, {unique_status}\n")

print("n_values:", n_values)
print("worst_case_times:", worst_case_times)
print("average_case_times:", average_case_times)

plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label='Worst Case', marker='o', color='red')
plt.plot(n_values, average_case_times, label='Average Case', marker='s', color='blue')
plt.title('Execution Time: Worst Case vs Average Case', fontsize=14)
plt.xlabel('Array Size (n)', fontsize=12)
plt.ylabel('Time (microseconds)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.savefig("worst_avg_plot.pdf")
plt.show()