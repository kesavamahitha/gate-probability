import numpy as np
import matplotlib.pyplot as plt

# Theoretical CDF function for the exponential distribution
def theoretical_cdf(x, lambda_val):
    return 1 - np.exp(-x / lambda_val)

# Generate some random data following the exponential distribution
np.random.seed(20)
lambda_val = 2.0
data = np.random.exponential(scale=lambda_val, size=1000)

# Calculate the empirical CDF from the data
sorted_data = np.sort(data)
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# Generate x values for the theoretical CDF
x_theoretical = np.linspace(0, 350, 1000)
y_theoretical = theoretical_cdf(x_theoretical, lambda_val)

# Calculate the CDF of X^2
x_squared = sorted_data ** 2
cdf_squared = np.arange(1, len(x_squared) + 1) / len(x_squared)

# Plot the theoretical and empirical CDFs for X and X^2
plt.figure(figsize=(10, 6))

plt.plot(x_theoretical, y_theoretical, label="Theoretical CDF (X)")
plt.step(sorted_data, cdf, label="Empirical CDF (X)")

plt.plot(np.sort(x_squared), cdf_squared, label="Empirical CDF (X^2)")

plt.xlabel("x")
plt.ylabel("CDF")
plt.legend()
plt.title("Theoretical and Empirical CDFs for X and X^2")
plt.show()

