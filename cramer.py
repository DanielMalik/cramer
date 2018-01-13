import pandas
from os import path

import ipdb

base_path = path.dirname(__file__)


class Cramer:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self._get_data_from_file()

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

    @classmethod
    def from_input(cls):
        return cls(input('enter file_name: '))


if __name__ == '__main__':
    process = Cramer.from_input()
    print(process.file_name)
    print(process.data)
    # ipdb.set_trace()
