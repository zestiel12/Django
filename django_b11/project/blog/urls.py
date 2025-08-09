from django.urls import path

from .views import news_list,news_detail,news_by_category,creat_news,creat_category,creat_tag,change_news,change_category,change_tag,change_img,images_all


urlpatterns = [
    path('',news_list,name="news-list"),
    path('<int:id>',news_detail,name="news-detail"),
    path('category/<int:category_id>/',news_by_category, name='news-by-categories'),
    path('create/',creat_news,name="create-news"),
    path('creat_category/', creat_category, name='creat-category'),
    path('creat_tag/', creat_tag, name='creat-tag'),
    path('change/<int:id>',change_news,name="change-news"),
    path('change_cat/<int:category_id>', change_category ,name="change-category"),
    path('change_tag/',change_tag,name="change-tag"),
    path('change_img/<int:img_id>',change_img,name="change-img"),
    path('images/',images_all,name="images-all")
    ]
