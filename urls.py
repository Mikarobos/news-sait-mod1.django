from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView, category_list, article_list

urlpatterns = [
    path("", views.index, name='index'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('calculator_risk/', views.calculator_risk, name='calculator_risk'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', article_list, name='article_list'),
]