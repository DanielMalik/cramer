import pytest
import cramer


@pytest.mark.cramertest
class TestCramer:

    def test_open_file_and_create_data(self):
        process = cramer.Cramer('test_1.csv')
        assert process.file_name == 'test_1.csv'
        assert process.data == {
            0: {'x': '2', 'y': '5', 'z': '3', 's': '5'},
            1: {'x': '4', 'y': '2', 'z': '5', 's': '4'},
            2: {'x': '3', 'y': '8', 'z': '4', 's': '9'},
        }
