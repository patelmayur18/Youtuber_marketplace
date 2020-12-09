from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name= models.CharField(max_length=50)        
    last_name= models.CharField(max_length=50)        
    role= models.CharField(max_length=50,null=True)        
    facebook_link= models.CharField(max_length=50)        
    linkedin_link= models.CharField(max_length=50)       
    created_date = models.DateTimeField(auto_now_add=True,null=True) 
    photo = models.ImageField(upload_to='media/team/%Y/')

    def __str__(self):
        return self.first_name


class Youtuber(models.Model):
    crew_choice=(
        ('solo','solo'),
        ('small','small'),
        ('large','large')
    )

    camera_choice=(
        ('canon','canon'),
        ('sony','sony'),
        ('red','red'),
        ('nikon','nikon'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('other','other')
    )

    category_choice=(
        ('mobile_review','mobile_review'),
        ('cooking','cooking'),
        ('vloging','vloging'),
        ('gaming','gaming'),
        ('film','film'),
        ('comady','comady'),
        ('review','review')
    )


    name = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/')
    video_url = models.CharField(max_length=250)        
    discription = RichTextField()       
    age = models.IntegerField()       
    hight = models.IntegerField()  
    crew = models.CharField(choices=crew_choice, max_length=250)
    camera_type = models.CharField(choices=camera_choice,max_length=250)
    subs_count = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    category = models.CharField(choices=category_choice,max_length=250)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
