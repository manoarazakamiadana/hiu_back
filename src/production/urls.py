from django.urls import path
from .views import ProductionView


urlpatterns = [
    path("", ProductionView.as_view())
]

