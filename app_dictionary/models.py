from django.db import models

# Create your models here.

class dictionary_model(models.Model):
    eng_word = models.CharField(max_length=128)
    mal_word = models.CharField(max_length=128)
