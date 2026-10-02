
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BlogPost

class PostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content', 'image']
    template_name = 'blogpost_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'image']
    template_name = 'blogpost_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('post_list')