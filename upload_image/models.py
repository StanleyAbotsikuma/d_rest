from django.db import models



class TestUser(models.Model):
  name = models.TextField(max_length=40)
  password = models.TextField(max_length=40)
  randoms = models.CharField(max_length=100)
  upload = models.ImageField(upload_to ='uploads/', default='uploads/xbFIHeh.png')
  

  
