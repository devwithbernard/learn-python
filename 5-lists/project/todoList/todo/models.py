from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'<Todo({self.title}, {self.completed}, {self.created_at}, {self.updated_at})>'
