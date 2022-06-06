from django.urls import path
from app1.views import ResultList

urlpatterns = [
    path("list/", ResultList, name="list"),
]