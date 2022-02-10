from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word


class Check(models.Model):
    w_word = models.CharField(max_length=20)
    word_id = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self):
        return self.w_word