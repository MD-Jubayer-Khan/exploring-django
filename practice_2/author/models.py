from django.db import models

# Create your models here.
class Author(models.Model):
    # comment = models.TextField()
    # email = models.EmailField()
    # agree = models.BooleanField()
    birth_date = models.DateField()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name