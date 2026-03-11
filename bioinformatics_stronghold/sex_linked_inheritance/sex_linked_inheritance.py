import numpy as np
from numpy.typing import NDArray


def probability_of_x_carrier(p_x: NDArray[np.float64]) -> NDArray[np.float64]:
    return 2 * p_x * (1 - p_x)


def calculate_probability_of_x_carrier():
    p_x = np.loadtxt('data.txt', dtype=np.float64)
    p_a = probability_of_x_carrier(p_x)
    np.savetxt('res.txt', p_a, fmt='%.3f', newline=' ')


if __name__ == '__main__':
    calculate_probability_of_x_carrier()
