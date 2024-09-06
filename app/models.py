from django.db import models


class list(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(blank=False, null=False, max_length=100)
    Create_At=models.DateTimeField(auto_now_add=True, blank=False, null=False)
    Description=models.CharField(blank=False, null=False, max_length=500)
    Deadline=models.IntegerField(blank=False, null=False)
    Finished_At=models.DateTimeField(auto_now=False)

    