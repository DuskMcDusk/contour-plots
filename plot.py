
from matplotlib import pyplot as plt
import numpy as np

# measurments is a dictionary {}
def plotMeasurementsTemperature(measurements):
    # Extract angles and temperatures
    
    angles = np.array(measurements[0]["angles"])  # Assuming all measurements have the same angles
    temperatures = np.array([m["temperature"] for m in measurements])
    # Create a 2D grid of intensity values
    intensity_grid = np.array([m["intensities"] for m in measurements])
    # Create the contour plot
    plt.figure(figsize=(8, 6))
    X, Y = np.meshgrid(angles, temperatures)  # Create a grid of angles and temperatures
    plt.ylabel("Temperature (°C)")


    levels = np.linspace(np.min(intensity_grid), np.max(intensity_grid), 20)
    contour = plt.contourf(X, Y, intensity_grid, levels=levels, cmap="jet")  # Filled contour plot

    # Add a colorbar
    cbar = plt.colorbar(contour)
    cbar.set_label("Intensity")

    # Add labels and title
    plt.xlabel("Angle (degrees)")
    
    plt.title("Contour Plot of XRD Measurements")

    plt.savefig("plot.png")