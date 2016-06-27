
class Config(object):
    _instance = None
    def __init__(self):
	self.fields = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def set_fields(self, fields):
        self.fields = fields
	#print self.fields
    
    def get_fields(self):
	if self.fields is None:
	    raise Exception("Sorting Fields not provided\n eg: sort(iterable, fields=['name' ,'dob'])")
        return self.fields
 
cfg = Config()

class Sortable(object):
    """
	Inherit Sortable from the child class, example given below

    """
    def __init__(self):
        self.eq = None

    def __hash__(self, *args):
	#print args
	argsum = ""
	for arg in args:
	    argsum += hash(arg)
	return hash(argsum)
        #return hash(hash(self.name)+hash(self.date))

    def equal(self, other):
        self.eq = 0
        for i, field in enumerate(cfg.get_fields()):
            if (getattr(self, field) == getattr(other, field)) and self.eq == i:
                self.eq = i+1
            else:
                break
        return self.eq

    def __eq__(self, other):
        index = self.equal(other)            
        return len(cfg.fields) == index

    def __lt__(self, other):
        index = self.equal(other)
        if index < len(cfg.fields):
            return (getattr(self, cfg.fields[index]) < getattr(other, cfg.fields[index]))
        return False

    def __gt__(self, other):
        index = self.equal(other)
        if index < len(cfg.fields):
            return (getattr(self, cfg.fields[index]) > getattr(other, cfg.fields[index]))
        return False
    
    def __ne__(self, other):
        return not(self.__eq__(other))


def sort(lst, reverse=False, fields=[]):
    cfg = Config()

    cfg.set_fields(fields)

    if isinstance(fields, list):
        return sorted(lst, reverse=reverse)
    else:
        raise Exception("No Fields provided")


# eg ...................
class Student(Sortable): # here student inherits Sortable

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __repr__(self):
        return "{}, {}\n".format(self.name, self.date)

    def __str__(self):
        return "{}, {}".format(self.name, self.date)


if __name__ == '__main__':
    from datetime import datetime, timedelta
    today = datetime.today()

    obj_list = []
    # adding objects
    s0 = Student("Zala Force", today-timedelta(days=1))
    s1 = Student("Kaccha Aam", today-timedelta(days=10))
    s2 = Student("Alla Maske", today-timedelta(days=15))
    s3 = Student("Namila Dua", today-timedelta(days=30))
    s4 = Student("Kaccha Aam", today-timedelta(days=12))
    obj_list.append(s0)
    obj_list.append(s1)
    obj_list.append(s2)
    obj_list.append(s3)
    obj_list.append(s4)

    fields=['name', "date"]
    print sort(obj_list, fields=fields, reverse=True)

