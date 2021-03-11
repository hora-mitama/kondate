from django.conf.urls.static import static
from django.urls import path

from kondate import settings
from .views import StartView, RecipeUpdateView, RecipeDeleteView, today_menu_list, recipe_create

app_name = 'kondate_app'
urlpatterns = [
    path('', StartView.as_view(), name="start"),
    path('today/', today_menu_list, name="today"),
    path('create/', recipe_create, name="create"),
    path('update/<int:pk>', RecipeUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', RecipeDeleteView.as_view(), name="delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
