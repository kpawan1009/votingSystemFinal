from django.db import models
import os
from twilio.rest import Client


class Candidateaura(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    party=models.CharField(max_length=30)
    constituency=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Candidatepalg(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    party=models.CharField(max_length=30)
    constituency=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Votergovt(models.Model):
    name=models.CharField(max_length=40)
    pannumber=models.CharField(max_length=10)
    constituency=models.CharField(max_length=40)
    age=models.IntegerField(default=18)

    def __str__(self):
        return self.name

class Voterregisteredpalghar(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    pannumber=models.CharField(max_length=10)
    email=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Voterregisteredamroha(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    pannumber=models.CharField(max_length=10)
    email=models.CharField(max_length=40)

    def __str__(self):
        return self.name



class UIDamroha(models.Model):
    pannumber=models.CharField(max_length=10)
    uniqueid=models.CharField(max_length=10)
    # phonenumber=models.IntegerField(max_length=15)

    def __str__(self):
        return self.uniqueid


class UIDpalghar(models.Model):
    pannumber=models.CharField(max_length=10)
    uniqueid=models.CharField(max_length=10)
    # phonenumber = models.IntegerField(max_length=15)
    def __str__(self):
        return self.uniqueid

class Feedback(models.Model):
    name2 = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    feedback=models.TextField()

    def __str__(self):
        return self.name2