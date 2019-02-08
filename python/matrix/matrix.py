class Matrix():
    def __init__(self, matrix_string):
        self.matrix = [[int(item) for item in row.split(' ')] \
            for _, row in enumerate(matrix_string.split('\n'))]

    def row(self, index=1):
        return self.matrix[index - 1]

    def column(self, index=1):
        result = []
        for rows in self.matrix:
            result.append(rows[index - 1])
        return result
