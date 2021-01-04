from django.urls import path
from .views import StartView, IndexView

app_name = 'kondate_app'
urlpatterns = [
    path('', StartView.as_view(), name="start"),
    path('index/', IndexView.as_view(), name="index")
]