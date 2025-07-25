from django.db import models
import string
import random


# Create your models here.
def generate_short_code():
    "Generates a unique short code of 6 characters"
    length = 6
    chars = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(chars) for _ in range(length))

        if not Link.objects.filter(short_code = short_code).exists():
            return short_code
        
    
class Link(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        #Generates a short code if one isn't provided
        if not self.short_code:
            self.short_code = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"