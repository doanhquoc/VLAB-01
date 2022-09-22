from django.urls import path

from . import views

from .views import GetListWorkInfo

# urlpatterns = [
#     path('', views.get_info_detail_api_views, name='index'),
# ]

app_name = 'post_working'

urlpatterns = [
    path('', GetListWorkInfo.as_view(), name='info-detail'),
]