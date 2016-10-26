from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    phone = PhoneNumberField(blank=False)
    address = models.CharField(max_length=200)
    birthday = models.DateField(blank=False)
    description = models.TextField(max_length=300)

    class Meta:
        ordering = ['name']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Preference(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    photo = models.ImageField()


class Game(models.Model):
    name = models.CharField(max_length=200)
    preferences = models.ManyToManyField(Preference, through='UserPrefGame')


class UserPrefGame(models.Model):
    preference = models.ForeignKey(Preference, primary_key=True)
    game = models.ForeignKey(Game, primary_key=True)
    order = models.IntegerField()
