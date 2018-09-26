from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Entreprise(models.Model):
	nom_entreprise=models.CharField(max_length=20,help_text="entrer le nom de l'entreprise")
	description_entreprise=models.TextField(max_length=1000,help_text="entrer une description de l'éntreprise")
	class Meta:
		ordering=['nom_entreprise']
	def get_absolute_url(self):
		return reverse('entreprise', args=[str(self.id)])
	def __str__(self):
		return self.nom_entreprise
class Activite(models.Model):
        nom_activite=models.CharField(max_length=20,help_text="entrer le nom de l'activité")
        description_activite=models.TextField(max_length=1000,help_text="entrer une description de l'activité")
        def __str__(self):
                return self.nom_activite
        def get_absolute_url(self):
                return reverse('activite', args=[str(self.id)])
class Commentaire(models.Model):
	activite=models.ForeignKey(Activite, on_delete=models.SET_NULL, null=True, blank=True)
	auteur=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	description=models.TextField(max_length=1000, help_text="Entrer un commentaire")
	date=models.DateField(auto_now_add=True)
	class Meta:
		ordering=['date']
	def get_absolute_url(self):
		return reverse('commentaires', args=[str(self.id)])
	def __str__(self):
		return '{} {} {}'.format(self.auteur,'comment '+self.description[:75],self.date)
