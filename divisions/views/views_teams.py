from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from divisions.models import Team
from boards.models import Board
from django.contrib.auth.mixins import LoginRequiredMixin

class TeamList(LoginRequiredMixin, ListView):
	model = Team
	context_object_name = 'teams'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['header'] = "Teams"
		context['sub_header'] = "We are groups of individuals working towards a common goal"
		return context

class TeamDetail(LoginRequiredMixin, DetailView):
	model = Team
	context_object_name = 'team_detail'
	pk_url_kwarg = 'team_id'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TeamCreate(LoginRequiredMixin, CreateView):
	model = Team
	fields = ['name', 'description','members']
	template_name = 'create-form.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formTitle'] = "Create Team"
		return context

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class TeamUpdate(LoginRequiredMixin, UpdateView):
	model = Team
	fields = ['name', 'description','members']
	template_name = 'create-form.html'

class TeamDelete(LoginRequiredMixin, DeleteView):
	model = Team
	pk_url_kwarg = 'team_id'
	template_name = 'confirm-delete.html'
	success_url = "/"