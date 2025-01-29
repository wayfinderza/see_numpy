import numpy as np

def load_npz_file(file_path):
    """
    Load an NPZ file and extract arrays with their basic information and data.
    
    Args:
        file_path (str): Path to the NPZ file.

    Returns:
        dict: A dictionary containing basic information and data for each array.
    """
    data = np.load(file_path)
    arrays = {
        key: {
            "Basic Information": {
                "ndim": data[key].ndim,
                "shape": data[key].shape,
                "dtype": str(data[key].dtype),
            },
            "Data": data[key].tolist()  # Convert to Python list for JSON compatibility
        }
        for key in data.keys()
    }
    return arrays

def validate_npz_file(file_path):
    """
    Validates that the .npz file contains only numeric NumPy arrays with at most 3 dimensions.

    Returns:
        (bool, str): A tuple where the first value is True if valid, False otherwise,
                     and the second value is an error message if invalid.
    """
    try:
        with np.load(file_path, allow_pickle=False) as data:
            for key in data.files:
                array = data[key]

                # Check if it's actually a NumPy array
                if not isinstance(array, np.ndarray):
                    return False, f"Error: '{key}' is not a valid NumPy array. Found type: {type(array)}."

                # Check if the data type is numeric
                if not np.issubdtype(array.dtype, np.number):
                    return False, f"Error: '{key}' contains non-numeric data. Detected dtype: {array.dtype}."

                # Check if the number of dimensions is within the limit
                if array.ndim > 3:
                    return False, f"Error: '{key}' has more than 3 dimensions ({array.ndim})."

        return True, "Valid"
    except Exception as e:
        return False, f"Error processing NPZ file: {e}"