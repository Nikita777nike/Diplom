from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def students(request):
    if request.user.is_student:
        student = Student.objects.get(user=request.user)
        context = {'student': student}
        return render(request, 'students.html', context)
    else:
        return redirect('home')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST['role']  # student or teacher

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        if role == 'student':
            user.is_student = True
            Student.objects.create(
                user=user,
                roll_number='12345',  # Введите актуальный номер
                course='Medicine',  # Введите актуальную специальность
                year_of_study=1,  # Введите актуальный год обучения
            )
        elif role == 'teacher':
            user.is_teacher = True
            Teacher.objects.create(
                user=user,
                department='Surgery',  # Введите актуальное отделение
                designation='Professor',  # Введите актуальную должность
            )

        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_student:
                return redirect('students')
            else:
                return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
