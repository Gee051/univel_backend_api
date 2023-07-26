from django.contrib import admin
from .models import Course, Student, Tutor, Admission

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Admission)
