from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('panel/', views.PanelList.as_view()),
    path('panel/<int:pk>/', views.PanelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)