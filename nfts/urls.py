from django.urls import path

from nfts import views

urlpatterns = [
    path('mint', views.mint, name="mint"),
    path('NFT/all', views.list_nfts, name="list-all-nfts"),
    path('NFT/<id>', views.get_nft, name="get-nft"),
    path('create_collection', views.create_collection, name="create-collection"),
    path('collection/all', views.list_collections, name="list-all-collections"),
    path('collection/<id>', views.get_collection, name="get-collection"),
]
