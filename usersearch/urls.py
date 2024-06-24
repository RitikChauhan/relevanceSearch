from django.urls import path

from usersearch.views import CandidateSearchView, NameSearchView

urlpatterns = [
    path('search/', CandidateSearchView.as_view(), name='name-search'),
    path('relevance_search/', NameSearchView.as_view(), name='relevance-search')
]