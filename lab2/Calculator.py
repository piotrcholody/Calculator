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

    def add(self, first, second):
        InputDataValidator.InputDataValidator.validate(first, second, "add")
        return first+second

    def subtract(self, first, second):
        InputDataValidator.InputDataValidator.validate(first, second, "subtract")
        return first-second

    def multiplicate(self, first, second):
        InputDataValidator.InputDataValidator.validate(first, second, "multiplicate")
        return first*second

    def divide(self, first, second):
        InputDataValidator.InputDataValidator.validate(first, second, "divide")
        return first/second

    def logarithm(self, first, second):
        InputDataValidator.InputDataValidator.validate(first, second, "logarithm")
        return math.log(first, second)

    def derivative(self, function, variable):
        InputDataValidator.InputDataValidator.validate(function, variable, "derivative")
        return sympy.diff(function, 'x', variable)

