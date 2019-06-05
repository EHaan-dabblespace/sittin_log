from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from sittin_log_app.models import Pet, Family


class PetListView(LoginRequiredMixin, ListView):

    template_name = './pet_list.html'
    model = Pet
    context_object_name = 'pets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Pet.objects.filter(family__user_id=self.request.user.id)

class FamilyListView(LoginRequiredMixin, ListView):

    template_name = './family_list.html'
    model = Family
    context_object_name = 'families'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Family.objects.filter(user_id=self.request.user.id)
