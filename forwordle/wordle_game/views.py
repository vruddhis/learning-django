from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpRequest, HttpResponse
from .models import Game, Word, Attempt 

import random

def index(request):
    word = random.choice(Word.objects.all())
    game = Game.objects.create(player_name="Player", correct_word=word)
    return render(request, "wordle_game/index.html", {"game": game})

def game_board(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    attempts = game.attempts.all()  
    feedbacks = []

    if request.method == 'POST':
        attempt_text = request.POST.get('attempt_text', '').upper()  # Assuming uppercase input
        if attempt_text:
            feedback = game.make_attempt(attempt_text)
            return render(request, 'wordle_game/game_board.html', {
                'game': game,
                'attempts': attempts,
                'feedbacks': feedbacks,
                'last_feedback': feedback,
            })

    for attempt in attempts:
        feedback = game.provide_feedback(attempt.attempt_text)
        feedbacks.append(f"{attempt.attempt_text}: {feedback}")

    return render(request, 'wordle_game/game_board.html', {
        'game': game,
        'attempts': attempts,
        'feedbacks': feedbacks,
        'last_feedback': None,
    })



def game_result(request, game_id):
    game = Game.objects.get(id=game_id)
    attempts = game.attempts.all()
    feedbacks = [
        {"attempt_text": attempt.attempt_text, "feedback": game.provide_feedback(attempt.attempt_text)}
        for attempt in attempts
    ]

    return render(request, "wordle_game/game_result.html", {"game": game, "feedbacks": feedbacks})

def all_games(request):
    games = Game.objects.all()
    return render(request, "wordle_game/all_games.html", {"games": games})
