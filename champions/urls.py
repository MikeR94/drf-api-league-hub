from django.urls import path
from champions import views


urlpatterns = [
    path("champions/", views.ChampionList.as_view()),
    path("champions/<int:pk>/", views.ChampionDetail.as_view()),
]
