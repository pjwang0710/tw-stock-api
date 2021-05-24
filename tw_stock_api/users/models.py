from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, null=False)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    hashed_password = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class UserSecretKeys(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    year = models.IntegerField()
    month = models.IntegerField()
    count = models.IntegerField()
    is_charged = models.BooleanField()

    def __str__(self):
        return self.user_id
