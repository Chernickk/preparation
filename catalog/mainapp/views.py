from django.views.generic import ListView, DetailView
from .models import Good, Partition


class ListGoods(ListView):
    model = Good
    queryset = Good.objects.prefetch_related('partitions')
    extra_context = {'partitions': Partition.objects.all()}


class PartitionView(DetailView):
    model = Partition
    queryset = Partition.objects.all().prefetch_related('goods', 'goods__partitions')
