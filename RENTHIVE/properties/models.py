from django.db import models


class Property(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    address = models.TextField()
    county = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)

    def __str__(self):
        return self.address
