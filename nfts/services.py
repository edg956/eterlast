from nfts.models import NFT, Collection


class NFTService:
    """Service that handles the use cases that update DB around NFTs"""
    class DuplicateID(Exception):
        pass

    @staticmethod
    def mint(data: dict):
        NFT.objects.create(**data)


class CollectionService:
    """Service that handles the use cases that update DB around Collections"""

    @staticmethod
    def create(data: dict):
        Collection.objects.create(**data)
