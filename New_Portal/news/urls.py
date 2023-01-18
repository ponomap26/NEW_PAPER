from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, PostDelete, PostUpdate, PostCreate


urlpatterns = [
    path('', NewsList.as_view(), name ='news'),
    path('<int:pk>', NewsDetail.as_view(), name='new'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),

]
