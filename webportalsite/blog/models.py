from django.db import models
from image_cropping import ImageRatioField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              
        return self.title



class BlogEntry(models.Model):
    

    author = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    
    photo = models.ImageField('Photo', upload_to='blog-photos', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    n_comments = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    cropping = ImageRatioField('photo', '430x360')

    def __str__(self):              
        return self.headline


class Comment(models.Model):
    blog_entry = models.ForeignKey(BlogEntry)
    author = models.CharField(verbose_name='Name', max_length=64)
    body_text = models.TextField(verbose_name='Comment')
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body_text




