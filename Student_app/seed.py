# from faker import Faker
# import random
# from .models import *
# from django.db.models import Sum
# fake=Faker()
# def create_students(n):
#     division=Division.objects.all()
#     for _ in range(0,n):
#         index=random.randint(0,len(division)-1)
#         student_id=f'STU-{random.randint(100,999)}'
#         student_id=Student_id.objects.create(
#             student_id=student_id
#         )
#         stu=Student.objects.create(
#             student_name=fake.name(),
#             student_id=student_id,
#             division=division[index],
#             student_age=random.randint(7,18),
#             student_email=fake.email(),
#             student_address=fake.address()
#         )
#         stu.save()
# def create_marks():
#     students=Student.objects.all()
#     subject=Subjects.objects.all()
#     for student in students:
#         for subjects in subject:
#             mark=random.randint(0,100)
#             a=Student_marks.objects.create(
#                 student=student,
#                 subject=subjects,
#                 marks=mark
#             )
#             a.save()
# def create_ranks():
#     student=Student.objects.annotate(marks=Sum('student_marks__marks')).order_by('-marks')
#     i=1
#     for stu in student:
#         Rank.objects.create(
#             student=stu,
#             rank=i
#         )
#         i=i+1