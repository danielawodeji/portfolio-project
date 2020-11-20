from django.contrib import admin




from django.forms import TextInput, Textarea
from django.db import models
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':400})},
    }

admin.site.register(Blog, BlogAdmin)