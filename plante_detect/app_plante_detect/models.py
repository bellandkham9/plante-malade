from django.db import models

# Create your models here.
from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    predicted_class = models.CharField(max_length=100)
    predicted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.predicted_class} - {self.predicted_at.strftime('%Y-%m-%d %H:%M')}"
