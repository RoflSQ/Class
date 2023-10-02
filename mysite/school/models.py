from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=25)
    body = models.TextField()

    def __str__(self):
        return self.name

class Choices:
    Clas_choices = (
    ('A',"A"),
    ('Б',"Б"),
    ('В',"В"),
    ('Г',"Г"),
    ('Д',"Д"),
    ('Е',"Е"))


class Day_Sub_Class(models.Model):
    class_name = models.CharField(choices = Choices.Clas_choices, default="A", max_length=1)
    first_s = models.CharField(max_length=20, blank=True)
    second_s = models.CharField(max_length=20, blank=True)
    third_s = models.CharField(max_length=20, blank=True)
    fourth_s = models.CharField(max_length=20, blank=True)
    fifth_s = models.CharField(max_length=20, blank=True)
    sixth_s = models.CharField(max_length=20, blank=True)
    seventh_s = models.CharField(max_length=20, blank=True)
