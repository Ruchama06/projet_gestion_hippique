from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Utilisateur(AbstractUser):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField(null=True,blank=True)  # Date de naissance de l'utilisateur
    telephone = models.CharField(max_length=9,default="000000000")
    adresse = models.CharField(max_length=255, default="Inconnue")

class Proprietaire(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='proprietaire')
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')], default='F')  # Genre du propriétaire

class Entraineur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entraineur')
    specialite = models.CharField(max_length=50)
    licence = models.CharField(max_length=50)  # Numéro de licence de l'entraîneur
    experience = models.IntegerField()  # Années d'expérience de l'entraîneur

class Jockey(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='jockey')
    poids = models.FloatField()
    taille = models.FloatField()
    licence = models.CharField(max_length=100)

# class Organisateur(models.Model):
#     nom = models.CharField(max_length=100)
#     adresse = models.CharField(max_length=255)
#     telephone = models.CharField(max_length=15)
#     email = models.EmailField()
#     # hippodromes = models.ManyToManyField('Hippodrome', related_name='organisateurs', blank=True)  # Hippodromes organisés par l'organisateur

# class Veterinaire(models.Model):
#     # nom = models.CharField(max_length=100)
#     # prenom = models.CharField(max_length=100)
#     # email = models.EmailField()
#     # telephone = models.CharField(max_length=15)
#     # adresse = models.CharField(max_length=255)
#     specialite = models.CharField(max_length=100)  # Spécialité du vétérinaire (ex: équine, généraliste, etc.)
#     disponibilite = models.CharField(max_length=100)  # Disponibilité du vétérinaire (ex: jours de la semaine, horaires, etc.)


# class Ecurie(models.Model):
#     nom = models.CharField(max_length=100)
#     adresse = models.CharField(max_length=255)
#     capacite = models.IntegerField()  # Capacité d'accueil de l'écurie
#     proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, related_name='ecuries')
#     entraineur = models.ForeignKey(Entraineur, on_delete=models.CASCADE, related_name='ecuries')
#     # chevaux = models.ManyToManyField('Cheval', related_name='ecuries', blank=True)  # Chevaux hébergés dans l'écurie

# class Cheval(models.Model):
#     nom = models.CharField(max_length=100)
#     age = models.IntegerField()
#     poids = models.FloatField()
#     race =models.CharField(max_length=100)  # en kilogrammes
#     sexe = models.CharField(max_length=10)
#     proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, related_name='chevaux')
#     jockey = models.ForeignKey(Jockey, on_delete=models.CASCADE, related_name='chevaux')
#     palmares = models.TextField(blank=True, null=True)  # Liste des palmarès du cheval

# class Course(models.Model):
#     nom = models.CharField(max_length=100)
#     date_cours = models.DateTimeField()
#     heure = models.TimeField()  # Heure de début de la course
#     chevaux = models.ManyToManyField(Cheval, related_name='courses')
#     jockey = models.ForeignKey(Jockey, on_delete=models.CASCADE, related_name='courses')
#     distance = models.FloatField()  # en mètres
#     type_course = models.CharField(max_length=50)  # Plat, Obstacle, Trot attelé, etc.
#     statut = models.CharField(max_length=30)
#     nbre_participants = models.IntegerField()  # Nombre de chevaux participants à la course

# class ParticipationCourseChev(models.Model):
#     jockey = models.ForeignKey(Jockey, on_delete=models.CASCADE, related_name='participations')
#     cheval = models.ForeignKey(Cheval, on_delete=models.CASCADE, related_name='participations')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='participations')
#     position = models.IntegerField()  # Position du cheval à l'arrivée de la course
#     temps_course = models.DurationField()  # Temps mis par le cheval pour terminer la course
#     gain = models.FloatField()  # Gain financier du cheval pour cette course
    
# class Hippodrome(models.Model):
#     nom = models.CharField(max_length=100)
#     adresse = models.CharField(max_length=255)
#     capacite = models.IntegerField()  # Capacité d'accueil de l'hippodrome
#     localisation = models.CharField(max_length=255)  # Localisation géographique de l'hippodrome
#     num_terrain = models.IntegerField()  # Numéro de terrain de l'hippodrome
#     proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, related_name='hippodromes')
#     courses = models.ManyToManyField(Course, related_name='hippodromes', blank=True)  # Courses organisées à l'
    

# class Bilan_Sante(models.Model):
#     cheval = models.ForeignKey(Cheval, on_delete=models.CASCADE, related_name='bilans_sante')
#     date_bilan = models.DateField()  # Date du bilan de santé
#     diagnostic = models.TextField()  # Observations du vétérinaire sur la santé du cheval
#     traitement_recommande = models.TextField(blank=True, null=True)  # Traitement recommandé par le vétérinaire
#     veterinaire = models.ForeignKey(Veterinaire, on_delete=models.CASCADE, related_name='bilans_sante')  # Vétérinaire responsable du bilan