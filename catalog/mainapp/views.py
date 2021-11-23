from django.views.generic import ListView
from .models import Good


class ListGoods(ListView):
    model = Good
