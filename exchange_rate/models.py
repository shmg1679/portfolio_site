from django.db import models

# Create your models here.
# the models or options will be what you're able to do in 
# local host admin http://127.0.0.1:8000/admin/ such as title,description, etc.
class exchange_rate(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title