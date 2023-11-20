from django.urls import path
from .views import view_list, view_list_class, sign_up
from django.conf import settings
urlpatterns = [
    path('', view_list_class, name='home'),
]

