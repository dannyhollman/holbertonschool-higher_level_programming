#!/usr/bin/python3
"""multiply two numpy arrays"""


def lazy_matrix_mul(m_a, m_b):
    """function to multiply two numpy arrays"""
    import numpy as np

    a = np.array(m_a)
    b = np.array(m_b)
    return np.dot(a, b)
