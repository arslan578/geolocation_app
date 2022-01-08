from django.db import models

# Create your models here.
STATUS = (
    ('0', 'Pending'),
    ('1', 'Approve'),
    ('2', 'Decline')
)


class GeoLocation(models.Model):
    username = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.username, self.latitude, self.longitude)