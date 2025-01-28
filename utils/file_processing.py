import numpy as np

def extract_array_info(array):
    return {
        "ndim": array.ndim,
        "shape": array.shape,
        "dtype": str(array.dtype),
    }

def convert_array_data(array):
    return array.tolist()

def load_npz_file(file_path):
    data = np.load(file_path)
    arrays = {
        key: {
            "Basic Information": extract_array_info(data[key]),
            "Data": convert_array_data(data[key])
        }
        for key in data.keys()
    }
    return arrays
