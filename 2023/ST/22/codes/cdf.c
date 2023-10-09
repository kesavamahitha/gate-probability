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
    double x = 1.0;      // The value of x for which you want to calculate CDF

    // Calculate the theoretical CDF
    double theoretical_cdf = exponential_cdf(x, lambda);

    printf("Theoretical CDF at x = %.2f: %.6f\n", x, theoretical_cdf);

    // Generate simulated data following the exponential distribution
    double simulated_data[SAMPLE_SIZE];
    for (int i = 0; i < SAMPLE_SIZE; i++) {
        double u = (double)rand() / RAND_MAX;  // Uniform random number between 0 and 1
        simulated_data[i] = -lambda * log(1 - u);
    }

    // Calculate the simulated CDF
    int count = 0;
    for (int i = 0; i < SAMPLE_SIZE; i++) {
        if (simulated_data[i] <= x) {
            count++;
        }
    }
    double simulated_cdf = (double)count / SAMPLE_SIZE;

    printf("simulated CDF at x = %.2f: %.6f\n", x, simulated_cdf);

    return 0;
}

