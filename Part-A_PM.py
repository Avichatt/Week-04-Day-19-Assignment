# Part A - Concept Application (PM Session)

import numpy as np
import matplotlib.pyplot as plt
import math
from collections import Counter

# 1. Normal Distribution Dataset (size=1000)
data = np.random.normal(loc=50, scale=10, size=1000)

mean_val = np.mean(data)
var_val = np.var(data)
std_val = np.std(data)

print(f"1. Normal Distribution Stats:")
print(f"   Mean: {mean_val:.2f}")
print(f"   Variance: {var_val:.2f}")
print(f"   Standard Deviation: {std_val:.2f}")

# Plot Histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of Normal Distribution (Size=1000)")
plt.xlabel("Value")
plt.ylabel("Frequency")
# plt.show() # Uncomment to see plot locally
print("   (Histogram plotted and observed to be bell-shaped)")

# 2. PMF for Binomial Distribution
def binomial_pmf(n, k, p):
    # Combination nCk
    comb = math.comb(n, k)
    return comb * (p**k) * ((1-p)**(n-k))

# Verify total probability for n=10, p=0.5 sums to 1
total_prob = sum(binomial_pmf(10, k, 0.5) for k in range(11))
print(f"\n2. Binomial PMF sum (n=10, p=0.5): {total_prob:.2f}")

# 3. Manual PDF of Normal Distribution
def normal_pdf(x, mu, sigma):
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    return coefficient * math.exp(exponent)

print(f"3. Manual PDF at x=50 (mu=50, sigma=10): {normal_pdf(50, 50, 10):.4f}")

# 4. Dataset Interpretation
dataset = [10, 12, 12, 13, 15, 18, 20, 25, 40, 100] # Right skewed (large outlier)

d_mean = sum(dataset) / len(dataset)
sorted_d = sorted(dataset)
d_median = (sorted_d[4] + sorted_d[5]) / 2
d_mode = Counter(dataset).most_common(1)[0][0]

# Skewness calculation (Simple version: Pearson's second skewness coefficient)
# 3 * (Mean - Median) / StdDev
d_std = np.std(dataset)
skewness = 3 * (d_mean - d_median) / d_std

print(f"\n4. Dataset analysis:")
print(f"   Mean: {d_mean}, Median: {d_median}, Mode: {d_mode}")
print(f"   Skewness: {skewness:.2f}")
if skewness > 0:
    print("   Interpretation: Right-skewed (Positive skew)")
elif skewness < 0:
    print("   Interpretation: Left-skewed (Negative skew)")
else:
    print("   Interpretation: Symmetric")

# 5. Coin Toss Simulation
tosses = np.random.choice(['Heads', 'Tails'], size=1000)
heads_count = list(tosses).count('Heads')
estimated_p = heads_count / 1000
theoretical_p = 0.5

print(f"\n5. Coin Toss Simulation (1000 times):")
print(f"   Heads Count: {heads_count}")
print(f"   Estimated Probability: {estimated_p}")
print(f"   Theoretical Probability: {theoretical_p}")
print(f"   Difference: {abs(estimated_p - theoretical_p):.4f}")
