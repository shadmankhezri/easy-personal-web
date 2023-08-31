from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    detail_address = models.CharField(max_length=50)
    image = models.ImageField(upload_to="project")



    def __str__(self):
        return self.title