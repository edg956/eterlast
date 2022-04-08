from django.urls import path

from nfts import views

urlpatterns = [
    path('mint', views.mint, name="mint"),
    path('NFT/all', views.list_all, name="list-all-nfts"),
    path('NFT/<id>', views.get, name="get-nft"),
    path('create_collection', views.dummy_view, name="create-collection"),
    path('collection/all', views.dummy_view, name="list-all-collections"),
    path('collection/<id>', views.dummy_view, name="get-collection"),
]
