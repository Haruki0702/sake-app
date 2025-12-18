from django.shortcuts import render
from .event_scraping import get_sake_events

def event_list(request):
    events=get_sake_events()
    return render(request, "sake_event_scraping/event_list.html",{"events": events})

# Create your views here.
