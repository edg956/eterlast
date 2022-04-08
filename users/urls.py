from django.urls import path

from users import views

urlpatterns = [
    path('create_user', views.create, name="create-user"),
    path('user/all', views.list_users, name="list-all-users"),
    path('user/<id>', views.get_user, name="get-user"),
]
