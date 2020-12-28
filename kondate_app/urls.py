from django.urls import path
from .views import IndexView

app_name = 'kondate_app'
urlpatterns = [
    path('', IndexView.as_view(), name="start")
]