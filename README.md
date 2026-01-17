# BPhO-Computational-Physics-Challenge-2023
## Solar System Dynamics & Simulations
### Developed by Anton Lewis and Yash Joshi

An interactive Python application built with **Kivy** and **Matplotlib** to simulate and analyze the orbital mechanics of our solar system. This project explores planetary motion through numerical integration, geometric visualizations, and data-driven proofs.

## 🌌 Project Overview
This project provides a graphical user interface (GUI) to interact with seven distinct computational physics tasks. Using real-world planetary data (semi-major axes, eccentricity, orbital periods, and inclinations), the simulation models the movement of the planets and Pluto.

## 📺 Project Demo Video

Watch the full walkthrough of the application and the physics behind each task:

[![BPhO Computational Physics Challenge 2023 Demo](https://img.youtube.com/vi/-qhC-RXS28Q/0.jpg)](https://www.youtube.com/watch?v=-qhC-RXS28Q)

> Click the image above to watch the demo on YouTube.

## 🛠 Features & Tasks

* **Task 1: Kepler’s Third Law Proof**
    * Verifies the relationship $T^2 \propto r^3$ using linear regression.
    * Plots orbital period ($T$) against semi-major axis ($r^{1.5}$) to demonstrate a perfect gradient of 1.00.
* **Task 2: 2D Static Elliptical Orbits**
    * Generates static plots of the inner and outer planets using the polar equation for an ellipse.
* **Task 3 & 4: 2D & 3D Orbital Animations**
    * Real-time animations of the planets. Task 4 specifically incorporates **orbital inclination** to show the 3D tilt of planetary planes.
* **Task 5: Orbital Angle vs. Time (Simpson's Integration)**
    * Solves the non-trivial relationship between time and polar angle for eccentric orbits.
    * Uses **Simpson’s Rule** to numerically integrate the equations of motion for Pluto.
* **Task 6: Planetary Spirographs**
    * An interactive tool where users select two planets to trace their relative positions over time, creating complex geometric patterns.
* **Task 7: Relative Motion Simulator**
    * Allows the user to shift the frame of reference to any planet (e.g., a Saturn-centric view), simulating how the rest of the solar system moves relative to that body in 3D.

## 🚀 Technical Stack
* **Language:** Python 3.x
* **GUI:** [Kivy](https://kivy.org/)
* **Plotting:** [Matplotlib](https://matplotlib.org/)
* **Numerical Processing:** NumPy and Pandas
* **Custom Backend:** `backend_kivyagg.py` is utilized to render Matplotlib figures as native Kivy widgets.

## 📂 File Structure
* `main.py`: The entry point for the Kivy application and main menu logic.
* `task1.py` to `task7.py`: Individual modules containing the logic and plotting for each task.
* `planets.xlsx`: The source dataset containing planetary constants (Semi-major axis `r`, Eccentricity `Epsilon`, Period `T`, and `Inclination`).
* `backend_kivyagg.py`: Handles the integration of Matplotlib plots into the Kivy UI.

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yash-joshi5379/BPhO-Computational-Physics-Challenge-2023.git
   cd BPhO-Computational-Physics-Challenge-2023
   ```

2.  **Install Dependencies:**
    The project relies on `Kivy` for the interface and `Matplotlib` for physics visualizations. Install all required packages using pip:
    ```bash
    pip install kivy matplotlib numpy pandas scipy openpyxl
    ```

3.  **Data Source:**
    Ensure the file `planets.xlsx` is located in the root directory. This file contains the orbital parameters (r, Epsilon, T, and Inclination) necessary for the simulations.

##  🪐 Usage

1.  **Launch the Application:**
    Run the main script to open the interactive GUI:
    ```bash
    python main.py
    ```

2.  **Navigate the Dashboard:**
    Upon launching, you will see a main menu with buttons for **Task 1 through Task 7**. 
    
    * **Keplerian Proofs:** Click Task 1 to see the linear regression proving the $T^2 \propto r^3$ relationship.
    * **Orbit Visualisations:** Click Task 2 to see the static orbital paths of the inner or outer planets.
    * **2D/3D Simulations:** Select Tasks 3 or 4 to view real-time animated orbits.
    * **Numerical Integration:** View Task 5 to see how **Simpson's Rule** is applied to Pluto's eccentric orbit.

3.  **Interactive Exploration:**
    * In **Task 6 (Spirographs)**, you can select two different planets to generate unique geometric patterns based on their relative orbital periods.
    * In **Task 7 (Relative Motion)**, you can change the reference frame to see the solar system move relative to Earth or other planets in 3D.

4.  **Exiting:**
    Use the "Go Back" buttons within each task to return to the main menu, or simply close the window to exit the simulation.
