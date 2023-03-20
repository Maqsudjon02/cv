from django.urls import path
from .views import HomePageView,AboutPageView,CallPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('cal/',CallPageView.as_view(),name='call'),
]
