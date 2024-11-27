import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
N = 12  # Number of robots
SPEED = 0.5  # Maximum robot speed
ARENA_BOUNDS = [-1.6, 1.6, -1, 1]  # [xmin, xmax, ymin, ymax]
TIME_STEP = 0.1  # Time step in seconds
SIMULATION_DURATION = 1000  # Total simulation time in seconds
NUM_STEPS = int(SIMULATION_DURATION / TIME_STEP)

# Initialize robot positions and velocities
positions = np.random.uniform([ARENA_BOUNDS[0], ARENA_BOUNDS[2]], 
                               [ARENA_BOUNDS[1], ARENA_BOUNDS[3]], 
                               (N, 2))
velocities = np.random.uniform(-SPEED, SPEED, (N, 2))

# Visualization setup
plt.figure(figsize=(8, 6))
plt.xlim(ARENA_BOUNDS[:2])
plt.ylim(ARENA_BOUNDS[2:])
plt.title("Robot Movements Simulation")
plt.xlabel("X Position")
plt.ylabel("Y Position")

# Simulation loop
for step in range(NUM_STEPS):
    plt.clf()
    plt.xlim(ARENA_BOUNDS[:2])
    plt.ylim(ARENA_BOUNDS[2:])
    plt.title(f"Step {step + 1}/{NUM_STEPS}")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    # Update positions and handle boundaries
    for i in range(N):
        positions[i] += velocities[i] * TIME_STEP

        # Check for boundary collisions and reverse velocity if needed
        if positions[i, 0] <= ARENA_BOUNDS[0] or positions[i, 0] >= ARENA_BOUNDS[1]:
            velocities[i, 0] *= -1  # Reverse x-velocity
        if positions[i, 1] <= ARENA_BOUNDS[2] or positions[i, 1] >= ARENA_BOUNDS[3]:
            velocities[i, 1] *= -1  # Reverse y-velocity

    # Plot robot positions
    plt.scatter(positions[:, 0], positions[:, 1], c='blue', label="Robots")
    plt.legend()
    plt.pause(0.01)

plt.show()