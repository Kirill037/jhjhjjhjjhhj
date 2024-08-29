from django.shortcuts import get_object_or_404, redirect
from news.forms import FavoriteForm
from .models import Favorite
from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_articles(category="all", lang="ru", page_size=200):
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={category}&language={lang}&pageSize={page_size}&apiKey={API_KEY}"
    )
    data = response.json()
    if data["status"] != "ok":
        print("[!] Ошибка в получении новостей")
        return

    return data["articles"]


def homepage_view(request):
    news = get_articles(category="sport", page_size=30)
    return render(request, "index.html", {"news_items": news})


# Возвращает понравившиеся новости
def favorites_view(request):
    items = Favorite.objects.all()
    return render(request, "favorite_items.html", {"favorite_items": items})


def add_favorite(request):
    if request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.title = favorite.title or "No Title"
            favorite.description = favorite.description or "No Description"
            favorite.url = favorite.url or "http://example.com"
            favorite.published_at = favorite.published_at or None
            favorite.author = favorite.author or "Unknown Author"
            form.save()
            return redirect("favorites")
        print("ADD_FAVORITE")
        print(form.errors)
    return redirect("home")


def delete_favorite(_request, favorite_id):
    favorite = get_object_or_404(Favorite, id=favorite_id)
    favorite.delete()
    return redirect('favorites')
