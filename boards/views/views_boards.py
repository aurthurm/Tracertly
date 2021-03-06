from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import *
from boards.forms import BoardForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class BoardList(ListView):
	model = Board
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['header'] = "All Boards"
		context['sub_header'] = "A list of all Boards Ever Created in this System"
		return context

class UserBoards(ListView):
	model = Board
	template_name = 'boards/user-boards.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# get the request / logged on user
		user = self.request.user
		# Get all the boards the user has created
		user_boards = Board.objects.filter(creator=user)
		context['header'] = "My Boards"
		context['sub_header'] = "These are the boards you created."
		context['user_boards'] = user_boards
		return context

class BoardDetail(DetailView):
	model = Board
	context_object_name = 'board_detail'
	pk_url_kwarg = 'board_id'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		board_listings = Listing.objects.all().filter(board=self.get_object()) # name=self.object.name
		all_items = Item.objects.all()
		context['board_listings'] = board_listings
		context['all_items'] = all_items
		return context
	
class BoardCreate(LoginRequiredMixin, CreateView):
	model = Board
	fields = ['name', 'description','section', 'public', 'archived']
	template_name = 'create-form.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formTitle'] = "Create Board"
		return context

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class BoardUpdate(UpdateView):
	model = Board
	pk_url_kwarg = 'board_id'
	fields = ['name', 'description','section', 'public', 'archived']
	template_name = 'create-form.html'

class BoardDelete(DeleteView):
	model = Board
	pk_url_kwarg = 'board_id'
	template_name = 'confirm-delete.html'
	success_url = "/"
