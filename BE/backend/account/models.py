from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=300)

    class Meta:
        db_table = 'user'