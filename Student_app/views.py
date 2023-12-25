from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *
from django.db.models import Sum
def view_students(request,id):
    student=Student.objects.filter(division__division=id)
    if request.GET.get('search'):
        student=student.filter(student_name__icontains=request.GET.get('search'))
    division=Division.objects.all()
    paginator = Paginator(student, 15)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    student = paginator.get_page(page_number)
    return render(request,'students.html',{'students':student,'division':division})

def report_card(request,id):
    rank=Rank.objects.filter(student__student_id__student_id=id)
    rank=rank[0].rank
    student=Student_marks.objects.filter(student__student_id__student_id=id)
    student_name=student[1].student.student_name
    marks=student.aggregate(marks=Sum('marks'))
    return render(request,'report_card.html',{'totalmarks':marks,'student':student,'student_name':student_name,'rank':rank})
def home(request):
    if request.GET.get("search"):
        quaryset=Student.objects.filter(student_name__icontains=request.GET.get("search"))
        division=Division.objects.all()
        return render(request,'students.html',{'students':quaryset,'division':division})
    return render(request,'home.html')

        