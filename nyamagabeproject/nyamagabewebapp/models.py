from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxLengthValidator
# Create your models here.
class services(models.Model):
    choice=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ]

    Day=[('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ]
    id=models.AutoField(primary_key=True)   
    picture =models.ImageField(null=True, upload_to='photoes')
    title = models.CharField(max_length=100, blank=True, null=False)
    description = models.TextField(max_length=380, blank=True, null=False)
    director_name=models.CharField(max_length=10, blank=True, null=False)
    director_position = models.CharField(max_length=100, blank=True, null=False)
    gender=models.CharField(max_length=10, choices=choice )
    twiterprofilelink=models.URLField(null=False)
    facebookprofilelink=models.URLField(null=False)
    instagramprofilelink=models.URLField(null=False)
    email=models.EmailField()
    phone=models.IntegerField()
    time =MultiSelectField(validators=[MaxLengthValidator(6)], choices=Day)
