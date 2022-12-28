from django.urls import path
from upvotes import views


urlpatterns = [
    path("upvotes/", views.UpVoteList.as_view()),
    path("upvotes/<int:pk>/", views.UpVoteDetail.as_view()),
]
