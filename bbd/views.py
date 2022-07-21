from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Player


def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Saul T'})


def list_players(request):
    player_list = Player.objects.all()
    paginator = Paginator(player_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_players.html', {'page_obj': page_obj})
