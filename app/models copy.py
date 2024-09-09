from django.db import models


class TimeScale(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class list(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(blank=False, null=False, max_length=100, verbose_name="Nome")
    Create_At=models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name="Criado em")
    Description=models.CharField(blank=False, null=False, max_length=500, verbose_name="Descrição")
    Deadline=models.IntegerField(blank=False, null=False, verbose_name="Prazo de")
    TimeScale = models.ForeignKey(TimeScale, on_delete=models.PROTECT, related_name='list_TimeScale')
    Finished_At=models.DateTimeField(auto_now=False)

    def __str__(self) -> str:
        return self.model

    