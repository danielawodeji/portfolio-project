from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=400)
    pub_date=models.DateTimeField()
    body=models.CharField(max_length=100000)
    Image=models.ImageField(upload_to='images/')
