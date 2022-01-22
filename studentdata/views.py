from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateStudent
from django.contrib.auth.decorators import login_required
from .models import Student
# Create your views here.


@login_required
def create_student(request):
    student_form = CreateStudent(None)
    if request.method == 'POST':
        student_form = CreateStudent(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
        # image = student_form.clean_profile_pic(request.FILES['photo'])
        # name = student_form.cleaned_data('name')

        return redirect('studentdata:students')
    context = {
        'title': 'IT Kerala | Student Creation Form',
        'student_form': student_form,
        'value': 'Submit',
    }
    return render(request, 'forms/create-student.html', context)


# @login_required
def home(request):
    return render(request, 'index.html')

@login_required
def view_students(request):
    context = {
        'title':'IT Kerala | Students',
        'students': Student.objects.all(),
        'reg_count':Student.objects.count
    }
    return render(request,'students.html',context)


@login_required
def individual_student(request,id):
    context = {
        'title': 'IT Kerala | Students',
        'student': get_object_or_404(Student,id=id)
    }
    return render(request, 'individual-student.html', context)

@login_required
def edit_student_data(request,id):
    student = get_object_or_404(Student,id=id)
    student_form = CreateStudent(instance=student)
    if request.method == 'POST':
        student_form = CreateStudent(request.POST, request.FILES,instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('studentdata:students')
    context = {
        'title': 'IT Kerala | Student Creation Form',
        'student_form': student_form,
        'value': 'Submit',
    }
    return render(request, 'forms/create-student.html', context)
