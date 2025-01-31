# SeeNumPy - Flexible Array Visualizer  

## Overview  
SeeNumPy is a **Flask-based web application** designed to offer **flexible and intuitive visualisations** for **multi-dimensional NumPy arrays**. This project focuses on providing users with a variety of tools and options to explore, customise, and analyse their data interactively. Whether you're working with simple 2D arrays or more complex 3D structures, SeeNumPy enables seamless exploration through a **highly interactive UI**.

Flask tutorial used: [Web Development with Python Tutorial – Flask & Dynamic Database-Driven Web Apps](https://youtu.be/yBDHkveJUf4?si=UgpIEPk7U34Z6kGq)


## Features  

- **Upload & Validate `.npz` Files**  
  - Supports **multiple arrays** within a single `.npz` file.  
  - Ensures all arrays are numeric and meet visualisation requirements.  

- **Dynamic & Flexible Visualisations**  
  - **Array-Like Display**: Intuitively explore arrays with structured expansion (downward, then rightward). (TODO) 
  - **Custom Views**:  
    - Switch between **table views** and **transparent cube-like visualisations** for 3D arrays. (TODO)
    - Enable **heatmap views** to represent data visually. (TODO)
  - **User-Controlled Collapse/Aggregation**: Choose specific levels to collapse and apply aggregations like sum, mean, or custom calculations dynamically. (TODO) 

- **Aggregations & Insights**  
  - Compute and display **sum, mean, count**, and other stats at different levels.  
  - Aggregations adjust dynamically as users expand or collapse data.  

- **Reset & Start Fresh**  
  - A dedicated reset button clears the interface for a new session.  

## Installation & Setup  

### Requirements  
Ensure you have **Python 3.13** installed along with the required dependencies.  

### Steps  
1. **Clone the Repository**  
   ```powershell
   git clone <repository_url>
   cd seenumpy

2. **Create a Virtual Environment**
    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate

3. **Install Dependencies**
    ```poweshell
    pip install -r requirements.txt

4. **Run the Flask App**
    ```powershell
    python app.py

5. **Navigate to the Web App**
    - Open the web app.

## Usage
1. Upload a `.npz` file containing one or more multi-dimensional arrays.
2. Select an array to explore from the list of uploaded arrays.
3. Use the expand/collapse controls to navigate through dimensions.
4. Choose from different view modes (e.g., heatmap, cube, table).
5. Apply aggregations or custom calculations at the desired levels.
6. Reset the session to begin a new exploration.


## Roadmap & Issues
We are committed to expanding SeeNumPy's capabilities with more visualisation options and enhanced flexibility.

📌 **Track Our Progress**: [GitHub Project Board](https://github.com/users/wayfinderza/projects/1/views/1)






