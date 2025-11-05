class Course:
    def __init__(self,name):
        self.name=name
        self.scores=[]

    def add_scores(self,s):
        self.scores.append(s)

    def avg(self):
        if len(self.scores)>0:
            average=sum(self.scores) / len(self.scores)
            return average
        else:
            return 0
       

    def info(self):
        print(f'과목:{self.name} , 평균:{self.avg()}')


c=Course('파이썬')
c.add_scores(80)
c.add_scores(90)
c.info()