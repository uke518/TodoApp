from django.db import models

# Create your models here.


class TodoModel(models.Model):
    # idとユーザーも追加
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
