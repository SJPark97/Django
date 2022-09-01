from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # created_at = request.GET.get('created_at')
    # updated_at = request.GET.get('updated_at')
    title = request.POST.get('title')
    content = request.POST.get('content')
    created_at = request.POST.get('created_at')
    updated_at = request.POST.get('updated_at')

    # article = Article()
    # article.title = title
    # article.content = content
    # article.created_at = created_at
    # article.updated_at = updated_at
    # article.save()

    # Article.objects.create(title=title, content=content, created_at=created_at, updated_at=updated_at)

    article = Article(
        title=title, content=content, created_at=created_at, updated_at=updated_at
    )
    article.save()

    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    NEXT = pk + 1
    PREV = pk - 1
    context = {
        'article': article,
        'NEXT': NEXT,
        'PREV': PREV,
    }

    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
