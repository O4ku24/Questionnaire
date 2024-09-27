from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=30)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class Questions(models.Model):
    question = models.CharField(max_length=100)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)