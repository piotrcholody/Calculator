import Exceptions
import abc


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, first, second, equation):
        pass


class InputDataValidator(AbstractValidator):

    @staticmethod
    def _is_number(number):
        return isinstance(number, (int, float))

    @staticmethod
    def _is_string(string):
        return isinstance(string, str)

    @staticmethod
    def _is_zero(number):
        return number == 0

    @staticmethod
    def _is_log_base_valid(number):
        return number > 0 and number != 1

    @staticmethod
    def _is_positive(number):
        return number > 0

    @staticmethod
    def _is_integer(number):
        return isinstance(number, int)

    @staticmethod
    def validate(self, first, second, equation):
        if equation != "derivative":
            if not self._is_number(first) or not self._is_number(second):
                raise Exceptions.NotANumber
        if equation == "logarithm":
            if not self._is_positive(first):
                raise Exceptions.NotAPositiveNumber
            if not self._is_log_base_valid(second):
                raise Exceptions.NotValidLogarithmBase
        if equation == "derivative":
            if not self._is_string(first):
                raise Exceptions.NotAFunction
            if not self._is_integer(second):
                raise Exceptions.NotAnInteger
            if not self._is_positive(second):
                raise Exceptions.NotAPositiveNumber
        if equation == "divide":
            if self._is_zero(second):
                raise Exceptions.DivideByZero





