import pytest
import cramer


@pytest.mark.cramertest
class TestCramer:

    def test_open_file_and_create_data(self):
        process = cramer.Cramer('test_1.csv')
        assert process.file_name == 'test_1.csv'
        assert process.raw_data == {
            0: {'x': '2', 'y': '5', 'z': '3', 's': '5'},
            1: {'x': '4', 'y': '2', 'z': '5', 's': '4'},
            2: {'x': '3', 'y': '8', 'z': '4', 's': '9'},
        }
        assert process.data == {
            0: {'x': '2', 'y': '5', 'z': '3'},
            1: {'x': '4', 'y': '2', 'z': '5'},
            2: {'x': '3', 'y': '8', 'z': '4'},
        }

    def test_creating_subarrays(self):
        process = cramer.Cramer('test_1.csv')
        assert process.sums == [5, 4, 9]

    def test_check_if_matrix_is_n_dimensional_square_matrix(self):
        process = cramer.Cramer('test_1.csv')
        assert process._check_if_matrix_is_square() is True
        assert process.matrix_dimension == 3

    def test_check_non_square_matrix(self):
        process = cramer.Cramer('wrong.csv')
        with pytest.raises(Exception):
            process._check_if_matrix_is_square()

    def test_determinant_is_not_zero(self):
        process = cramer.Cramer('test_1.csv')
        assert process._check_if_determinant_is_not_zero() is True
        assert process.matrix_determinant == -2

    def test_if_cramers_rule_can_be_applied(self):
        process = cramer.Cramer('test_1.csv')
        assert process.check_if_cramers_rule_assumptions_are_met() is True
