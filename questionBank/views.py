from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from questionBank import models


# Create your views here.


class IndexView(ListView):
    context_object_name = 'ques'
    model = models.QuestionBank
    template_name = 'questionBank/index.html'



