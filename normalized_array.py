import numpy as np

def normalize_array(input_array):
    arr = np.asarray(input_array)
   
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.zeros_like(arr, dtype=float)

    normalized = (arr - min_val) / (max_val - min_val)

    return normalized
    
if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
