class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f'hi my name is {self.full_name}')


class Student(Member):
    def __init__(self, full_name, myReason):
        super().__init__(full_name)
        self.myReason = myReason

    def reason(self):
        print(f'my name is {self.full_name} and i am a student here because {self.myReason}')


class Instructor(Member):
    def __init__(self, full_name, skills = []):
        super().__init__(full_name)
        self.skills = skills

    def addSkill(self, newSkill):
        self.skills.append(newSkill)
        print(self.skills)



myMember = Student('kyle', 'i want to learn')

myMember.reason()

myInstructor = Instructor('madeline', ['python', 'react'])

print(myInstructor.skills)

myInstructor.addSkill('javascript')
