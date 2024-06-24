from django.core.management import BaseCommand
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl.management.commands import search_index

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for doc in registry.get_documents():
            search_index.Command().handle(doc.Meta.model, **kwargs)