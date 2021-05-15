from django.urls import path
from .views import *

urlpatterns = [
    path('', questions, name='base'),
    path('thanks/', ThanksView.as_view(), name='thanks')
]