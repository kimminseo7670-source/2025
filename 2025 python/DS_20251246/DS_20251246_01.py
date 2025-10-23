class DSstudent:
    def __init__(self,stu_id,name):
        self.name=name
        self.stu_id=stu_id

    def show_info(self):
        print('학번:',self.stu_id,',이름:',self.name)

student=DSstudent(20251246,'김민서')
student.show_info()
