# Part C - Interview Ready (PM Session)

# Q1: Difference between PMF and PDF?
"""
- Probability Mass Function (PMF): Used for discrete random variables (countable outcomes 
  like a coin toss or dice roll). It gives the probability that a variable is exactly 
  equal to a specific value.
- Probability Density Function (PDF): Used for continuous random variables (uncountable 
  outcomes like height or time). It doesn't give the probability of a specific point 
  (which is 0), but the density. Probability is found by calculating the area under 
  the curve for a range of values.
"""

# Q2: Compute probability from frequency data
def compute_relative_frequency(data):
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    
    total = len(data)
    probs = {key: val/total for key, val in counts.items()}
    return probs

# Example
sample_data = ['Red', 'Blue', 'Red', 'Green', 'Red', 'Blue']
print("Event Probabilities (Relative Frequency):")
print(compute_relative_frequency(sample_data))

# Q3: What is the Central Limit Theorem (CLT)?
"""
The CLT states that if you take enough samples from any distribution (regardless of its shape), 
the means of those samples will follow a Normal Distribution as the sample size increases.

Importance in Machine Learning:
1. Foundation for Confidence Intervals and Hypothesis Testing.
2. Explains why many real-world errors/noises follow a normal distribution.
3. Allows us to make inferences about a population mean even when the population distribution 
   is unknown or non-normal.
"""
