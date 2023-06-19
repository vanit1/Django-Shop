from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsList.as_view(), name='home'),
    path('category/<slug:cat_slug>', views.CategoryList.as_view(), name='category'),
    path('product/<slug:product_slug>', views.ProductDetail.as_view(), name='product'),
    path('logout/', views.logout_user, name='logout'),
    path('user_accounts/', views.Accounts.as_view(), name='accs'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginUs.as_view(), name='login'),
]