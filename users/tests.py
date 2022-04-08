from django.test import TestCase

from users.models import User


class UserApiTestCase(TestCase):
    def test_create_happy_path(self):
        r = self.client.post('/nft-api/v1/create_user', {"user": "user_wallet"})

        self.assertEquals(r.status_code, 201)

        users = User.objects.all()
        self.assertEquals(1, len(users))

        user = users[0]
        self.assertEquals(user.user, "user_wallet")

    def test_get_user(self):
        user = User.objects.create(user="user_wallet")
        r = self.client.get('/nft-api/v1/user/user_wallet')

        self.assertEquals(r.status_code, 200)

        data = r.json()

        self.assertEquals(user.user, data["user"])

    def test_list_users_without_users(self):
        r = self.client.get('/nft-api/v1/user/all')
        self.assertEquals(r.status_code, 200)

        data = r.json()

        self.assertEquals(len(data), 0)

    def test_list_users(self):
        user = User.objects.create(user="user_wallet")
        r = self.client.get('/nft-api/v1/user/all')
        self.assertEquals(r.status_code, 200)
        data = r.json()
        self.assertEquals(len(data), 1)
        user_data = data[0]

        self.assertEquals(user.user, user_data["user"])
