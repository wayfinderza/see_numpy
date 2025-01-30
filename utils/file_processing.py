import numpy as np

def load_npz_file(file_path):
    """
    Load an NPZ file and extract arrays with structured data and aggregation.
    
    Args:
        file_path (str): Path to the NPZ file.

    Returns:
        dict: A dictionary containing structured data for each array.
    """
    data = np.load(file_path)
    arrays = {}
    
    for key in data.keys():
        array = data[key]

        if array.ndim > 3:
            parsed_data = {"Error": "Only arrays with up to 3 dimensions are supported."}
        else:
            parsed_data = parse_nd_array(array, ())

        arrays[key] = {
            "Basic Information": {
                "ndim": array.ndim,
                "shape": array.shape,
                "dtype": str(array.dtype),
            },
            "Parsed Data": parsed_data,
        }
    
    return arrays

def parse_nd_array(array, index):
    """
    Recursively parses an N-dimensional NumPy array into a structured dictionary format with aggregation.
    
    Args:
        array (np.ndarray): N-dimensional NumPy array.
        index (tuple): Current index in the recursion.

    Returns:
        dict: A dictionary mapping indices to values and aggregations.
    """
    parsed_dict = {}

    if array.ndim == 0:  # Base case: scalar value
        parsed_dict[index] = [str(array.item()), str(array.item()), '1']
        return parsed_dict

    # Compute aggregation for this level
    total_sum = array.sum()
    total_count = array.size
    total_avg = total_sum / total_count
    parsed_dict[index] = [str(total_sum), str(total_avg), str(total_count)]

    # Iterate over first dimension
    for i in range(array.shape[0]):
        sub_index = index + (i,)
        parsed_dict.update(parse_nd_array(array[i], sub_index))

    return parsed_dict

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
