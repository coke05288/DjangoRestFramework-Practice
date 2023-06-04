from django.urls import re_path
from .views.testapp import MemberListView

urlpatterns = [
    re_path(r'^member/$', MemberListView.as_view(), name='member'),
]