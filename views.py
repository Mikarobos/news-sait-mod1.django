from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment, Category, Article
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'firstapp/category_list.html', {'categories': categories})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'firstapp/article_list.html', {'articles': articles})


def index(request):
    news = News.objects.all()  # Получаем все объекты News
    return render(request, "firstapp/index.html", {'news': news})


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    comments = news_item.comments.all()  # Получаем все комментарии к новости
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.user = request.user  # Присваиваем текущего пользователя
            comment.save()
            return redirect('news_detail', news_id=news_item.id)  # Перенаправляем на ту же страницу
    else:
        form = CommentForm()
    return render(request, "firstapp/news_detail.html", {'news_item': news_item, 'comments': comments, 'form': form})


def calculator_risk(request):
    return render(request, 'firstapp/calculator_risk.html')

