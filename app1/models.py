from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django_jalali.db import models as jmodels#تاریخ جلالی

# Create your models here.

class Profile(models.Model):
    GENDER = [
        ('m', 'مرد'),
        ('w', 'زن'),
    ]

    MARITAL = [
        ('m', 'متاهل'),
        ('s', 'مجرد'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField('ایمیل')
    first_name = models.CharField('نام', max_length=200)
    last_name = models.CharField('نام خانوادگی', max_length=200)
    national_code = models.CharField('کد ملی', max_length=200)
    date_birth = jmodels.jDateField('تاریخ تولد')
    gender = models.CharField('جنسیت', max_length=1, choices=GENDER)
    marital = models.CharField('وضعیت تاهل', max_length=1, choices=MARITAL)
    address = models.TextField('آدرس')
    mobile = models.CharField('موبایل', max_length=15)
    picture = models.ImageField('عکس', null=True, blank=True)
    father_name = models.CharField('نام پدر', max_length=200)

    def __str__(self):
        return (self.user.username)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'پروفایل افراد'


class Hamkari(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    darman = models.BooleanField('بهداشتی و درمانی')
    sakht = models.BooleanField('ساخت و ساز')
    amoozesh = models.BooleanField('آموزشی')
    farhangi = models.BooleanField('فرهنگی')
    daroo = models.BooleanField('دارو')
    lebas = models.BooleanField('لباس')
    ghaza = models.BooleanField('غذا')
    tahrir = models.BooleanField('لوازم التحریر')
    masaleh = models.BooleanField('مصالح')
    naghdi_mostaghim = models.BooleanField('پرداخت نقدی لحظه ای')
    naghdi_ghest = models.BooleanField('پرداخت قسطی')

    def __str__(self):
        return (self.profile.user.username)

    class Meta:
        verbose_name = 'hamkari'
        verbose_name_plural = ' لیست همکاری'


class Hamkari_code(models.Model):
    national_code = models.CharField('کد ملی', max_length=200)
    darman = models.BooleanField('بهداشتی و درمانی')
    sakht = models.BooleanField('ساخت و ساز')
    amoozesh = models.BooleanField('آموزشی')
    farhangi = models.BooleanField('فرهنگی')
    daroo = models.BooleanField('دارو')
    lebas = models.BooleanField('لباس')
    ghaza = models.BooleanField('غذا')
    tahrir = models.BooleanField('لوازم التحریر')
    masaleh = models.BooleanField('مصالح')
    naghdi_mostaghim = models.BooleanField('پرداخت نقدی لحظه ای')
    naghdi_ghest = models.BooleanField('پرداخت قسطی')

    def __str__(self):
        return (self.national_code)

    class Meta:
        verbose_name = 'hamkari_code'
        verbose_name_plural = ' لیست همکاری با کد ملی'


class Farakhan(models.Model):
    HAMKARI = [
        ('n', 'نقدی'),
        ('k', 'خدماتی'),
        ('e', 'اجناس اهدایی'),
    ]

    date_first = jmodels.jDateField('تاریخ شروع')
    date_end = jmodels.jDateField('تاریخ پایان')
    place = models.CharField('مکان فراخوان', max_length=200)
    farakhan_title = models.TextField('تیتر فراخوان')
    farakhan_content = models.TextField('متن فراخوان')
    hamkari_type = models.CharField('نوع همکاری', max_length=1, choices=HAMKARI)

    def __str__(self):
        return (self.farakhan_title)

    class Meta:
        verbose_name = 'farakhan'
        verbose_name_plural = ' لیست فراخوان'


class Profile_ready(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    farakhan = models.ForeignKey(Farakhan, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'profile_ready'
        verbose_name_plural = ' لیست افراد آماده در فراخوان'


class Profile_present(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    farakhan = models.ForeignKey(Farakhan, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'profile_present'
        verbose_name_plural = ' لیست افراد حاضر در فراخوان'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    date = jmodels.jDateField()

