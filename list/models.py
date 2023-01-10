from django.db import models


# Create your models here.
class TodoListItem(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return str(self.title)
