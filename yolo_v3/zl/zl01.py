class Student():
    def __init__(self,id,name):
        self.id = id
        self.name =name

    def __repr__(self):
        return 'id='+self.id+', name='+self.name

    def __call__(self):
        print('I will be back!')


class Undergraduate(Student):
        def study_class(self):
            pass

        def attend_activity(self):
            pass


xiaoming = Student('001', 'zhaoliang')
# help(xiaoming)
isinstance(xiaoming,Student)
issubclass(Undergraduate,Student)

class TestIter(object):
    def __init__(self):
        self.l = [1,3,2,3,4,5]
        self.i = iter(self.l)

    def __call__(self):
        item = next(self.i)
        print("__call__ is called,fowhich would return",item)

    def __iter__(self):
        print("__iter__is called!")
        return iter(self.l)


t = TestIter()
t()
for e in TestIter():
    print(e)
