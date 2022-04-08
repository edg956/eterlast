from django.urls import path

from nfts import views

urlpatterns = [
    path('mint', views.dummy_view, name="mint"),
    path('NFT/<id>', views.dummy_view, name="get-nft"),
    path('NFT/all', views.dummy_view, name="list-all-nfts"),
    path('create_collection', views.dummy_view, name="create-collection"),
    path('collection/all', views.dummy_view, name="list-all-collections"),
    path('collection/<id>', views.dummy_view, name="get-collection"),
]
