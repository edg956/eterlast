from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404

from nfts.models import NFT
from nfts.services import NFTService


def get(request: HttpRequest, id: str):
    nft = get_object_or_404(NFT, asset_id=id)
    return JsonResponse(model_to_dict(nft), safe=False, status=200)


def list_all(request: HttpRequest):
    queryset = NFT.objects.all().order_by("date_of_creation")
    return JsonResponse([model_to_dict(nft) for nft in queryset], safe=False, status=200)


def mint(request: HttpRequest) -> HttpResponse:
    try:
        NFTService.mint(request.POST.dict())
    except Exception as e: # noqa
        return HttpResponse(status=400)

    return HttpResponse(status=201)


def dummy_view(request):
    pass
