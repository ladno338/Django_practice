from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    deadline = models.DateTimeField(blank=False)
    ready = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
