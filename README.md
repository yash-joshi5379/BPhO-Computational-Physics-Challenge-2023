# BPhO-Computational-Physics-Challenge-2023
## Solar System Dynamics & Simulations
### Developed by Anton Lewis and Yash Joshi

An interactive Python application built with **Kivy** and **Matplotlib** to simulate and analyze the orbital mechanics of our solar system. This project explores planetary motion through numerical integration, geometric visualizations, and data-driven proofs.

## 🌌 Project Overview
This project provides a graphical user interface (GUI) to interact with seven distinct computational physics tasks. Using real-world planetary data (semi-major axes, eccentricity, orbital periods, and inclinations), the simulation models the movement of the planets and Pluto.

## 🛠 Features & Tasks

* **Task 1: Kepler’s Third Law Proof**
    * Verifies the relationship $P^2 \propto a^3$ using linear regression.
    * Plots orbital period ($P$) against semi-major axis ($a^{1.5}$) to demonstrate a perfect gradient of 1.00.
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
* `planets.xlsx`: The source dataset containing planetary constants (Semi-major axis `a`, Eccentricity `Epsilon`, Period `P`, and `Inclination`).
* `backend_kivyagg.py`: Handles the integration of Matplotlib plots into the Kivy UI.

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[your-username]/[your-repo-name].git
   cd [your-repo-name]
