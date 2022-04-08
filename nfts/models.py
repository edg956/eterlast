import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_network = models.TextField()


class NFT(models.Model):
    asset_id = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to="nft_pictures")
    external_link = models.URLField()
    description = models.TextField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    supply = models.IntegerField()
    royalties = models.IntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    buyer = models.TextField()
