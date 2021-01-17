from django.urls import path
from . import views

urlpatterns = [
    path("", views.major_index, name="major_index"),
    path("add_major", views.enter_data_form, name="enter_form"),
    path("<int:pk>/", views.major_detail, name="major_detail"),
]