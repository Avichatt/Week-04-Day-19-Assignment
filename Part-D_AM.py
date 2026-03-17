# Part D - AI-Augmented Task

# 1. Prompt Documentation
prompt = "Explain descriptive statistics and hypothesis testing with a Python example using real-world data."

# 2. Simulated AI Output
ai_output = """
Descriptive statistics summarize the main features of a dataset (Mean, Median, Std Dev), 
while Hypothesis Testing helps us make inferences about a population based on sample data.

Example using 'Miles Per Gallon' (MPG) data:
Suppose we compare MPG of cars from USA vs Japan.

H0: No difference in average MPG between USA and Japan.
H1: Significant difference in MPG.

```python
import pandas as pd
import scipy.stats as stats

# Hypothetical data
usa_mpg = [18, 21, 22, 19, 20, 18, 17, 21]
japan_mpg = [30, 32, 35, 31, 29, 33, 34, 30]

# Descriptive Stats
print(f"USA Mean: {sum(usa_mpg)/len(usa_mpg)}")
print(f"Japan Mean: {sum(japan_mpg)/len(japan_mpg)}")

# T-Test (Hypothesis Testing)
t_stat, p_val = stats.ttest_ind(usa_mpg, japan_mpg)
print(f"P-Value: {p_val}")

if p_val < 0.05:
    print("Reject Null Hypothesis: Significant difference found.")
```
"""

# 3. Evaluation
evaluation = """
Evaluation:
- Is the explanation clear and correct? Yes, it clearly distinguishes between summarizing 
  data and making inferences. The definitions of H0 and H1 are accurate.
- Is the code logically structured and runnable? Yes, it uses a standard library (scipy) 
  for the t-test and basic arithmetic for descriptive stats. The logic follows the 
  standard hypothesis testing workflow.
"""

print("--- PROMPT ---")
print(prompt)
print("\n--- AI OUTPUT ---")
print(ai_output)
print("\n--- EVALUATION ---")
print(evaluation)
