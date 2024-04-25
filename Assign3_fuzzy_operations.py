
import numpy as np

# Fuzzy Set Operations
def fuzzy_union(A, B):
    return np.maximum(A, B)

def fuzzy_intersection(A, B):
    return np.minimum(A, B)

def fuzzy_complement(A):
    return 1 - A

def fuzzy_difference(A, B):
    return np.maximum(A, 1 - B)

# Fuzzy Relation Operations
def cartesian_product(A, B):
    return np.outer(A, B)

def max_min_composition(R1, R2):
    return np.maximum.reduce([np.minimum.outer(row_R1, col_R2) for row_R1 in R1 for col_R2 in R2])

# Example usage
A = np.array([0.2, 0.4, 0.6, 0.8])
B = np.array([0.1, 0.3, 0.5, 0.7])

# Fuzzy Set Operations
union_result = fuzzy_union(A, B)
intersection_result = fuzzy_intersection(A, B)
complement_A = fuzzy_complement(A)
difference_result = fuzzy_difference(A, B)

print("Fuzzy Set Operations:")
print("Union:", union_result)
print("Intersection:", intersection_result)
print("Complement of A:", complement_A)
print("Difference (A - B):", difference_result)

# Fuzzy Relation Operations
R1 = np.array([[0.2, 0.4], [0.6, 0.8]])
R2 = np.array([[0.1, 0.3], [0.5, 0.7]])

cartesian_product_result = cartesian_product(A, B)
max_min_composition_result = max_min_composition(R1, R2)

print("\nFuzzy Relation Operations:")
print("Cartesian Product:")
print(cartesian_product_result)
print("\nMax-Min Composition:")
print(max_min_composition_result)
