from django.urls import path
from .views import DashBoardAPI

urlpatterns = [
    path('', DashBoardAPI.as_view(), name='')
]