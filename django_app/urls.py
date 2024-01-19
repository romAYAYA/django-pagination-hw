from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.render_index, name='index'),
    path("get_services/", views.get_services, name="get_services"),
]
