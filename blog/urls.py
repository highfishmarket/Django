from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index)
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.Postdetail.as_view())
]