from django.db import models

class Candidate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    years_of_experience = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    current_salary = models.IntegerField()
    expected_salary = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='Applied', max_length=20)

    def __str__(self):
        return self.name

    def ready(self):
        import usersearch.signals