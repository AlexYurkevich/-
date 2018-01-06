from django.db import models

class Horse(models.Model):
    nickname = models.CharField(max_length=20)
    number = models.CharField(max_length=5)
    age = models.CharField(max_length=5)
    description = models.CharField(max_length=254)
    image = models.FileField(null=True, blank=True, upload_to='static/images')


    def __unicode__(self):
        dict = {}
        dict['nickname'] = self.nickname
        dict['number'] = self.number
        dict['age'] = self.age
        dict['description'] = self.description
        dict['image'] = self.image
        return dict

class Main(models.Model):
    description = models.CharField(max_length=556)
    image = models.FileField(null=True, blank=True, upload_to='static/images')


    def __unicode__(self):
        dict = {}
        dict['description'] = self.description
        dict['image'] = self.image
        return dict