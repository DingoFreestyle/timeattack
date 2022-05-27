from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=256, null=False)
# Create your models here.
