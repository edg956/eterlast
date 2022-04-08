from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404

from nfts.models import NFT, Collection
from nfts.services import NFTService, CollectionService


def get_nft(request: HttpRequest, id: str):
    nft = get_object_or_404(NFT, asset_id=id)
    return JsonResponse(model_to_dict(nft))


def list_nfts(request: HttpRequest):
    queryset = NFT.objects.all().order_by("date_of_creation")
    return JsonResponse([model_to_dict(nft) for nft in queryset], safe=False)


def mint(request: HttpRequest) -> HttpResponse:
    try:
        NFTService.mint(request.POST.dict())
    except Exception as e: # noqa
        return HttpResponse(status=400)

    return HttpResponse(status=201)


def create_collection(request: HttpRequest) -> HttpResponse:
    try:
        CollectionService.create(request.POST.dict())
    except Exception as e:  # noqa
        return HttpResponse(status=400)

    return HttpResponse(status=201)


def list_collections(request: HttpRequest) -> HttpResponse:
    queryset = Collection.objects.all()
    return JsonResponse([model_to_dict(collection) for collection in queryset], safe=False)


def get_collection(request: HttpRequest, id: str) -> HttpResponse:
    collection = get_object_or_404(Collection, id=id)
    return JsonResponse(model_to_dict(collection))
