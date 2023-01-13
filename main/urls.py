from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geo'),
    path('skills', views.skills, name='skills'),
    path('rv', views.rv, name='rv'),
]
