from django.conf.urls import url, patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    # url(r'^data/', views.json_data, name='json_data')
]