from argparse import MetavarTypeHelpFormatter
from django.db import models

from account.models import User

class Center(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    code = models.CharField(max_length=12)
    homepage = models.CharField(max_length=150)
    telephone = models.CharField(max_length=16)

    class Meta:
        db_table = "center"

class CenterUser(models.Model):
    center_id = models.ForeignKey('Center', on_delete=models.CASCADE, db_column="center_id")
    username = models.ForeignKey(User, on_delete=models.CASCADE, db_column="username", to_field="username")

    class Meta:
        db_table = "center_user"