# coding: utf-8


def method_friendly_decorator(method_to_decorator):
    def wrapper(self, lie):
        lie = lie - 3
        return method_to_decorator(self, lie)
    return wrapper


class Lucy:

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print("I am {}, what did you think?".format(self.age + lie))


l = Lucy()
l.say_your_age(-3)
