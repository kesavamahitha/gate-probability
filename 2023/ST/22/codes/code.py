import numpy as np

# Set the random seed for reproducibility
np.random.seed(50)

# Generate a random value for lambda
true_lambda = np.random.uniform(1, 6)  # You can adjust the range as needed

# No. of samples
n = 10000

# Generate random values of X based on the given probability density function
X = np.random.exponential(scale=true_lambda, size=n)

# Compute Y using X
Y = X ** 2

# Compute the sample mean of Y (Y̅)
sample_mean_Y = np.mean(Y)

# Estimate lambda using (Y̅)
estimated_lambda = np.sqrt(sample_mean_Y / 2)
print("True Lambda:", true_lambda)
print("Estimated Lambda:", estimated_lambda)
print(X)
