from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from schoolapp.models import Student

def login_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        usr = authenticate(request, username=username, password=password)
        if usr is not None:
            login(request, usr)
            if 'failed_login_attempts' in request.session:
                del request.session['failed_login_attempts']
            success_logins = request.COOKIES.get('success_logins', 0)
            success_logins = int(success_logins) + 1
            response = redirect('student-all')
            response.set_cookie('success_logins', success_logins)
            return response
        else:
            request.session['failed_login_attempts'] = request.session.get('failed_login_attempts', 0) + 1
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        failed_login_attempts = request.session.get('failed_login_attempts', 0)
        success_logins = request.COOKIES.get('success_logins', 0)
        
        return render(request, 'login.html', {'failed_login_attempts': failed_login_attempts, 'success_logins': success_logins})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


@login_required
def logout_student(request):
    logout(request)
    return redirect('login')
