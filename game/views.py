from django.shortcuts import render
from game.serializers import *
from rest_framework import permissions, viewsets
from rest_framework.response import Response
# Create your views here.


class ProblemsViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #     return (permissions.IsAuthenticated(), IsAuthorOfReport(),)

    # def perform_create(self, serializer):
    #     instance = serializer.save(author=self.request.user)
        
    #     return super(ReportViewSet, self).perform_create(serializer)

class ChoiceProblemViewSet(viewsets.ViewSet):
    queryset = Choice.objects.select_related('problem').all()
    serializer_class = ChoiceProblemSerializer

    def list(self, request, problems_pk=None):
        queryset = self.queryset.filter(problem__pk=problems_pk)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)