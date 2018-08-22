from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Album,Song,UserSignup


class IndexView(generic.ListView):
    template_name = 'signup/index.html'

    def get_queryset(self):
        return UserSignup.objects.all()


class DetailView(generic.DetailView):
    model = UserSignup

    template_name = 'signup/details.html'





