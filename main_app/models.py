from django.db import models
from datetime import date
from django.urls import reverse
# import user
from django.contrib.auth.models import User

from django.contrib.auth.models import User


CATEGORIES = (
    (1, 'Abs'), 
    (2, 'Arms'), 
    (3, 'Back'), 
    (4, 'Calves'), 
    (5, 'Cardio'), 
    (6, 'Chest'), 
    (7, 'Legs'), 
    (8, 'Shoulders'),
)

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
        )
    equipment = models.CharField(max_length=20)
    weights = models.IntegerField()
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):

        return f"{self.name}: {self.reps} reps x {self.sets} set(s)"
    
    def get_absolute_url(self):
        return reverse('exercises_detail', kwargs={'pk': self.id})

class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('workout date')
    duration = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    exercises = models.ManyToManyField(Exercise, related_name='workouts')

    def __str__(self):
        return self.name
<<<<<<<<< Temporary merge branch 1
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    weights = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f"{self.exercise.name} - {self.weights} lbs - {self.reps} reps"
=========
>>>>>>>>> Temporary merge branch 2
