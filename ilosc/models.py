from django.db import models



class Stat(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    author = models.CharField(max_length=40)

class Word_freq(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User1(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User2(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User3(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User4(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User5(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User6(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User7(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User8(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User9(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()

class User10(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    quantity = models.IntegerField()
