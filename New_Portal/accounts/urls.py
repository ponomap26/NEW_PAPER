from django.urls import path
from .views import SignUp, AuthorCreate

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    # path('author/', AuthorCreate.as_view(), name='add_author'),
]