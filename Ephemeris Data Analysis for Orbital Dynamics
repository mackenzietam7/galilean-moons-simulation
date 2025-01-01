import pandas as pd
import matplotlib.pyplot as plt

# List of moons and their corresponding CSV files
moons = {
    'Io': 'Io_1000_years_data.csv',
    'Europa': 'Europa_1000_years_data.csv',
    'Ganymede': 'Ganymede_1000_years_data.csv',
    'Callisto': 'Callisto_1000_years_data.csv'
}

# Loop through each moon and generate plots
for moon_name, file_name in moons.items():
    # Load the moon's data
    moon_data = pd.read_csv(file_name)

    # Check column names
    print(f"Columns in {moon_name}: {moon_data.columns}")

    # Ensure correct column names are used
    time_col = 'datetime_str'  # Column for timestamps
    eccentricity_col = 'e'  # Column for eccentricity
    distance_col = 'a'  # Column for semi-major axis (AU)

    # Convert semi-major axis from AU to meters
    moon_data[distance_col] = moon_data[distance_col] * 1.496e11

    # Plot Eccentricity
    plt.figure(figsize=(12, 6))
    plt.plot(moon_data[time_col], moon_data[eccentricity_col], label=f'{moon_name} Eccentricity')
    plt.title(f'Eccentricity of {moon_name} Over 1000 Years')
    plt.xlabel('Time')
    plt.ylabel('Eccentricity')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot Orbital Distance
    plt.figure(figsize=(12, 6))
    plt.plot(moon_data[time_col], moon_data[distance_col], label=f'{moon_name} Orbital Distance')
    plt.title(f'Orbital Distance of {moon_name} Over 1000 Years')
    plt.xlabel('Time')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.grid()
    plt.show()
