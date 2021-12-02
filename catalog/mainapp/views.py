from django.views.generic import ListView, DetailView
from .models import Good, Partition


class ListGoods(ListView):
    model = Good
    queryset = Good.on_site.prefetch_related('partitions')
    extra_context = {'partitions': Partition.on_site.all()}


class PartitionView(DetailView):
    model = Partition
    queryset = Partition.on_site.all().prefetch_related('goods', 'goods__partitions')
