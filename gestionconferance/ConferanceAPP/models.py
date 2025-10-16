from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
import uuid
from datetime import date

# Create your models here.
# Vérifie que le titre de la conférence contient uniquement des lettres et espaces
conference_name_validator = RegexValidator(
    regex=r'^[A-Za-z\s]+$',
    message="Le titre de la conférence ne doit contenir que des lettres et espaces."
)
# Vérifie que le nom de la salle contient seulement lettres et chiffres
room_validator = RegexValidator(
    regex=r'^[A-Za-z0-9\s]+$',
    message="Le nom de la salle ne doit contenir que des lettres et chiffres."
)
# Vérifie que le nombre de mots-clés ne dépasse pas 10
def validate_keywords(value):
    words = [w.strip() for w in value.split(",") if w.strip()]
    if len(words) > 10:
        raise ValidationError("Vous ne pouvez pas avoir plus de 10 mots-clés.")
# Génère un ID automatique pour les soumissions
def generate_submission_id():
    return "SUB-" + uuid.uuid4().hex[:8].upper()



class Conference(models.Model):
    conferance_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    THEME=[
        ("IA","Computer science & ia"),
        ("SE","Science & eng"),
        ("SC","Social sciences"),
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    location=models.CharField(max_length=50)
    description=models.TextField(validators=[MinLengthValidator(30,"minimum 30 caracteres")])
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"la conference a comme titre {self.name}"

    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("la date de debut de la conference doit etre inferieur a la date fin")
        

class Submission(models.Model):
    submission_id=models.CharField(max_length=255,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=50)
    abstract=models.TextField()
    keywords=models.TextField()
    paper=models.FileField(
        upload_to="papers/"
    )
    STATUS=[
        
        ("submitted" ,"submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected"),

    ]

    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
# Génération automatique du submission_id
    def save(self, *args, **kwargs):
        if not self.submission_id:
            self.submission_id = generate_submission_id()
        super().save(*args, **kwargs)

    # Vérifications supplémentaires
    def clean(self):
        today = date.today()
        # Vérifie que la conférence est à venir
        if self.conference.start_date < today:
            raise ValidationError("Les soumissions ne sont possibles que pour les conférences à venir.")
        # Limite : un participant ne peut soumettre que 3 papiers par jour
        count = Submission.objects.filter(user=self.user, submission_date=today).count()
        if count >= 3:
            raise ValidationError("Vous avez déjà soumis 3 articles aujourd'hui.")

class organizing_committe(models.Model):
    COMITEE_ROLE=[
        ("chair","chair"),
        ("co-chair","co-chair"),
        ("member","member"),
    ]


    commitee_role=models.CharField(max_length=255,choices=COMITEE_ROLE)
    date_joined=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="commitee")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="commitee")


#  Validation : une seule personne peut être chair et une seule co-chair par conférence
    def clean(self):
        if self.commitee_role in ["chair", "co-chair"]:
            exists = organizing_committe.objects.filter(
                conference=self.conference,
                commitee_role=self.commitee_role
            ).exclude(pk=self.pk).exists()
            if exists:
                raise ValidationError(f"Cette conférence a déjà un {self.commitee_role}.")

    def __str__(self):
        return f"{self.user.username} - {self.commitee_role} ({self.conference.name})"
    


    
     
    
    


