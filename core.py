class Vector:
    def __init__(self, data: list[float]):
        self.data = list(data)

    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)

    def __repr__(self) -> str:
        return f" Vector ({self.data})"


class Matrix:
    def __init__(self, data: list[list[float]]):
        self.data = [list(r) for r in data]

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)

    def __repr__(self) -> str:
        return f" Matrix ({self.data})"

    def matrix_mul_vector(self, x: Vector) -> Vector:
        """Matrix x Vector, returning a Vector."""
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0

        #  check dimensions
        if cols != len(x):
            raise ValueError(
                f"Error: Matrix column({cols}) does not match Vector length({len(x)})"
            )

        result = []
        for i in range(rows):
            row = self.data[i]
            s = 0.0
            for k in range(cols):
                s += row[k] * x[k]
            result.append(s)

        return Vector(result)

    def matrix_mul_matrix(self, other: "Matrix") -> "Matrix":
        """Matrix x Matrix, returning a Matrix."""
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0
        other_rows = len(other.data)
        other_cols = len(other.data[0]) if other_rows > 0 else 0

        #  check dimensions
        if cols != other_rows:
            raise ValueError(
                f"Error: Matrix A column({cols}) does not match Matrix B row({other_rows})"
            )

        result = []
        for i in range(rows):
            row = self.data[i]
            row_result = []
            for j in range(other_cols):
                s = 0.0
                for k in range(cols):
                    s += row[k] * other.data[k][j]
                row_result.append(s)
            result.append(row_result)

        return Matrix(result)
