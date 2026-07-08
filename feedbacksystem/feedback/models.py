from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email    

class Feedback(models.Model):

    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    subject = models.CharField(max_length=100)

    message = models.TextField()

    reply = models.TextField(blank=True)

    status = models.CharField(max_length=30,default="Pending")

    def __str__(self):
        return self.subject

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    reply = models.TextField(blank=True)
    status = models.CharField(max_length=30, default="Pending")

    def __str__(self):
        return self.subject