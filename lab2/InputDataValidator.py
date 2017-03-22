import Exceptions
import abc


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, first, second, equation):
        pass


class InputDataValidator(AbstractValidator):

    @staticmethod
    def validate(self, first, second, equation):
        if equation != "derivative":
            if not self._is_number(first) or not self._is_number(second):
                raise Exceptions.NotANumber
        if equation == "derivative":
            if not self._is_string(first):
                raise Exceptions.NotAFunction
            if not self._is_integer(second):
                raise Exceptions.NotAnInteger
            if self._is_negative(second):
                raise Exceptions.NotAPositiveNumber
        if equation == "logarithm":
            if not self._is_positive(second):
                raise Exceptions.NotValidLogarithm
            if self._is_log_base_one(second):
                raise Exceptions.NotValidLogarithm
            if not self._is_positive(first) or not self._is_positive(second):
                raise Exceptions.NotAPositiveNumber
        if equation == "divide" and self._is_zero(second):
            raise Exceptions.DivideByZero

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
    def _is_positive(number):
        return number > 0

    @staticmethod
    def _is_negative(number):
        return number < 0

    @staticmethod
    def _is_log_base_one(number):
        return number == 1

    @staticmethod
    def _is_integer(number):
        return isinstance(number, int)



