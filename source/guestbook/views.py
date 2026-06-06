from django.shortcuts import render

from guestbook.models import GuestbookEntry


def index_view(request):
    entries = GuestbookEntry.objects.all().order_by('-created_at').filter(status='active')
    context = {'entries': entries}
    return render(request, 'index.html', context)