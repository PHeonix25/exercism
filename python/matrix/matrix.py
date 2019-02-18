class Matrix():
    def __init__(self, matrix_string):
        self.__matrix_rows = [[int(item) for item in row.split(' ')]
                          for row in matrix_string.split('\n')]
        self.__matrix_columns = \
            [list(column) for column in zip(*self.__matrix_rows)]

    def row(self, index=1):
        return self.__matrix_rows[index-1]

    def column(self, index=1):
        return self.__matrix_columns[index-1]
