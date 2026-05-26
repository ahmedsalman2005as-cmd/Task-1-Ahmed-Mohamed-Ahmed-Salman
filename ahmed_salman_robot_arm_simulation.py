# Author: Ahmed Salman
import math
import random
import matplotlib.pyplot as plt

# Function to simulate a robot arm movement
def move_arm(angle, distance):
    # Calculate new position based on angle and distance
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    return x, y

def read_sensor():
    
    return random.uniform(5, 20)

# Main function
def main():
    print("=== Robotics Project 1 Simulation ===\n")
    print("Developer: Ahmed Salman\n")

    angles = list(range(0, 181, 30))  
    x_positions = []
    y_positions = []

    for angle in angles:
        distance = read_sensor()
        position = move_arm(angle, distance)
        x_positions.append(position[0])
        y_positions.append(position[1])
        print(f"Moving arm to {angle}° - Sensor reads {distance:.2f} - Position: {position}")

    print("\nSimulation finished!")

    # Plot the arm positions
    plt.figure(figsize=(6,6))
    plt.plot(x_positions, y_positions, marker='o', linestyle='-', color='blue')
    for i, angle in enumerate(angles):
        plt.text(x_positions[i], y_positions[i], f"{angle}°", fontsize=9)
    plt.title("Robot Arm Movement Simulation - Ahmed Salman")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()