from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:game_id>/", views.game_board, name="game_board"),  
    path("<int:game_id>/result/", views.game_result, name="game_result"), 
    path("games/", views.all_games, name="all_games"), 
]