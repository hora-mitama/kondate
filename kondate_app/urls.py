from django.urls import path
from .views import StartView, MenuUpdateView, MenuDeleteView, today_list, create

app_name = 'kondate_app'
urlpatterns = [
    path('', StartView.as_view(), name="start"),
    path('today/', today_list, name="today"),
    path('create/', create, name="create"),
    path('update/<int:pk>', MenuUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', MenuDeleteView.as_view(), name="delete"),

]
