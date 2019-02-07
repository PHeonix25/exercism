class Matrix():
    def __init__(self, matrix_string):
        # I dislike building the array myself, but numpy isn't available...?
        # Also, this could be "more pythonic", but it gets very confusing.
        self.matrix = []
        for rownum, row in enumerate(matrix_string.split('\n')):
            self.matrix.append([])
            for item in row.split(' '):
                self.matrix[rownum].append(int(item))

    def row(self, index=1):
        return self.matrix[index - 1]

    def column(self, index=1):
        result = []
        for rows in self.matrix:
            result.append(rows[index - 1])
        return result
