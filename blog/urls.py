from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blogdetail"),
    path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    path('blogedit/<int:pk>', BlogEditView.as_view(), name = "blogedit")
]
