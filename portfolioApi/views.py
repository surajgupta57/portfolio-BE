from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.views import View


@api_view(['GET'])
def get_jumbo(request):
    intro_details = Jumbo.objects.filter().order_by("-weight")
    serializer = JumboSerializer(intro_details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_works_todo(request):
    details = ServicesOffred.objects.filter().order_by("-weight")
    serializer = ServicesOffredSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_social_media(request):
    details = SocialMediaLinks.objects.filter().order_by("-weight")
    serializer = SocialMediaLinksSerializer(details, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_projects(request):
    details = Project.objects.filter().order_by("-weight")
    serializer = ProjectSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_me(request):
    details = AboutMeSection.objects.filter().order_by("-weight")
    serializer = AboutMeSectionSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_contacted(request):
    details = ContactMe.objects.all()
    serializer = ContactMeSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_progress_bar(request):
    details = SkillSection.objects.filter().order_by("-weight")
    serializer = SkillSectionSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_technologies_icon(request):
    details = LanguageIcons.objects.filter().order_by("-weight")
    serializer = LanguageIconsSerializer(details, many=True)
    return Response(serializer.data)


class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()
