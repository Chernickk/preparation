from django.urls import path
from .views import ListGoods, PartitionView

urlpatterns = [
    path('', ListGoods.as_view()),
    path('partition/<int:pk>', PartitionView.as_view())
]
