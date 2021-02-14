from django.db import models

# Create your models here.
class Technologies(models.Model):
    TechnologyUsed = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.TechnologyUsed

class Student(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    workupdate = models.CharField(max_length=800)
    githublink = models.CharField(max_length=200)
    #technologiesUsed = models.CharField(max_length=200, default="")
    #technologiesUsed = models.OneToManyField('', related_name='order', blank=True)
    technologiesUsed = models.ManyToManyField('Technologies', related_name='entry')
    image1 = models.ImageField(upload_to="student/images", default="")
    image2 = models.ImageField(upload_to="student/images", default="")
    image3 = models.ImageField(upload_to="student/images", default="")
    image4 = models.ImageField(upload_to="student/images", default="")
    # image5 = models.ImageField(upload_to="student/images", default="")

    def __str__(self):
        return self.name
