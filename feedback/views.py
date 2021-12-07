from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from feedback import models


# Create your views here.


class IndexView(ListView):
    context_object_name = 'feedback'
    model = models.Feedback
    template_name = 'feedback/index.html'


class Details(DetailView):
    context_object_name = 'feedback'
    model = models.Feedback
    template_name = 'feedback/feedback.html'


class Add(CreateView):
    fields = ('first_name', 'last_name', 'feedback')
    model = models.Feedback
    template_name = 'feedback/addFeedback.html'


class Update(UpdateView):
    fields = ('first_name', 'last_name', 'feedback')
    model = models.Feedback
    template_name = 'feedback/updateFeedback.html'


class Delete(DeleteView):
    context_object_name = 'feedback'
    model = models.Feedback
    success_url = reverse_lazy('f:home')
    template_name = 'feedback/deleteFeedback.html'
