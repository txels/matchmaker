from hamcrest.core.base_matcher import BaseMatcher


class CallableMatcher(BaseMatcher):
    """
    This will be used as a base class for all created matchers
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _matches(self, item):
        return self.callee(item, *self.args, **self.kwargs)


def matcher(func):
    """
    Decorator that converts a function into a hamcrest matcher

    The function must accept a parameter and return a boolean
    """
    def _func(self, *args, **kwargs):
        return func(*args, **kwargs)

    if func.__doc__:
        funcdoc = func.__doc__
    else:
        funcdoc = func.__name__.replace('_', ' ').capitalize()

    def describe_to(self, description):
        mydoc = funcdoc.format(*self.args)
        return description.append_text(mydoc)

    cls = type(func.__name__, (CallableMatcher,),
               {'callee': _func,
                'describe_to': describe_to})
    return cls
