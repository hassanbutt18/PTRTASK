from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.first_name


class EmploymentHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employment_history')
    start_date = models.DateField(null=True ,blank=True)
    end_date = models.DateField(null=True ,blank=True)
    position = models.CharField(max_length=100)
    current_job = models.BooleanField(default=False)
