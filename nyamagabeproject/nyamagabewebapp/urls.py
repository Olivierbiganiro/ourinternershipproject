
from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/',views.detail_view, name='detail'),
]
 