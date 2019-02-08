class Matrix():
    def __init__(self, matrix_string):
        self.matrix = [[int(item) for item in row.split(' ')] \
            for _, row in enumerate(matrix_string.split('\n'))]

    def row(self, index=1):
        return self.matrix[index - 1]

    def column(self, index=1):
        return [rows[index-1] for rows in self.matrix]
