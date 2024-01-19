from django.core.paginator import Paginator
from django.shortcuts import render
from django_app import models


def render_index(request):
    return render(request, 'index.html')


def get_services(request):
    selected_page = request.GET.get(key='page', default=1)
    ans = models.Price.objects.all()
    page_objs = Paginator(object_list=ans, per_page=30)

    page_obj = page_objs.page(number=selected_page)

    return render(request, 'services.html', context={"page_obj": page_obj})
