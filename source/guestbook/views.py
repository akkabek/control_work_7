from django.shortcuts import render, redirect, get_object_or_404

from guestbook.forms import GuestbookEntryForm
from guestbook.models import GuestbookEntry


def index_view(request):
    entries = GuestbookEntry.objects.all().order_by('-created_at').filter(status='active')
    context = {'entries': entries}
    return render(request, 'index.html', context)

def entry_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = GuestbookEntryForm()
        return render(request, 'entry_create.html', context={'form': form})
    elif request.method == 'POST':
        form = GuestbookEntryForm(data=request.POST)
        if form.is_valid():
            GuestbookEntry.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                content=form.cleaned_data['content']
            )
            return redirect('list')
        else:
            return render(request, 'entry_create.html', context={'form': form})

def entry_edit_view(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'GET':
        form = GuestbookEntryForm(initial={
            'author': entry.author,
            'email': entry.email,
            'content': entry.content
        })
        return render(request, 'entry_edit.html', context={'form':form,'entry': entry})
    elif request.method == 'POST':
        form = GuestbookEntryForm(data=request.POST)
        if form.is_valid():
            entry.author = form.cleaned_data['author']
            entry.email = form.cleaned_data['email']
            entry.content = form.cleaned_data['content']
            entry.save()
            return redirect('list')
        else:
            return render(request, 'entry_edit.html', context={'form': form, 'entry': entry})


