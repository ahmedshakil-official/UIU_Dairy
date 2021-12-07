from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from feedback import models


# Create your views here.


class IndexView(ListView):
    context_object_name = 'feedback'
    model = models.Feedback
    template_name = 'feedback/index.html'



