from django.db import models

# Create your models here.

class Contactus(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='Name')
    email = models.CharField(max_length=200, blank=False, verbose_name='Email')
    phone = models.CharField(max_length=12,null=False,blank=False,verbose_name='phone')
    org = models.CharField(max_length=200, blank=True, verbose_name='org',null=True)


    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = "Contact us"
    #     verbose_name_plural = "Contact us"
