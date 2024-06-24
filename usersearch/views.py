# views.py
from .document import CandidateNameDocument
from .models import Candidate
from .serializers import CandidateSerializer, CandidateSearchSerializer, CandidateNameSerializer
import json

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

class CandidateSearchView(APIView):
    def get(self, request):
        serializer = CandidateSearchSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        expected_salary_min = serializer.validated_data.get('expected_salary_min')
        expected_salary_max = serializer.validated_data.get('expected_salary_max')
        age_min = serializer.validated_data.get('age_min')
        age_max = serializer.validated_data.get('age_max')
        years_of_experience_min = serializer.validated_data.get('years_of_experience_min')
        phone_number = serializer.validated_data.get('phone_number')
        email = serializer.validated_data.get('email')
        name = serializer.validated_data.get('name')

        queryset = Candidate.objects.all()

        # Apply filters based on validated data
        if expected_salary_min is not None and expected_salary_max is not None:
            queryset = queryset.filter(expected_salary__gte=expected_salary_min, expected_salary__lte=expected_salary_max)

        if age_min is not None and age_max is not None:
            queryset = queryset.filter(age__gte=age_min, age__lte=age_max)

        if years_of_experience_min is not None:
            queryset = queryset.filter(years_of_experience__gte=years_of_experience_min)

        if phone_number:
            queryset = queryset.filter(phone_number__icontains=phone_number)

        if email:
            queryset = queryset.filter(email__icontains=email)

        if name:
            queryset = queryset.filter(name__icontains=name)

        serializer = CandidateSerializer(queryset, many=True)
        return Response(serializer.data)


class NameSearchView(APIView):
    def get(self, request):
        query_param = request.query_params.get('name')
        if not query_param:
            return Response({"error": "Missing query parameter"}, status=400)

        # Perform Elasticsearch search using django-elasticsearch-dsl
        queryset = CandidateNameDocument.search().query("multi_match", query=query_param, fields=['name'])

        # Serialize the queryset using the Elasticsearch document serializer
        serializer = CandidateNameSerializer(queryset.to_queryset(), many=True)
        json_data = JSONRenderer().render(serializer.data)
        json_data_dict = json.loads(json_data)

        return Response(json_data_dict)

