from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

# Create your models here.
class CatManager(models.Manager):
    def create_cat(self, data, user):
        errors = {}
        if not data['name'] and not data['age']:
            errors['data'] = 'Field cant be empty'
        if len(errors):
            return errors
        else:
            return self.create(name=data['name'], age=data['age'], user=user)
    def update_cat(self, data, cat_id):
        errors = {}
        if not data['name'] or not data['age']:
            errors['data'] = 'Field cant be empty'
        if len(errors):
            return errors
        else:
            return self.filter(id=cat_id).update(name=data['name'], age=data['age'])       

class Cat(models.Model):
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=25)
    user = models.ForeignKey(User, related_name='cats')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = CatManager()


class Like(models.Model):
    cat = models.ForeignKey(Cat, related_name='cat_likes')
    user = models.ForeignKey(User, related_name='user_likes')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
