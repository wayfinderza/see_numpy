import numpy as np

def main():
    # Create a 4 x 5 x 3 array of floats with dtype float32
    float_array = np.random.rand(4, 5, 3).astype(np.float32)
    
    # Create a 5 x 5 x 5 array of complex numbers with integer real and imaginary parts
    real_part = np.random.randint(-100, 100, (5, 5, 5), dtype=np.int32)  # Random integers between -100 and 100
    imag_part = np.random.randint(-100, 100, (5, 5, 5), dtype=np.int32)  # Same range for imaginary part
    complex_array = real_part + 1j * imag_part  # Combine into complex numbers
    
    # Save the float array to Sample1.npz
    np.savez("sample1.npz", array=float_array)
    
    # Save the complex array to Sample2.npz
    np.savez("sample2.npz", array=complex_array)
    
    print("Files Sample1.npz and Sample2.npz have been created.")

if __name__ == "__main__":
    main()
