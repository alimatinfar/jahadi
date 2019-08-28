from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    GENDER = [
        ('m', 'man'),
        ('w', 'woman'),
    ]

    MARITAL = [
        ('m', 'married'),
        ('s', 'single'),
    ]

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_code = models.CharField(max_length=200)
    date_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    picture = models.ImageField(null=True, blank=True)
    father_name = models.CharField(max_length=200)

    def __str__(self):
        return (self.user.username)


class Hamkari(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    darman = models.BooleanField()
    sakht = models.BooleanField()
    amoozesh = models.BooleanField()
    farhangi = models.BooleanField()
    daroo = models.BooleanField()
    lebas = models.BooleanField()
    ghaza = models.BooleanField()
    tahrir = models.BooleanField()
    masaleh = models.BooleanField()
    naghdi_mostaghim = models.BooleanField()
    naghdi_ghest = models.BooleanField()


class Farakhan(models.Model):
    HAMKARI = [
        ('n', 'naghdi'),
        ('k', 'khadamat'),
        ('e', 'ehda'),
    ]


    title = models.CharField(max_length=200)
    date_first = models.DateField()
    date_end = models.DateField()
    place = models.CharField(max_length=200)
    hamkari_title = models.CharField(max_length=400)
    kamkari_type = models.CharField(max_length=1, choices=HAMKARI)
