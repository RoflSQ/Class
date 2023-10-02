from django.urls import path
from .views import view_list, view_list_class, sign_up

urlpatterns = [
    path('sub', view_list),
    path('', view_list_class, name='home'),
    path('signup', sign_up, name='signup')
]
