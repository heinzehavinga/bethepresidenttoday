from rest_framework import serializers
from game.models import *

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem

        fields = ('id', 'name', 'text', 'actual_result', 'tweet', 'tweet_link', 'actual_result_title', 'background_media_url', 'actual_result_media_url')
        read_only_fields = ('id', 'name', 'text', 'actual_result', 'tweet', 'tweet_link', 'actual_result_title', 'background_media_url', 'actual_result_media_url')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ProblemSerializer, self).get_validation_exclusions()

        return exclusions

class ChoiceProblemSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Choice

        fields = ('text', 'resultText', 'scoreA', 'scoreB', 'scoreC', 'scoreD', 'scoreE', 'scoreF')
#TODO: Volgens mij kan hier het id veld ook bij
        read_only_fields = ('text', 'resultText', 'scoreA', 'scoreB', 'scoreC', 'scoreD', 'scoreE', 'scoreF')

    def get_validation_exclusions(self, *args, **kwargs):
#TODO: Leren wat dit regeltje doet
        exclusions = super(ResultWordTwitterSerializer, self).get_validation_exclusions()

        return exclusions
