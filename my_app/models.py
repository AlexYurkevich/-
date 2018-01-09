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

'''
class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __unicode__(self):
        dict = {}
        dict['login'] = self.login
        dict['password'] = self.password
        dict['email'] = self.email
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        return dict
'''