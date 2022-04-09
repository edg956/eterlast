from django.db import models


class User(models.Model):
    user = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return str(self.user)
