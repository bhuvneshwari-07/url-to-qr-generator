from django.db import models

class QRCodeData(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    qr_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
