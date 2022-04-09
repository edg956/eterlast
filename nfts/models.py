import uuid

from django.db import models
from users.models import User


class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_network = models.TextField()


class NFT(models.Model):
    asset_id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=128)
    picture = models.URLField()
    external_link = models.URLField()
    description = models.TextField(null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    supply = models.IntegerField()
    royalties = models.IntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    buyer = models.TextField(null=True, blank=True)
