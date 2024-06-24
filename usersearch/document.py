from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Candidate

@registry.register_document
class CandidateNameDocument(Document):

    class Index:
        name = 'candidates-exp'  # Elasticsearch index name

    class Django:
        model = Candidate
        fields = ["id", "name", "age", "gender", "years_of_experience", "phone_number", "email", "current_salary", "expected_salary", "status"]
