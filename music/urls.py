from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from app1.api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/Music/', views.create.as_view(), name="api"),  # api create
    path('list/', views.show.as_view(), name="api"),  # api list
    url(r'^(?P<id>\d)/update/',views.update.as_view() , name='update'), # update
    url(r'^(?P<id>\d)/user/',views.user.as_view(),name='user'),
    path('create/user/',views.createUser.as_view(),name='Create User'),
    path('api-auth/', include('rest_framework.urls',namespace="api-main")),

]
