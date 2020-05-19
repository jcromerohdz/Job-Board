from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from jobs.models import JobOffer


class JobSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer()

    class Meta:
        model = JobOffer
        exclude = ("id",)

    def get_time_since_publication(self, object):
        publication_date = object.created_at
        now = datetime.now()
        time_delta = timesince(publication_date)
        return time_delta

    def validate_company_name(self,value):
        if not value:
            raise serializers.ValidationError("The company name is nedded!")
        return value
    
    def validate_job_title(self,value):
        if not value:
            raise serializers.ValidationError("The job title name is nedded!")
        return value
