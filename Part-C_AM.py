# Part C - Interview Ready

# Q1: Difference between loops, list comprehension, and higher-order functions
"""
- Loops: Provide full control over the iteration process. Used for complex logic where 
  multiple operations or side effects (like printing) are needed inside the loop.
- List Comprehension: A concise, readable way to create new lists based on existing ones. 
  Best used for simple filtering and transformation.
- Higher-Order Functions (HOF): Functions like map() and filter() that take other functions 
  as arguments. Useful for functional programming styles and when reusing logic.
"""

# Q2: Implement function to flatten a nested list and remove even numbers
def flatten_and_remove_evens(nested_list):

    return [item for sublist in nested_list for item in sublist if item % 2 != 0]

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = flatten_and_remove_evens(nested)
print("Flattened & Odd Numbers Only:", result)

# Q3: Question Explanations
"""
Hypothesis Testing: A statistical method used to decide whether the data supports 
a particular hypothesis or if result occurs by chance.

1. Null Hypothesis (H0): The default assumption that there is no effect or no difference.
   Example: "A new drug has no effect on blood pressure compared to a placebo."
   
2. P-Value: The probability of obtaining the test results at least as extreme as the 
   ones observed, assuming the null hypothesis is true. A low p-value (usually < 0.05) 
   suggests H0 might be wrong.

3. Significance Level (Alpha): The threshold set before the test (usually 0.05). 
   If p-value < Alpha, we reject the null hypothesis.
"""
