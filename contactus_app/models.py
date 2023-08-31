from django.db import models

# Create your models here.


class Footer(models.Model):
    country_state = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    facebook = models.CharField(max_length=50)
    insta = models.CharField(max_length=50)
    twiter = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)



class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.name