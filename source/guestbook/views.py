from django.shortcuts import render, redirect, get_object_or_404

from guestbook.forms import GuestbookEntryForm, SearchForm
from guestbook.models import GuestbookEntry


def index_view(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    search_form = SearchForm(data=request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            entries = entries.filter(author=query)

    form = GuestbookEntryForm()
    context = {'entries': entries, 'search_form': search_form, 'form': form}
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

def entry_delete_view(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    errors = {}
    if request.method == 'POST':
        check_email = request.POST.get('check_email')
        if check_email == entry.email:
            entry.delete()
            return redirect('list')
        else:
            errors['email'] = 'Email does not match'
    return render (request, 'entry_delete.html', context={'entry': entry, 'errors': errors})