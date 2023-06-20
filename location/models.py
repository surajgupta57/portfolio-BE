from django.db import models
from django.forms import JSONField
from analytics.utils import unique_slug_generator_using_name

from location.utils import user_city_photo_upload_path, user_country_photo_upload_path, user_district_photo_upload_path, user_district_region_photo_upload_path, user_states_photo_upload_path

# Create your models here.

class Pincode(models.Model):
    type = models.CharField(max_length=30, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.pincode


class Country(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    params = JSONField(null=True, blank=True, default=dict)
    description = models.TextField(
        max_length=3000, null=True, blank=True)
    photo = models.FileField(
        upload_to=user_country_photo_upload_path, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator_using_name(self)
        super().save(*args, **kwargs)


class States(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    country = models.ForeignKey(
        "Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=3000, null=True, blank=True)
    params = JSONField(null=True, blank=True, default=dict)
    photo = models.FileField(
        upload_to=user_states_photo_upload_path, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator_using_name(self)
        super().save(*args, **kwargs)


class City(models.Model):
    OPTIONS = (("Main", "Main"), ("Other", "Other"), ("Category", "Category"))
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    country = models.ForeignKey(
        "Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    states = models.ForeignKey(
        "States",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=3000, null=True, blank=True)
    params = JSONField(null=True, blank=True, default=dict)
    photo = models.FileField(
        upload_to=user_city_photo_upload_path, blank=True, null=True
    )
    type = models.CharField(max_length=15, choices=OPTIONS, null=True, blank=True, default="Other")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator_using_name(self)
        super().save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    state = models.ForeignKey(
        "States",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    country = models.ForeignKey(
        "Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    city = models.ForeignKey(
        "City",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    photo = models.FileField(
        upload_to=user_district_photo_upload_path, blank=True, null=True
    )
    description = models.TextField(
        max_length=3000, null=True, blank=True)
    params = JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator_using_name(self)
        super().save(*args, **kwargs)


class DistrictRegion(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    district = models.ForeignKey(
        "District",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    state = models.ForeignKey(
        "States",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    country = models.ForeignKey(
        "Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    city = models.ForeignKey(
        "City",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    photo = models.FileField(
        upload_to=user_district_region_photo_upload_path, blank=True, null=True
    )
    pincode = models.ManyToManyField(
        "Pincode",
        blank=True,
    )
    description = models.TextField(max_length=3000, null=True, blank=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    params = JSONField(null=True, blank=True, default=dict)
    latitude = models.DecimalField(max_digits=22,decimal_places=16,blank=True,null=True)
    longitude = models.DecimalField(max_digits=22,decimal_places=16,blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator_using_name(self)
        if not self.latitude and not self.longitude:
            if self.city:
                from geopy.geocoders import Nominatim
                from geopy.distance import geodesic
                app = Nominatim(user_agent="Inavihs",timeout=3)
                name = f"{self.name}, {self.city.name}"
                if app.geocode(name):
                    coordinates = app.geocode(name)
                    city_coardinates = app.geocode(self.city.name)
                    city = (city_coardinates.latitude,city_coardinates.longitude)
                    region = (coordinates.latitude, coordinates.longitude)
                    if int(geodesic(city, region).km) > 50:
                        pass
                    else:
                        self.latitude = coordinates.latitude
                        self.longitude = coordinates.longitude
        super().save(*args, **kwargs)
