from django.db import models

# Create your models here.

class ReactJs(models.Model):
    name = models.CharField(max_length=200)
    uses = models.IntegerField()
    

    def __str__(self):
        return "{}-{}".format(self.name, self.uses)
    
    def Percentages(self):
        return f"{self.uses} %"

class Django(models.Model):
    djangoname = models.CharField(max_length=200)
    use = models.IntegerField(default=0)
    

    def __str__(self):
        return "{}-{}".format(self.djangoname, self.use)
    

class Salary(models.Model):
    salary = models.CharField(max_length=200)
    use = models.IntegerField(default=0)
    

    def __str__(self):
        return "{}-{}".format(self.salary, self.use)
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()


    

class Registerfr(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)

