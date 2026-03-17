# Part B - Stretch Problem: Basic Hypothesis Testing

def compute_mean(data):
    return sum(data) / len(data)

def compute_variance(data):
    m = compute_mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)  # Using n-1 for sample variance

def two_sample_t_test(sample1, sample2):
    # 1. Compute mean and variance
    m1, m2 = compute_mean(sample1), compute_mean(sample2)
    v1, v2 = compute_variance(sample1), compute_variance(sample2)
    n1, n2 = len(sample1), len(sample2)
    
    # 2. Calculate t-statistic (Simplified formula for independent samples)
    # denominator = sqrt( (var1/n1) + (var2/n2) )
    denominator = ((v1 / n1) + (v2 / n2)) ** 0.5
    t_stat = (m1 - m2) / denominator
    
    # 3. Interpret result
    # For a beginner, we compare t_stat with a common critical value (e.g., ~2.0 for 95% confidence)
    # or just report the stats.
    alpha = 0.05
    # Simplified: if |t| > 2, it's usually significant for small samples
    is_different = abs(t_stat) > 2.0 
    
    return {
        "Mean 1": round(m1, 2),
        "Mean 2": round(m2, 2),
        "T-Statistic": round(t_stat, 4),
        "Significant Difference": is_different
    }

# Synthetic Dataset
# Group A: Students who studied 10+ hours
# Group B: Students who studied <2 hours
group_high = [80, 85, 88, 75, 92, 90, 84]
group_low = [50, 60, 55, 65, 58, 62, 45]

result = two_sample_t_test(group_high, group_low)

print("Hypothesis Testing Results:")
for key, value in result.items():
    print(f"{key}: {value}")

if result["Significant Difference"]:
    print("\nConclusion: The groups are significantly different.")
else:
    print("\nConclusion: There is no significant difference.")
