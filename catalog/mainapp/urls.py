from django.urls import path
from .views import ListGoods

urlpatterns = [
    path('', ListGoods.as_view()),
]
