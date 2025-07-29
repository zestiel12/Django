from django.urls import path

from .views import news_list,news_detail


urlpatterns = [
    path('',news_list,name="news-list"),
    path('<int:id>',news_detail,name="news-detail"),
    # path('category/<str:str>/',news_by_category, name='news-by-categories'),
    ]