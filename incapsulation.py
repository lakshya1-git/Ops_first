class ineuron:
    def __init__(self):
        self.students1 = "data science"
    def students(self):
        print(self.students1)
i = ineuron()
i.students()
i.student1 = "data analytics"
class ineuron1:
    def __init__(self):
        self.__students1 = "data science"
    def students(self):
        print(self.__students1)
i1 = ineuron1()
i1.students()
i1.student1 = "data analytics"
i1.__students1 ='big data'
