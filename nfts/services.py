from django.contrib.auth import get_user_model

from nfts.models import NFT, Collection


User = get_user_model()


class NFTService:
    """Service that handles the use cases that update DB around NFTs"""
    @staticmethod
    def mint(data: dict):
        data["collection"] = Collection.objects.get(id=data["collection"])
        NFT.objects.create(**data)


class CollectionService:
    """Service that handles the use cases that update DB around Collections"""

    @staticmethod
    def create(data: dict):
        data["creator"] = User.objects.get(user=data["creator"])
        Collection.objects.create(**data)
