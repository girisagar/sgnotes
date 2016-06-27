import inspect

class OverrideInspectionWarning(Exception):
    def __init__(self, message):
        super(OverrideInspectionWarning, self).__init__(message)

def override(parent):
    def wrapper(func, *args, **kwargs):
        def test_it(self, *args, **kwargs):
            flag = False
            try:
                parent_func = getattr(parent, func.__name__ )
                if (inspect.getargspec(func) == inspect.getargspec(parent_func) and 
                    func.__name__ == parent_func.__name__):
                    flag = True
            except AttributeError:
                flag = False
            if not flag:
                print OverrideInspectionWarning('Warning: there is no method {} on super class {}'.format(func.__name__, parent.__name__))
            return func(self, *args, **kwargs)
        return test_it
    return wrapper


#usage
class A():
    def display():
	print "super class display"

class B():

    @overridei(A) # Execution Type: inpects  display method overrided from A or not
    def display():
	print "sub class display"
