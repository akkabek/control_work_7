from django.contrib import admin
from guestbook.models import GuestbookEntry



class GuestbookEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'created_at']
    list_filter = ['author','email']
    search_fields = ['author', 'email']
    fields = [ 'author','email', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(GuestbookEntry, GuestbookEntryAdmin)