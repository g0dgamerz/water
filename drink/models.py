from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    

# Create your models here.

class Infos(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE,)

    AGE_CHOICES = (
        (0, '5-10'),
        (1, '10-15'),
        (2, '15-20'),
        (3, '20-25'),
        (4,'25-30')
    )
    age = models.IntegerField(max_length=2,choices=AGE_CHOICES)
 

    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'not specified'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    WEIGHT_CHOICES=(
        (0,'less than 35'),
        (1,'35-40'),
        (2,'45-50'),
        (3,'50-60'),
        (3,'60-70'),
        (4,'70-80'),
        (5,'80-90'),
        (6,'90-100'),
        (7,'greater than 100')
    )
    weight = models.IntegerField(choices=WEIGHT_CHOICES)
    HEIGHT_CHOICES=(
        (0,'less than 3 feet'),
        (1,'3-3.5 feet'),
        (2,'3-3.5 feet'),
        (3,'3.6-4 feet'),
        (4,'4-4.5 feet'),
        (5,'4.6-5 feet'),
        (6,'5.1-5.5 feet'),
        (7,'5.6-6 feet'),
        (8,'6.1-6.5 feet'),
        (9,'6.6-7 feet'),
    )
    height=models.IntegerField(choices=HEIGHT_CHOICES)
    
    def __str__(self):
    	return str(self.user)

class Water(models.Model):
    accountholder = models.ForeignKey(User,on_delete=models.CASCADE)
    noofglass = models.IntegerField(default=0)
    date=models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
    	return str(self.accountholder)
