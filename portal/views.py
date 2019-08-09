from django.shortcuts import render, get_object_or_404

from .models import ShortPost, Researcher, Post, Article


def home(request):
    context = {}
    short_posts = ShortPost.objects.filter(is_cover=True)
    researchers = Researcher.objects.filter(is_cover=True)
    posts = Post.objects.filter(is_cover=True)
    context['short_posts'] = short_posts
    context['researchers'] = researchers
    context['posts'] = posts
    return render(request, 'portal/home/_home.html', context)

def researchers(request):
  context = {}
  return render(request, 'portal/researcher/_index.html', context)

def researcher_detail(request, researcher_id):
  context = {}
  researcher = get_object_or_404(Researcher, pk=researcher_id)
  articles = Article.objects.filter(researcher_id=researcher_id)
  context['researcher'] = researcher
  context['articles'] = articles
  return render(request, 'portal/researcher/_detail.html', context)

def posts(request):
  context = {}
  return render(request, 'portal/post/_index.html', context)

def post_detail(request, post_id):
  context = {}
  post = get_object_or_404(Post, pk=post_id)
  context['post'] = post
  return render(request, 'portal/post/_detail.html', context)
