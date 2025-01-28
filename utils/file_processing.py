import numpy as np

def load_npz_file(file_path):
    """
    Load an NPZ file and extract arrays with their dimensions and data.
    
    Args:
        file_path (str): Path to the NPZ file.

    Returns:
        dict: A dictionary containing the array details.
    """
    data = np.load(file_path)
    arrays = {
        key: {
            "dimensions": data[key].shape,
            "data": data[key].tolist()  # Convert to Python list for JSON compatibility
        }
        for key in data.keys()
    }
    return arrays
