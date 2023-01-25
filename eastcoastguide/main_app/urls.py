from django.urls import path
from . import views

urlpatterns = [    
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('NY/', views.RestaurantsNYIndex.as_view(), name='ny_restaurants'),
    path('MA/', views.RestaurantsMAIndex.as_view(), name='ma_restaurants'),
    path('restaurants/<int:restaurant_id>/', views.RestaurantDetail.as_view(), name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('comments/create/', views.CommentCreate.as_view(), name='comments_create')                                      
]