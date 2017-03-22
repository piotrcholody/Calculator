import abc
import sympy
import InputDataValidator
import math


class AbstractCalculator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add(self, first, second):
        pass

    @abc.abstractmethod
    def subtract(self, first, second):
        pass

    @abc.abstractmethod
    def multiplicate(self, first, second):
        pass

    @abc.abstractmethod
    def divide(self, first, second):
        pass

    @abc.abstractmethod
    def logarithm(self, first, second):
        pass

    @abc.abstractmethod
    def derivative(self, function, variable):
        pass


class Calculator(AbstractCalculator):

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

    def add(self, first, second):
        InputDataValidator.InputDataValidator.validate(self,first, second, "add")
        return first+second

    def subtract(self, first, second):
        InputDataValidator.InputDataValidator.validate(self,first, second, "subtract")
        return first-second

    def multiplicate(self, first, second):
        InputDataValidator.InputDataValidator.validate(self,first, second, "multiplicate")
        return first*second

    def divide(self, first, second):
        InputDataValidator.InputDataValidator.validate(self,first, second, "divide")
        return first/second

    def logarithm(self, first, second):
        InputDataValidator.InputDataValidator.validate(self,first, second, "logarithm")
        return math.log(first, second)

    def derivative(self, function, variable):
        InputDataValidator.InputDataValidator.validate(self,function, variable, "derivative")
        return sympy.diff(function, 'x', variable)

