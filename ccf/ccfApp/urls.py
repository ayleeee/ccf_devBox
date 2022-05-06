from django.urls import path,include
from ccfApp.views import search,HomePageView

urlpatterns = [
    path('search/',search.as_view(),name='search'),
    path('',HomePageView.as_view(),name='home') ,   
]
