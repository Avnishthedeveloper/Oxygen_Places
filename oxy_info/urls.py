from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from oxy_info import views

urlpatterns = [
	path('Places/', views.PlaceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)