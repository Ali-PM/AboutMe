from django.db import models


# Create your models here.
class ContactUs(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()

    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)


class MassageMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'