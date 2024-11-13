from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,Created=False,**kwargs):
    if Created:
        Token.objects.create(user=instance)
<<<<<<< HEAD
# Create your wonderful models here.

=======
# Create your models here.
#models
>>>>>>> 31551434ded65a8def326cb5fb1ff11f396abffe
class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.DepartmentName
class Employee(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=200)
    Designation =models.CharField(max_length=150)
    DataJoining=models.DateField()
    DepartmentId=models.ForeignKey(Department,on_delete=models.CASCADE)
    Contact=models.CharField(max_length=150)
    ISActive=models.BooleanField(default=True)
    def __str__(self):
        return self.EmployeeName
    


