import json

from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from users.models import User
from users.services import UserService


@require_http_methods(["GET"])
def get_user(request: HttpRequest, id: str):
    nft = get_object_or_404(User, user=id)
    return JsonResponse(model_to_dict(nft, fields=["user"]))


@require_http_methods(["GET"])
def list_users(request: HttpRequest):
    queryset = User.objects.all()
    return JsonResponse([model_to_dict(nft, fields=["user"]) for nft in queryset], safe=False)


@require_http_methods(["POST"])
def create(request: HttpRequest) -> HttpResponse:
    try:
        UserService.create(json.loads(request.body))
    except Exception as e: # noqa
        return HttpResponse(status=400)

    return HttpResponse(status=201)
