import copy
import pandas

from os import path

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
            return True
        else:
            raise Exception(f'{self.data} is not a n dimensional square matrix')

    def _check_if_determinant_is_not_zero(self):
        return False

    def check_if_cramers_rule_assumptions_are_met(self):
        try:
            if self._check_if_matrix_is_square():
                if self._check_if_determinant_is_not_zero():
                    return True
        except:
            print('wrong')

    @classmethod
    def from_input(cls):
        return cls(input('enter file_name: '))


if __name__ == '__main__':
    # process = Cramer('test_1.csv')
    process = Cramer.from_input()
    print(process.file_name)
    print(process.raw_data)
    print(process.data)
    print(process.sums)
    process.check_if_cramers_rule_assumptions_are_met()
    # ipdb.set_trace()
