from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Lead(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Names = models.CharField(max_length=100, blank=False)
    Email = models.EmailField(blank=False)
    DNI = models.PositiveIntegerField(blank=False, validators=[MaxValueValidator(99999999)])
    Phone = models.PositiveIntegerField(blank=False, validators=[MaxValueValidator(999999999)])

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.Names, self.Email, self.DNI, self.Phone)