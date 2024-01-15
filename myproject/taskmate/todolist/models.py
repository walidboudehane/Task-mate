from django.db import models

class Task(models.Model):
    task=models.CharField(max_length=200)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.task + '-'+str(self.done)
class Person(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    