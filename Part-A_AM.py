# Part A - Concept Application

import numpy as np
from functools import reduce

# 1. Using loops to compute Men, Median, Variance
def mean_loops(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def median_loops(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

def variance_loops(numbers):
    m = mean_loops(numbers)
    sum_sq_diff = 0
    for num in numbers:
        sum_sq_diff += (num - m) ** 2
    return sum_sq_diff / len(numbers)

# 2. Using Higher-Order Funcions (map, filter, reduce)
def mean_hof(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

def variance_hof(numbers):
    m = mean_hof(numbers)
    # Using map to get squareddifferences
    sq_diffs = list(map(lambda x: (x - m) ** 2, numbers))
    # Using reduce tosum them
    return reduce(lambda x, y: x + y, sq_diffs) / len(numbers)



# 3. Student Marks Dtaset
marks = [85, 92, 78, 90, 65, 88, 72, 95, 40, 55]


avg_mark = mean_loops(marks)
above_avg = [m for m in marks if m > avg_mark]


grades = ["A" if m > 85 else "B" if m >= 70 else "C" for m in marks]

print("Marks:", marks)
print("Above Average:", above_avg)
print("Grades:", grades)

# 4. Standard Deviation Function + NuPy Verification
def std_dev(numbers):
    var = variance_loops(numbers)
    return var ** 0.5

test_data = [10, 20, 30, 40, 50]
my_std = std_dev(test_data)
numpy_std = np.std(test_data)

print(f"\nCustom SD: {my_std}")
print(f"NumPy SD: {numpy_std}")
print(f"Match: {round(my_std, 5) == round(numpy_std, 5)}")

# 5. Two groups Mean ad Variance
A = [12, 23, 3, 34, 45, 56, 5]
B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

mean_A, var_A = mean_loops(A), variance_loops(A)
mean_B, var_B = mean_loops(B), variance_loops(B)

print(f"\nGroup A: Mean={mean_A:.2f}, Variance={var_A:.2f}")
print(f"Group B: Mean={mean_B:.2f}, Variance={var_B:.2f}")
print(f"Difference in Means: {abs(mean_A - mean_B):.2f}")
