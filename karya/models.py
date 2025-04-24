from django.db import models
from django.contrib.auth.models import User

class tasks(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)