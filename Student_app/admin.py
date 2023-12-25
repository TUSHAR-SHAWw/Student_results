from django.contrib import admin
from django.db.models import Sum
from Student_app.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Student_id)
admin.site.register(Division)
admin.site.register(Subjects)
class Student_ranks(admin.ModelAdmin):
    list_display=['student','rank','total_marks']

    def total_marks(self,obj):
        marks=Student_marks.objects.filter(student=obj.student)
        totalmarks=Student
        return 0
admin.site.register(Rank,Student_ranks)
class Student_marks_Admin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(Student_marks,Student_marks_Admin)