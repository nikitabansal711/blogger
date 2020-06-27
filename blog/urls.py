from django.urls import path
from .views import PostView, UserView, SignUp,LoginView
from . import views

app_path = "blog"

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', PostView.as_view()),
    path('users/', UserView.as_view()),
    path('getbyname/', views.getByName),
    path('getbytitle/', views.getByTitle),
    path('signup/', SignUp.as_view()),
    path('login/', LoginView.as_view()),
    # path('signup/', views.signup),
 ]