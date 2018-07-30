from django.db import models
from django.contrib.auth.models import User
 
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='user', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, blank=True, default='e.g Accountant')
    phone = models.CharField(max_length=20, blank=True, default='')
    teams = models.ManyToManyField('divisions.Team', related_name='user_teams', blank = True)
    section = models.ForeignKey('divisions.Section', related_name='user_section', on_delete=models.PROTECT, blank = True, null = True)
    subsection = models.ForeignKey('divisions.SubSection', related_name='user_subsection', on_delete=models.PROTECT, blank = True, null = True)
    status = models.CharField(max_length=100, blank=True, null=True, default='Mood? :)')
    about = models.TextField(default='Who are you?', blank=True)