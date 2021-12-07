from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from questionBank import models


# Create your views here.


class IndexView(ListView):
    context_object_name = 'ques'
    model = models.QuestionBank
    template_name = 'questionBank/index.html'


class Details(DetailView):
    context_object_name = 'ques'
    model = models.QuestionBank
    template_name = 'questionBank/question.html'


class Add(CreateView):
    fields = ('first_name', 'last_name', 'question')
    model = models.QuestionBank
    template_name = 'questionBank/addQ.html'


class Update(UpdateView):
    fields = ('first_name', 'last_name', 'question')
    model = models.QuestionBank
    template_name = 'questionBank/updateQ.html'



