# from datetime import datetime 
# from dateutil.relativedelta import relativedelta --make sure you install them
from django.db import models
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=500, default="3 months")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(default=None)

    def __str__(self):
        return self.name


    # @property -- to calculate your date and time
    # def end_date(self):
    #     if self.start_date:
    #         duration_parts = self.duration.split()
    #         if len(duration_parts) == 2:
    #             duration_value, duration_unit = duration_parts
    #             if duration_unit == 'months':
    #                 months = int(duration_value)
    #                 start_datetime = datetime.combine(self.start_date, datetime.min.time())
    #                 end_datetime = start_datetime + relativedelta(months=months)
    #                 return end_datetime.date()
    #     return None


class Student(models.Model):
    class GenderChoice(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=5, choices=GenderChoice.choices)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.student.name} is registered"
