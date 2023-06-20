from dataclasses import field
from rest_framework import serializers
from .models import *


class JumboSerializer(serializers.ModelSerializer):
    contact = serializers.CharField(source="contact.contact_info")

    class Meta:
        model = Jumbo
        fields = '__all__'


class AboutMeSectionSerializer(serializers.ModelSerializer):
    cv = serializers.CharField(source="cv.cv.url")
    class Meta:
        model = AboutMeSection
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMe
        fields = '__all__'


class ServicesOffredSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesOffred
        fields = '__all__'


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = '__all__'


class SkillSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSection
        fields = '__all__'


class LanguageIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageIcons
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
