import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
time_step = 1e7  # Time step in seconds (~116 days)
simulation_years = 1000  # Simulate for 1000 years
steps = int((simulation_years * 365.25 * 24 * 3600) / time_step)

# Jupiter and moon data (mass in kg, distance in m, velocity in m/s)
jupiter_mass = 1.898e27
moons = {
    "Io": {"mass": 8.93e22, "position": np.array([4.22e8, 0]), "velocity": np.array([0, 17.334e3])},
    "Europa": {"mass": 4.8e22, "position": np.array([6.71e8, 0]), "velocity": np.array([0, 13.74e3])},
    "Ganymede": {"mass": 1.48e23, "position": np.array([1.07e9, 0]), "velocity": np.array([0, 10.88e3])},
    "Callisto": {"mass": 1.08e23, "position": np.array([1.882e9, 0]), "velocity": np.array([0, 8.204e3])},
}

# Initialize position, velocity, and history arrays
for moon in moons.values():
    moon["position_history"] = [moon["position"].copy()]
    moon["velocity_history"] = [moon["velocity"].copy()]
    moon["eccentricity_history"] = []
    moon["distance_history"] = []

# Simulation loop
for step in range(steps):
    for moon_name, moon in moons.items():
        # Calculate distance and force
        r_vec = moon["position"]
        r = np.linalg.norm(r_vec)
        force = -G * jupiter_mass * moon["mass"] * r_vec / r**3

        # Update acceleration
        acceleration = force / moon["mass"]

        # Verlet integration: update position and velocity
        if step == 0:
            # First step: use velocity for initial step
            next_position = moon["position"] + moon["velocity"] * time_step + 0.5 * acceleration * time_step**2
        else:
            prev_position = moon["position_history"][-2]
            next_position = 2 * moon["position"] - prev_position + acceleration * time_step**2

        next_velocity = (next_position - moon["position"]) / time_step

        # Update histories
        moon["position"] = next_position
        moon["velocity"] = next_velocity
        moon["position_history"].append(next_position)
        moon["velocity_history"].append(next_velocity)
        moon["distance_history"].append(r)

        # Update eccentricity
        apoapsis = max(moon["distance_history"], default=r)
        periapsis = min(moon["distance_history"], default=r)
        eccentricity = (apoapsis - periapsis) / (apoapsis + periapsis)
        moon["eccentricity_history"].append(eccentricity)

# Visualization
years = np.linspace(0, simulation_years, len(moons["Io"]["eccentricity_history"]))

# Plot Eccentricity Evolution
plt.figure(figsize=(12, 6))
for moon_name, moon in moons.items():
    plt.plot(years, moon["eccentricity_history"], label=f"{moon_name}")
plt.title("Eccentricity Evolution of Galilean Moons Over 1000 Years")
plt.xlabel("Years")
plt.ylabel("Eccentricity")
plt.legend()
plt.grid()
plt.show()

# Plot Orbital Distance Evolution
plt.figure(figsize=(12, 6))
for moon_name, moon in moons.items():
    plt.plot(years, moon["distance_history"], label=f"{moon_name}")
plt.title("Orbital Distance Evolution of Galilean Moons Over 1000 Years")
plt.xlabel("Years")
plt.ylabel("Orbital Distance (m)")
plt.legend()
plt.grid()
plt.show()
