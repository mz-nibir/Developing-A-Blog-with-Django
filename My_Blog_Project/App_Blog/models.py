from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_auther')
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="what is your mind?")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    #kon blog er Comment ta jana jabe..(ek e blog er under a onk Comment thakte pare)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    #kon user se Comment ti korese ta jana jabe..(ek user er onek gula Comment thakte pare)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment

class Like(models.Model):
    #kon blog e like poreche ta jana jabe..
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    #kon user blog ti te like diyese ta jana jabe..
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_user')
