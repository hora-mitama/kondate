from django.urls import path
from .views import StartView, IndexView,MenuList

app_name = 'kondate_app'
urlpatterns = [
    path('', StartView.as_view(), name="start"),
    path('index/', IndexView.as_view(), name="index"),
    path('list/', MenuList.as_view(), name="list"),
]
