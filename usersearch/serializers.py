from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'name',
            'gender',
            'years_of_experience',
            'phone_number',
            'email',
            'current_salary',
            'expected_salary',
            'age'
        ]

    def validate_name(self, value):
        if len(value.split()) < 2:
            raise serializers.ValidationError("Full name must contain at least two words.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError("Phone number must be between 10 and 15 digits.")
        return value

    def validate_years_of_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Years of experience cannot be negative.")
        return value

    def validate_current_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Current salary cannot be negative.")
        return value

    def validate_expected_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Expected salary cannot be negative.")
        return value

    def validate(self, data):
        if data['current_salary'] > data['expected_salary']:
            raise serializers.ValidationError("Expected salary must be greater than or equal to the current salary.")
        return data


class CandidateSearchSerializer(serializers.Serializer):
    expected_salary_min = serializers.IntegerField(required=False)
    expected_salary_max = serializers.IntegerField(required=False)
    age_min = serializers.IntegerField(required=False)
    age_max = serializers.IntegerField(required=False)
    years_of_experience_min = serializers.IntegerField(required=False)
    phone_number = serializers.CharField(max_length=15, required=False)
    email = serializers.EmailField(max_length=100, required=False)
    name = serializers.CharField(max_length=200, required=False)

    def validate(self, data):
        expected_salary_min = data.get('expected_salary_min')
        expected_salary_max = data.get('expected_salary_max')
        age_min = data.get('age_min')
        age_max = data.get('age_max')
        years_of_experience_min = data.get('years_of_experience_min')

        if expected_salary_min and expected_salary_max and expected_salary_min > expected_salary_max:
            raise serializers.ValidationError("Minimum expected salary cannot be greater than maximum expected salary.")

        if age_min and age_max and age_min > age_max:
            raise serializers.ValidationError("Minimum age cannot be greater than maximum age.")

        if years_of_experience_min and years_of_experience_min < 0:
            raise serializers.ValidationError("Minimum years of experience cannot be negative.")

        return data


class CandidateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name']
