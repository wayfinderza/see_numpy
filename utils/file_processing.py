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
        
        if array.ndim == 1:  # Process only 1D arrays for now
            parsed_data = parse_1d_array(array)
        else:
            parsed_data = {"Data": array.tolist()}  # Keep other arrays in list format for now
        
        arrays[key] = {
            "Basic Information": {
                "ndim": array.ndim,
                "shape": array.shape,
                "dtype": str(array.dtype),
            },
            "Parsed Data": parsed_data,
        }
    
    return arrays

def parse_1d_array(array):
    """
    Converts a 1D NumPy array into the required dictionary format with aggregations.
    
    Args:
        array (np.ndarray): 1D NumPy array.
    
    Returns:
        dict: A dictionary with indexed data and aggregated statistics.
    """
    parsed_dict = {}
    
    # Store individual elements
    for i in range(array.shape[0]):
        parsed_dict[(i,)] = [str(array[i]), str(array[i]), '1']
    
    # Store aggregated values
    total_sum = array.sum()
    total_count = array.size
    total_avg = total_sum / total_count
    parsed_dict[()] = [str(total_sum), str(total_avg), str(total_count)]
    
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
