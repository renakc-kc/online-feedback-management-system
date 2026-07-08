from django.shortcuts import render, redirect
from .models import Student
from .models import Student, Feedback

def register(request):

    if request.method == "POST":

        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password']
        )

        return redirect('/register')

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        try:
            student = Student.objects.get(
                email=email,
                password=password
            )

            request.session['student_id'] = student.id

            return redirect('/dashboard/')

        except Student.DoesNotExist:

            return render(request,
                          'login.html',
                          {'error':'Invalid Email or Password'})

    return render(request,'login.html')

def dashboard(request):

    student = Student.objects.get(
        id=request.session['student_id']
    )

    return render(
        request,
        'welcome.html',
        {'student':student}
    )

def sendfeedback(request):

    student = Student.objects.get(
        id=request.session['student_id']
    )

    if request.method=="POST":

        Feedback.objects.create(

            student=student,

            subject=request.POST['subject'],

            message=request.POST['message']

        )

        return redirect('/dashboard/')

    return render(request,'sendfeedback.html')

def myfeedback(request):

    student = Student.objects.get(
        id=request.session['student_id']
    )

    feedback = Feedback.objects.filter(
        student=student
    )

    return render(
        request,
        'myfeedback.html',
        {'feedback': feedback}
    )

def adminlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email == "admin@gmail.com" and password == "admin123":
            return redirect('/admindashboard/')
        else:
            return render(request, 'adminlogin.html', {
                'error': 'Invalid Admin Credentials'
            })

    return render(request, 'adminlogin.html')

def admindashboard(request):
    total_students = Student.objects.count()
    total_feedback = Feedback.objects.count()
    replied = Feedback.objects.filter(status="Replied").count()
    pending = Feedback.objects.filter(status="Pending").count()

    context = {
        'total_students': total_students,
        'total_feedback': total_feedback,
        'replied': replied,
        'pending': pending,
    }

    return render(request, 'admindashboard.html', context)

def allfeedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'allfeedback.html', {'feedback': feedback})

def replyfeedback(request, id):
    if request.method == "POST":
        feedback = Feedback.objects.get(id=id)
        feedback.reply = request.POST['reply']
        feedback.status = "Replied"
        feedback.save()

    return redirect('/allfeedback/')

def viewstudents(request):
    students = Student.objects.all()
    return render(request, 'viewstudents.html', {'students': students})

def deletefeedback(request, id):
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('/allfeedback/')