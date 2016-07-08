from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

import numpy as np

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	company = models.CharField(max_length=100,blank=True,null=True)
	location = models.CharField(max_length=250,blank=True)
	type = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=200, default="https://github.com/personal")
    owner_id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    language = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField('date created')
#   forked_from = models.ForeignKey(Project, on_delete=models.CASCADE)
    updated_at = models.DateTimeField('date updated',blank=True,null=True)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    repo = models.ForeignKey(Project, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
""" 
 def __unicode__(self):
        return self.id
    def __str__(self):  
        return "%s commented on %s on %s" % (self.user_name, self.repo_name, self.pub_date)
"""
		
"""
class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])

		
		
"""