import os
import numpy as np

# Parameters for file location and name
data_location = 'data/'
file_name = 'example_arrays'

# Ensure the directory exists
os.makedirs(data_location, exist_ok=True)

# Create the sample arrays
arrays = {
    # arr1: A 1D array of integers with 5 elements.
    "arr1": np.array([1, 2, 3, 4, 5], dtype=np.int32),

    # arr2: A 1D array of floats with 4 elements.
    "arr2": np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64),

    # arr3: A 1D array of strings with 3 elements.
    "arr3": np.array(['apple', 'banana', 'cherry'], dtype=np.str_),

    # arr13: A 2D array of integers, 5 rows and 6 columns.
    "arr13": np.arange(30).reshape(5, 6).astype(np.int32),

    # arr4: A 2D array of integers, 2 rows and 3 columns.
    "arr4": np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64),

    # arr6: A 2D boolean array, 2 rows and 2 columns.
    "arr6": np.array([[True, False], [False, True]], dtype=np.bool_),

    # arr7: A 3D array of integers, 2x2x2 structure.
    "arr7": np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.int16),

    # arr8: A 3D array of random floats, dimensions 3x4x2.
    "arr8": np.random.random((3, 4, 2)).astype(np.float32),

    # arr9: A 4D array of zeros, dimensions 2x3x4x5.
    "arr9": np.zeros((2, 3, 4, 5), dtype=np.float64),

    # arr10: A 5D array of ones, dimensions 1x2x3x4x5.
    "arr10": np.ones((1, 2, 3, 4, 5), dtype=np.int8),

    # arr12: A structured array with two elements, each having fields: id (integer), name (string), and score (float).
    "arr12": np.array(
        [(1, 'Alice', 25.5), (2, 'Bob', 30.8)],
        dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'f4')]
    ),

    # arr5: A 2D array of complex numbers, dimensions 2x2.
    "arr5": np.array([[1+2j, 2+3j], [3+4j, 4+5j]], dtype=np.complex128),

    # arr14: A 2D array of random floats, dimensions 1000x1000 (1 million elements).
    "arr14": np.random.rand(1000, 1000).astype(np.float64),

    # arr15: A 1D object array containing two arrays of different sizes.
    "arr15": np.array([np.arange(3), np.arange(5)], dtype=object)
}

# Save each array into its own .npz file
for name, array in arrays.items():
    file_path = os.path.join(data_location, f"{name}.npz")
    np.savez(file_path, array=array)
    print(f"{name} saved to {file_path}")
    print(f"{name}: shape = {array.shape}, dtype = {array.dtype}")
