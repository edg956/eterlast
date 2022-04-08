from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from nfts.models import Collection, NFT
from nfts.services import NFTService, CollectionService

User = get_user_model()


class NftApiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(user="dummy-wallet")
        c = Collection.objects.create(name="default", creator=u)

        cls.user = u
        cls.collection = c

        cls.data = {
            "image": "https://images.url/image.jpg",
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
        nft = NFT.objects.create(**self.data)
        r = self.client.get(f'/nft-api/v1/NFT/{nft.asset_id}')
        self.assertEquals(r.status_code, 200)
        self.assertDictEqual(nft.__dict__, r.data)

    def test_list_nfts_without_nfts(self):
        r = self.client.get(f'/nft-api/v1/NFT/all')
        self.assertEquals(r.status_code, 200)

        self.assertEquals(len(r.data), 0)

    def test_list_nfts(self):
        nft = NFT.objects.create(**self.data)
        r = self.client.get(f'/nft-api/v1/NFT/all')
        self.assertEquals(r.status_code, 200)

        self.assertEquals(len(r.data), 1)
        nft_data = r.data[0]

        self.assertDictEqual(nft.__dict__, nft_data)

