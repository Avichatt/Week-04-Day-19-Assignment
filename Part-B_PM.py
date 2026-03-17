# Part B - Stretch Problem (PM Session)

import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Distributions
normal_data = np.random.normal(50, 10, 1000)
uniform_data = np.random.uniform(20, 80, 1000)

# 2. Plotting Comparison
plt.figure(figsize=(12, 5))

# Plot Normal
plt.subplot(1, 2, 1)
plt.hist(normal_data, bins=30, alpha=0.7, color='blue', label='Normal')
plt.title("Normal Distribution (Bell Shape)")
plt.axvline(np.mean(normal_data), color='red', linestyle='dashed', linewidth=1, label='Mean')

# Plot Uniform
plt.subplot(1, 2, 2)
plt.hist(uniform_data, bins=30, alpha=0.7, color='green', label='Uniform')
plt.title("Uniform Distribution (Flat Shape)")
plt.axvline(np.mean(uniform_data), color='red', linestyle='dashed', linewidth=1, label='Mean')

# plt.show() # Uncomment to see plot

# Comparison Logic
print("Distribution Comparison:")
print("-" * 30)
print(f"Normal:  Mean={np.mean(normal_data):.2f}, Std={np.std(normal_data):.2f}")
print(f"Uniform: Mean={np.mean(uniform_data):.2f}, Std={np.std(uniform_data):.2f}")

"""
3. Explanations:

Shape:
- Normal: Bell-shaped, symmetric around the mean. Most values cluster in the center.
- Uniform: Flat/Rectangular shape. Every value in the range is equally likely to occur.

Spread:
- Normal: Concentrated around the center; tails fade out.
- Uniform: Spread evenly across the entire range from minimum to maximum.

Central Tendency:
- Both have a clear mean, but the mean of a Normal distribution represents the most 
  probable outcome, whereas in a Uniform distribution, the mean is just the midpoint 
  of equally likely outcomes.

Real-World Uses:
- Normal Distribution: Used for natural phenomena like heights, IQ scores, or 
  measurement errors in physics.
- Uniform Distribution: Used for scenarios where every outcome is equally likely, 
  like picking a random number between 1 and 100, or arrival times in some queueing models.
"""
