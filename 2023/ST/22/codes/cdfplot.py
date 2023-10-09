import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parameters
lambda_val = 2.0  # Change this to your desired lambda
sample_size = 100000  # Increased sample size

# Generate empirical data following the exponential distribution
u_values = np.random.rand(sample_size)
simulated_data = -lambda_val * np.log(1 - u_values)

# Calculate the theoretical CDF
x_theoretical = np.linspace(0, np.max(simulated_data), 1000)
theoretical_cdf = expon.cdf(x_theoretical, scale=1 / lambda_val)

# Calculate the simulated CDF
sorted_simulated_data = np.sort(simulated_data)
simulated_cdf = np.arange(1, sample_size + 1) / sample_size

# Plot CDFs
plt.figure(figsize=(8, 5))
plt.plot(x_theoretical, theoretical_cdf, label="Theoretical CDF")
plt.step(sorted_simulated_data, simulated_cdf, label="simulated CDF")

plt.xlabel("x")
plt.ylabel("CDF")
plt.legend()
plt.title("Theoretical and simulated CDFs (Increased Sample Size)")
plt.grid(True)
plt.show()

