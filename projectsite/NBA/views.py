from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from NBA.models import NBATeam,NBAPlayer,Brands,Playerscareer,ProLeague
from django.urls import reverse_lazy



class HomePageView(ListView):
    model = NBATeam
    context_object_name = 'home'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PlayersCareer(ListView):
    model = Playerscareer
    context_object_name = 'playerscareer'
    template_name = "players_career.html"
    paginate_by = 8
    ordering = ['created_at']  # Use a valid field from the Playerscareer model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    

class NBAPlayers(ListView):
    model = NBAPlayer
    context_object_name = 'nbaplayers'
    template_name = "player_list.html"
    paginate_by = 8
    ordering = ['created_at']  # Use a valid field from the Playerscareer model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NBATeam(ListView):
    model = NBATeam
    context_object_name = 'teams'
    template_name = "team.html"
    paginate_by = 8
    ordering = ['created_at']  # Use a valid field from the Playerscareer model
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class Brands(ListView):
    model = Brands
    context_object_name = 'brands'
    template_name = "brands.html"
    paginate_by = 8
    ordering = ['created_at']  # Use a valid field from the Playerscareer model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Create your views here.
