from django.urls import path

from accounts.views import AuthorCreate, add_author
from .views import subscribe
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, PostDelete, PostUpdate, PostCreate, CategoryListView

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', NewsDetail.as_view(), name='new'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('author/<int:pk>', AuthorCreate.as_view(), name='author'),
    # path('author/<int:pk>/subcr', add_author, name='add_author'),

]
