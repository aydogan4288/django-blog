from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated():
        context = {
        'name': 'Ferhat'
        }
    else:
        context = {
        'name': 'Misafir',
        }
    return render(request, 'home.html', context)
