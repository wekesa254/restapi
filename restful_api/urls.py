
from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView
from . import views

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:pk>/', ArticleDetails.as_view()),
    #path('Show', views.article_list, name='article_list'),
    path('', views.display_data),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

]