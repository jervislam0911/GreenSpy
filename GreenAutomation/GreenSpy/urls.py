from django.conf.urls import url, patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^plant/$', views.plant_list, name='plant_list'),
    url(r'^plant/(?P<pk>[0-9]+)/$', views.plant_detail, name='plant_detail'),
    url(r'^data/', views.json_data, name='json_data'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^power_on/$', views.power_on, name='power_on'),
    url(r'^power_off/$', views.power_off, name='power_off'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

