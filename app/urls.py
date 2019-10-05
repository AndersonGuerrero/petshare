from django.conf.urls import url
from app.views import AppIndex

urlpatterns = [
    url(r'^$', AppIndex.as_view(), name='app_index'),
]