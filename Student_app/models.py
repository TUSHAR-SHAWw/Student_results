from django.db import models

class Division(models.Model):
    division=models.CharField(max_length=100)
    def __str__(self)->str:
        return self.division
class Student_id(models.Model):
    student_id=models.CharField(max_length=100)
    def __str__(self)->str:
        return self.student_id
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    student_id=models.OneToOneField(Student_id,on_delete=models.CASCADE)
    division=models.ForeignKey(Division,on_delete=models.CASCADE)
    student_age=models.IntegerField()
    student_email=models.EmailField()
    student_address=models.TextField()
    def __str__(self) -> str:
        return self.student_name
    class META:
        ordering=['student_name']
class Subjects(models.Model):
    subject=models.CharField( max_length=50)
    def __str__(self) -> str:
        return self.subject

class Student_marks(models.Model):
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    marks=models.IntegerField()
    def __str__(self)->str:
        return f'{self.student}, {self.subjects}'
    class META:
        unique_together=['student','subject']

class Rank(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    rank=models.IntegerField()
    creaton_date=models.DateField(auto_now_add=True)
