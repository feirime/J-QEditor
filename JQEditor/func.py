from math import sqrt


def read_tmp_cell(self, n, filename):
    self.n = n
    self.read_data(filename, True)


def check_cell_size(file_path):
    line_count = 0
    with open(file_path, 'r') as file:
        for _ in file:
            line_count += 1

    n = sqrt(line_count)
    return int(n) if n.is_integer() else None