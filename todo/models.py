from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering= ('id',)
        verbose_name_plural = 'To do'

    def __str__ (self):
        return self.text
