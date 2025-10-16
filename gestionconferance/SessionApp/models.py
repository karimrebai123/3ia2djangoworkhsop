from django.db import models
from ConferanceAPP.models import Conference
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here. 

room_validator = RegexValidator(
    regex=r'^[A-Za-z0-9\s]+$',
    message="Le nom de la salle ne doit contenir que des lettres et chiffres."
)
    
class Session(models.Model):
    session_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    conference=models.ForeignKey("ConferanceAPP.Conference",
                                 on_delete=models.CASCADE,
                                 related_name="sessions")

 
  #  Validation logique : heures et dates
    def clean(self):
        errors = {}

        # Vérifie que l'heure de fin est après l'heure de début
        if self.start_time and self.end_time and self.start_time >= self.end_time:
            errors['end_time'] = ValidationError("L'heure de fin doit être supérieure à l'heure de début.")

        # Vérifie que la date de la session est dans la période de la conférence
        if self.conference and self.session_date:
            if not (self.conference.start_date <= self.session_date <= self.conference.end_date):
                errors['session_date'] = ValidationError(
                    "La date de la session doit appartenir à la période de la conférence."
                )

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"Session : {self.title} ({self.conference.name})"