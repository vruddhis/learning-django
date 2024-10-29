from django.db import models
import random

class Word(models.Model):
    text = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.text

class Attempt(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    attempt_text = models.CharField(max_length=5)

    def __str__(self):
        return f"Attempt: {self.attempt_text} for Word: {self.word.text}"

class Game(models.Model):
    player_name = models.CharField(max_length=50)
    correct_word = models.ForeignKey(Word, on_delete=models.CASCADE)
    attempts = models.ManyToManyField(Attempt)
    MAX_ATTEMPTS = 5

    def __str__(self):
        return f"Game for {self.player_name} - Correct Word: {self.correct_word.text} with {self.attempts.count()} attempts made"

    def make_attempt(self, attempt_text):
        if len(attempt_text) != 5:
            raise ValueError("Invalid input. Please enter a 5 lettered word")
        
        attempt = Attempt.objects.create(word=self.correct_word, attempt_text=attempt_text)
        self.attempts.add(attempt)

        if attempt_text == self.correct_word.text:
            return "YAYAYYAYAY!!! THIS WAS THE CORRECT WORD"
        
        feedback = self.provide_feedback(attempt_text)
        
        if self.attempts.count() >= self.MAX_ATTEMPTS:
            return f"Game Over! The correct word was '{self.correct_word.text}'."
        
        return feedback

    def provide_feedback(self, attempt_text):
        feedback = []
        correct_word_text = self.correct_word.text
        
        for i in range(len(attempt_text)):
            if attempt_text[i] == correct_word_text[i]:
                feedback.append('G')  
            elif attempt_text[i] in correct_word_text:
                feedback.append('Y')  
            else:
                feedback.append('B') 
        
        return feedback
