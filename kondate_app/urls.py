from django.urls import path
from .views import StartView, TodayMenuView, MenuCreateView, MenuUpdateView, MenuDeleteView

app_name = 'kondate_app'
urlpatterns = [
    path('', StartView.as_view(), name="start"),
    path('today/', TodayMenuView.as_view(), name="today"),
    path('create/', MenuCreateView.as_view(), name="create"),
    path('update/<int:pk>', MenuUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', MenuDeleteView.as_view(), name="delete"),

]
