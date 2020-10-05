import numpy as np


class Concatenation:
    def __init__(self, a1: np.ndarray, a2: np.ndarray) -> None:
        self._a1: np.ndarray = a1
        self._a2: np.ndarray = a2

    def concatenate(self) -> np.ndarray:
        return np.core.defchararray.add(self._a1, self._a2)
