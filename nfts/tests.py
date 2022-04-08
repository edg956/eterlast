from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from nfts.models import Collection, NFT

User = get_user_model()


class NftApiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(user="dummy-wallet")
        c = Collection.objects.create(name="default", creator=u)

        cls.user = u
        cls.collection = c

        cls.data = {
            "picture": "https://images.url/image.jpg",
            "asset_id": "the asset id",
            "external_link": "https://openocean.io/the-asset-id",
            "description": "Dummy description",
            "collection": str(c.id),
            "supply": 14,
            "royalties": 1,
            "buyer": "the-buyers-wallet-addr"
        }

        cls.client = Client()

    def test_mint_creates_nft(self):
        r = self.client.post('/nft-api/v1/mint', self.data)

        self.assertEquals(r.status_code, 201)

        nfts = NFT.objects.all()
        self.assertEquals(1, len(nfts))

        nft = nfts[0]
        self.assertEquals(nft.asset_id, self.data["asset_id"])

        self.assertEquals(nft.collection, self.collection)

    def test_get_nft(self):
        nft = NFT.objects.create(**{**self.data, "collection": self.collection})
        r = self.client.get(f'/nft-api/v1/NFT/{nft.asset_id}')
        self.assertEquals(r.status_code, 200)

        data = r.json()

        self.assertEquals(nft.asset_id, data["asset_id"])

    def test_list_nfts_without_nfts(self):
        r = self.client.get(f'/nft-api/v1/NFT/all')
        self.assertEquals(r.status_code, 200)

        data = r.json()

        self.assertEquals(len(data), 0)

    def test_list_nfts(self):
        nft = NFT.objects.create(**{**self.data, "collection": self.collection})
        r = self.client.get(f'/nft-api/v1/NFT/all')
        self.assertEquals(r.status_code, 200)
        data = r.json()
        self.assertEquals(len(data), 1)
        nft_data = data[0]

        self.assertEquals(nft.asset_id, nft_data["asset_id"])


class CollectionApiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(user="dummy-wallet")

        cls.user = u

        cls.data = {
            "name": "The Collection",
            "creator": u,
            "creator_network": "user_wallet"        # TODO: what's user_wallet?
        }

        cls.client = Client()

    def test_create_collection_does_what_it_should(self):
        r = self.client.post('/nft-api/v1/create_collection', self.data)

        self.assertEquals(r.status_code, 201)

        collections = Collection.objects.all()
        self.assertEquals(1, len(collections))

        collection = collections[0]
        self.assertEquals(collection.name, self.data["name"])

        self.assertEquals(collection.creator, self.user)

    def test_get_collection(self):
        collection = Collection.objects.create(**self.data)
        r = self.client.get(f'/nft-api/v1/collection/{collection.id}')
        self.assertEquals(r.status_code, 200)

        data = r.json()

        self.assertEquals(str(collection.id), data["id"])

    def test_list_collections_without_collections(self):
        r = self.client.get(f'/nft-api/v1/collection/all')
        self.assertEquals(r.status_code, 200)

        data = r.json()

        self.assertEquals(len(data), 0)

    def test_list_collections(self):
        collection = Collection.objects.create(**self.data)

        r = self.client.get(f'/nft-api/v1/collection/all')

        self.assertEquals(r.status_code, 200)
        data = r.json()
        self.assertEquals(len(data), 1)
        data = data[0]

        self.assertEquals(str(collection.id), data["id"])
