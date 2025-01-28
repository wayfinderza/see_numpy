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
