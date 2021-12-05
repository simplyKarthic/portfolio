
from django.urls import path
from website import views
urlpatterns = [
    path('', views.index),
    path('blog', views.blog),
    path('portfolio', views.portfolio),

]
