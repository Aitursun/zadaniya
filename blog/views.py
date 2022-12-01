from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from . import forms

# Create your views here.
def hello_world(request):
    return HttpResponse('<h1>Страница </h1>')

def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post':post})

def blog_detail(request, id):
    posts = get_object_or_404(models.Post, id=id)
    return render(request, 'postview_detail.html', {'posts':posts})

class PostView(generic.ListView):
    template_name = 'postview.html'
    queryset = models.Post.objects.all()

def get_queryset(self):
    return models.Post.objects.all()

class PostDetailView(generic.DetailView):
    template_name = 'postview_detail.html'

def get_object(self, **kwargs):
    postview_id = self.kwargs.get('id')
    return get_object_or_404(models.Post, id=postview_id)





#create TvShow
class PostCreateView(generic.CreateView):
    template_name = 'add_post_list.html'
    form_class = forms.PostForm
    queryset = models.Post.objects.all()
    success_url = '/posts/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PostCreateView, self).form_valid(form=form)

#update TvShow

class PostUpdateView(generic.UpdateView):
    template_name = 'post_update.html'
    form_class = forms.PostForm
    success_url = '/posts/'

    def get_object(self, **kwargs):
        postview_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=postview_id)

    def form_valid(self, form):
        return super(PostUpdateView, self).form_valid(form=form)

#delete TvShow
class PostDeleteView(generic.DeleteView):
    template_name = 'post_delete.html'
    success_url = '/posts/'

    def get_object(self, **kwargs):
        postview_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=postview_id)