# admin.py

from django.contrib import admin
from .models import Candidate

# Define a custom ModelAdmin class
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'years_of_experience', 'phone_number', 'email', 'status')
    list_filter = ('gender', 'status')
    search_fields = ('name', 'email', 'phone_number')
    list_per_page = 20  # Number of items to display per page

# Register the Candidate model with the custom admin options
admin.site.register(Candidate, CandidateAdmin)
