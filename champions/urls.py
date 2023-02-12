from django.urls import path
from champions import views


urlpatterns = [
    path("champions/", views.ChampionList.as_view()),
    path("champions/<int:pk>/", views.ChampionDetail.as_view()),
    path("champions/<int:pk>/edit/", views.ChampionEdit.as_view()),
    path("champions/<int:pk>/delete/", views.ChampionDelete.as_view()),
    path("champions/create/", views.ChampionCreate.as_view()),
    path("champions/leaderboard/", views.ChampionLeaderboard.as_view()),
]
