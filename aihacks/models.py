from django.db import models

# Create your models here.
# Verification Code
#MSP University
#Event Name
#Attendee First Name
#Attendee University Name

class Detail(models.Model):
    Verification_Code = models.CharField(max_length=200, blank=True,
        null=True)
    MSP_University = models.CharField(max_length=200, blank=True,
        null=True)
    Event_Name = models.CharField(max_length=200, blank=True,
        null=True)
    Email = models.EmailField(max_length=200,default = "", blank=True,
        null=True)
    Attendee_First_Name = models.CharField(max_length=200, blank=True,
        null=True)
    Attendee_University_Name = models.CharField(max_length=200, blank=True,
        null=True)
    def __str__(self):
        return str(self.Email) if self.Email else ''
        


