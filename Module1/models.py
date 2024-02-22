from django import forms
from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveBigIntegerField()

    class Meta:
        db_table = "Register"


class contactus(models.Model):
    firstname = models.TextField(max_length=100)
    lastname = models.TextField(max_length=100)
    email = models.EmailField(primary_key=True)
    comment = models.TextField(max_length=255)

    class Meta:
        db_table = "contactus"


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')
