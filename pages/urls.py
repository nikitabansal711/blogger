from django.urls import path
from .views import PageView, AllPages, StatView

app_path = "pages"

urlpatterns = [
    path('page/', PageView.as_view()),
    path('page/<int:pk>', AllPages.as_view()),
    path('pageStat/', StatView.as_view())
]
