from django.db import models

# Create your models here.
class company(models.Model):
    name=models.CharField(max_length=25)
    location=models.CharField(max_length=50)
    desc=models.TextField()
    type=models.CharField(max_length=199,choices=(("It","It"),("non it","non it")))
    add_time=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name + " --"+self.location
    
    
    
class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    position=models.CharField(max_length=50,choices=(("manager","manager")
                                      ,("software developer","software developer"),
                                                     ("leader","leader")))
    
    company=models.ForeignKey(company,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name