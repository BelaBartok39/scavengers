from django.contrib.auth import get_user_model
from django.db import models

def treasure_image_path(instance, filename):
    # Define the path where the treasure images will be uploaded
    return f'treasure_images/user_{instance.user.id}/{filename}'

class Treasure(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    hints = models.TextField(default='')
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255,null=True)
    zipcode = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to=treasure_image_path, null=True)  # Add the image field

    def __str__(self):
        return self.name
