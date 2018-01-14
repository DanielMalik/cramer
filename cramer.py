import copy
import numpy
import pandas

from os import path

from solvers import DETERMINANT_SOLVERS
import ipdb

base_path = path.dirname(__file__)


class Cramer:

    def __init__(self, file_name):
        self.file_name = file_name
        self.raw_data = self._get_data_from_file()
        self.data = copy.deepcopy(self.raw_data)
        self.sums = [int(s.pop('s')) for s in self.data.values()]
        self.matrix_dimension = None
        self.matrix_determinant = None
        self.results = []

    def _get_data_from_file(self):
        try:
            with open(path.join(base_path, self.file_name), 'r') as file:
                data = pandas.read_csv(file, sep=',', dtype=str).to_dict(orient='index')
                if data:
                    return data
                else:
                    raise Exception('empty data')
        except FileNotFoundError as e:
            print(f'No such file found, {e}, text input: {self.file_name}')

    def _check_if_matrix_is_square(self):
        matrix_dimension_set = {len(self.data)}
        if matrix_dimension_set == {len(d) for d in self.data.values()}:
            self.matrix_dimension, = matrix_dimension_set
            self.unknowns = {key for key in self.data.get(0).keys()}
            return True
        else:
            raise Exception(f'{self.data} is not a n dimensional square matrix')

    def _check_if_determinant_is_not_zero(self):
        self.matrix_determinant = self.find_determinant(self.data, self.matrix_dimension)
        if self.matrix_determinant != 0:
            return True

    def check_if_cramers_rule_assumptions_are_met(self):
        try:
            if self._check_if_matrix_is_square():
                if self._check_if_determinant_is_not_zero():
                    return True
        except:
            print('something went wrong')

    def solve(self):
        if self.check_if_cramers_rule_assumptions_are_met():

            for key in self.unknowns:
                self.results.append(self._solve_key(key))

            # ipdb.set_trace()
            return True

    def _solve_key(self, key):
        matrix = {}
        print(self.data)
        for k, v in self.data.items():
            row = v
            print(k)
            print('org', row)
            print('pop', row.pop(key))
            print(self.sums)
            row[key] = self.sums[k]
            print(row)
            matrix[k] = row
            print(matrix)
        print('end', matrix)
        r = self.find_determinant(matrix, self.matrix_dimension)
        return r

    @staticmethod
    def find_determinant(matrix_as_dict, matrix_dimension):
        matrix = []
        for k, v in matrix_as_dict.items():
            matrix.append([int(number) for number in list(v.values())])
        solver = DETERMINANT_SOLVERS.get(matrix_dimension)
        return solver(numpy.array(matrix))

    @classmethod
    def from_input(cls):
        return cls(input('enter file_name: '))


if __name__ == '__main__':
    process = Cramer('test_1.csv')
    # process = Cramer('test_2.csv')
    # process = Cramer('wrong.csv')
    # process = Cramer.from_input()
    print(process.file_name)
    print(process.raw_data)
    print(process.data)
    print(process.sums)
    print(process.matrix_dimension)
    print(process.matrix_determinant)
    # process.check_if_cramers_rule_assumptions_are_met()
    process.solve()
    ipdb.set_trace()



