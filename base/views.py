from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn Python'},
    {'id': 2, 'name': 'Lets Learn Django'},
    {'id': 3, 'name': 'Lets Learn React'},
]


# def home(request):
#     return render(request, 'home.html', {'rooms': rooms})

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}    
    return render(request, 'base/room.html', context)