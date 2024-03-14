import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  # нижня межа
b = 2  # верхня межа

def monte_carlo_method(f, a, b, num_points):
    x_rand = np.random.uniform(a, b, num_points)
    y_rand = np.random.uniform(0, f(b), num_points)  
    points_under_curve = sum(y_rand <= f(x_rand))
    area_rectangle = (b - a) * f(b)  
    area_of_interest = (points_under_curve / num_points) * area_rectangle

    return area_of_interest

num_points_per_experiment = 10000
num_experiments = 100

results = [monte_carlo_method(f, a, b, num_points_per_experiment) for _ in range(num_experiments)]
result_quad, error_quad = spi.quad(f, a, b)
# Обчислення інтеграла
print(f"Метод Монте-Карло: {np.mean(results)}")
print(f"Інтеграл (quad): {result_quad}")