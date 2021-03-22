from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Signup(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    Cn_password = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video%y")

    def __str__(self):
        return self.caption


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name
