from django.urls import path
from .views import homePageView, ethanPageView, aboutPageView, results, homePost
urlpatterns = [
    path('', homePageView, name='home'),
    path('ahout/', aboutPageView, name='about'),
    path('ethan', ethanPageView, name='ethan'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
