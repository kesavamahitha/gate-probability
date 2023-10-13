#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SAMPLE_SIZE 10000  // Number of random samples to generate

double exponential_pdf(double x, double lambda) {
    if (x > 0) {
        return (1.0 / lambda) * exp(-x / lambda);
    } else {
        return 0.0;
    }
}

double exponential_cdf(double x, double lambda) {
    if (x <= 0) {
        return 0.0;
    } else {
        return 1.0 - exp(-x / lambda);
    }
}

int main() {
    double lambda = 2.0; 
    double x = 2.1;      // The value of x for which you want to calculate CDF

    // Calculate the theoretical CDF of X
    double theoretical_cdf_x = exponential_cdf(x, lambda);

    printf("Theoretical CDF of X at x = %.2f: %.6f\n", x, theoretical_cdf_x);
    
    double theoretical_cdf_x2 = exponential_cdf(x * x, lambda);

    printf("Theoretical CDF of X^2 at x = %.2f: %.6f\n", x * x, theoretical_cdf_x2);

    // Generate simulated data following the exponential distribution for X
    double simulated_data_x[SAMPLE_SIZE];
    for (int i = 0; i < SAMPLE_SIZE; i++) {
        double u = (double)rand() / RAND_MAX;  // Uniform random number between 0 and 1
        simulated_data_x[i] = -lambda * log(1 - u);
    }

    // Calculate the simulated CDF of X
    int count_x = 0;
    for (int i = 0; i < SAMPLE_SIZE; i++) {
        if (simulated_data_x[i] <= x) {
            count_x++;
        }
    }
    double simulated_cdf_x = (double)count_x / SAMPLE_SIZE;

    printf("Simulated CDF of X at x = %.2f: %.6f\n", x, simulated_cdf_x);

    // Generate simulated data following the exponential distribution for X^2
    double simulated_data_x2[SAMPLE_SIZE];
    for (int i = 0; i < SAMPLE_SIZE; i++) {
        double u = (double)rand() / RAND_MAX;  // Uniform random number between 0 and 1
        double x_val = -lambda * log(1 - u);
        simulated_data_x2[i] = pow(x_val, 2);
    }

    // Calculate the simulated CDF of X^2
    int count_x2 = 0;
    for (int i = 0; i < SAMPLE_SIZE; i++) {
        if (simulated_data_x2[i] <= x * x) {
            count_x2++;
        }
    }
    double simulated_cdf_x2 = (double)count_x2 / SAMPLE_SIZE;

    printf("Simulated CDF of X^2 at x = %.2f: %.6f\n", x * x, simulated_cdf_x2);

    return 0;
}

