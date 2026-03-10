import numpy as np
from numpy.typing import NDArray


def probability_of_one_or_two_allele(p_aa: NDArray[np.float64]) -> NDArray[np.float64]:
    p_a = p_aa ** 0.5
    return p_aa + 2 * p_a * (1 - p_a)


def calculate_probability_of_one_or_two_allele():
    p_aa = np.loadtxt('data.txt', dtype=np.float64)
    p_array = probability_of_one_or_two_allele(p_aa)
    np.savetxt('res.txt', p_array, fmt='%.3f', newline=' ')


if __name__ == '__main__':
    calculate_probability_of_one_or_two_allele()
