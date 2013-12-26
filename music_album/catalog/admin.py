from django.contrib import admin
from models import Album, Artist, Track

class Album_form(admin.ModelAdmin):
    list_display = ('name', 'genre', 'relyr', 'is_famous')
    list_filter = ['relyr']
    search_fields = ['name']
    prepopulated_fields = {'link': ('name', )}
    
admin.site.register(Album, Album_form)

class Artist_form(admin.ModelAdmin):
    list_display = ('name', 'dob', 'is_famous')
    list_filter = ['dob']
    search_fields = ['name']
    prepopulated_fields = {'link': ('name', )}
    
admin.site.register(Artist, Artist_form)

class Track_form(admin.ModelAdmin):
    
    search_fields = ['name']
    prepopulated_fields = {'link': ('name', )}
    
admin.site.register(Track, Track_form)