from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page, name='category'),
    path('article/<int:article_id>/', article_detail, name='article'),
    path('add_article/', add_article, name='add_article'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('search/', search_results, name='search'),
    path('about_dev/', about_dev, name='about_dev'),
    path('about_us/', about_us, name='about_us'),
    path('article_update/<int:id>/', article_edit, name='update'),
    # path('save_comment/<int:pk>/', save_comment, name='save_comment'),
    path('delete/<int:id>/', delete_article, name='delete')
]
