# Part D - AI-Augmented Task (PM Session)

# 1. Prompt Documentation
prompt = "Explain probability distributions (normal, uniform, binomial) with Python visualizations."

# 2. Captured AI Output
ai_output = """
Probability distributions help us understand how data is spread.

1. Normal Distribution (Continuous):
Bell curve used for things like weight or height.
```python
import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30)
```

2. Uniform Distribution (Continuous/Discrete):
Flat shape where all values are equally likely.
```python
data = np.random.uniform(0, 10, 1000)
plt.hist(data, bins=30)
```

3. Binomial Distribution (Discrete):
Models number of successes in fixed trials (like coins).
```python
data = np.random.binomial(n=10, p=0.5, size=1000)
plt.hist(data, bins=11)
```
"""

# 3. Evaluation
evaluation = """
Evaluation:
- Are the explanations correct? Yes, they provide simple but accurate context for each.
- Are the visualizations meaningful? Yes, the histograms effectively show the shape 
  distinctions (bell vs flat vs discrete steps). The code snippets provided are 
  runnable and correctly demonstrate the distributions.
"""

print("--- PROMPT ---")
print(prompt)
print("\n--- AI OUTPUT ---")
print(ai_output)
print("\n--- EVALUATION ---")
print(evaluation)
