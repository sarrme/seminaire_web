
    
from django.shortcuts import render
from .models import Entreprise, Activite, Commentaire
from django.contrib.auth.models import User
def index(request):
	num_entreprise=Entreprise.objects.all().count()
	return render(
        request,
        'index.html',
        context={'num_entreprise':num_entreprise},)
from django.views import generic
class EntrepriseList(generic.ListView):
	model=Entreprise
    
	paginate_by=10
class EntrepriseDetail(generic.DetailView):
	model=Entreprise

class ActiviteDetail(generic.DetailView):
	model= Activite

class ActiviteList(generic.ListView):
	model=Activite
    
from django.shortcuts import get_object_or_404
from django.urls import reverse


	
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
class CommentaireCreate(CreateView):
	model=Commentaire
	fields=['description',]
	def get_context_data(self, **kwargs):
		context = super(CommentaireCreate, self).get_context_data(**kwargs)
		context['activite'] = get_object_or_404(Activite, pk = self.kwargs['pk'])
		return context
	def form_valid(self, form):
		form.instance.auteur = self.request.user
		form.instance.activite = get_object_or_404(Activite, pk = self.kwargs['pk'])
		return super(CommentaireCreate, self).form_valid(form)
	def get_success_url(self, **kwargs): 
		return reverse('activite', kwargs={'pk': self.kwargs['pk'],})
        
        
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})