from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):#
	tagName=models.CharField(max_length=20)
	createTime=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.tagName
class Classification(models.Model):
	name=models.CharField(max_length=40)
	def __unicode__(self):
		return self.name
class Author(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(blank=True)
	website=models.URLField(blank=True)
	def __unicode__(self):
		return u'%s'%(self.name)
class Artical(models.Model):
	caption =models.CharField(max_length=30)
	subcaption =models.CharField(max_length=50,blank=True)
	publishTime=models.DateTimeField(auto_now_add=True)
	updateTime=models.DateTimeField(auto_now=True)
	author=models.ForeignKey(Author)
	classification=models.ForeignKey(Classification)
	tags=models.ManyToManyField(Tag,blank=True)
	content=models.TextField()
	summary=models.CharField(max_length=300,blank=True)
	views=models.IntegerField(default=0)
	likes=models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s'%(self.caption)
# class Comments(models.Model):
# 	artical=models.ForeignKey(Artical)
# 	content=models.TextField()
# 	commentor=models.ForeignKey(User)
# 	commentTime=models.DateTimeField(auto_now_add=True)
# 	updateTime=models.DateTimeField(auto_now=True)
# class Replys(models.Model):
# 	comment=models.ForeignKey(Comments)
# 	content=models.TextField()
# 	replyTime=models.DateTimeField(auto_now_add=True)
# 	updateTime=models.DateTimeField(auto_now=True)
# 	replyer=models.ForeignKey(User)
class UserProfile(models.Model):
	website=models.URLField()
	picture=models.ImageField(upload_to='profile_images',blank=True)
	user=models.OneToOneField(User)
	def __unicode__(self):
		return self.user.username
