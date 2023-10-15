from django.db import models
from datetime import date
from ckeditor.fields import RichTextField



class Playlist(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(blank=True)
    img = models.URLField()
    

    def __str__(self):
        return self.name



class AddBlog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    category = models.CharField(max_length=200, blank=True)
    sub_category = models.CharField(max_length=200, blank=True)

    content = RichTextField()
    author= models.CharField(max_length=150, default="Coding India")
    readtime = models.IntegerField()
    tags = models.CharField(max_length=150)
    # dexc = models.TextField()
    play = models.ForeignKey(Playlist, on_delete=models.CASCADE)


    def __str__(self):  
        return self.title
    

