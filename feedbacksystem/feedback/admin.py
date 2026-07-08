from django.contrib import admin
from .models import Student, Feedback

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'status')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'status')
    search_fields = ('subject', 'student__name')
