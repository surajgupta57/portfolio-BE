from django.db import models

from portfolioApi.utils import aboutme_upload_logo, cv_upload_path, jumbo_upload_image, project_upload_logo, service_upload_icon, skill_logo_upload_path, testimonial_upload_photo

class Base(models.Model):
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    weight = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(null=True, auto_now=True, blank=True)



class ContactMe(Base):
    icon = models.CharField(max_length=200, blank=True, null=True, verbose_name="Icon (eg: fa -fa-twitter)")
    contact_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Contact Name (eg: twitter)")
    contact_info = models.CharField(max_length=100, blank=True, null=True, verbose_name="Contact Info (eg: johndoe@gmail.com)")

    class Meta:
        verbose_name_plural = 'Contacts Section'

    def __str__(self):
        return self.contact_name

class Jumbo(Base):
    heading = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Full Name")
    job_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    jumbo_img = models.ImageField(
        upload_to=jumbo_upload_image,
        blank=True,
        null=True,
    )
    contact = models.ForeignKey(ContactMe, on_delete=models.SET_NULL, null=True, blank=True)
    cv_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Jumbo Section"
        verbose_name_plural = 'Jumbo Section'

    def __str__(self):
        return self.name


class SkillSection(Base):
    language = models.CharField(max_length=40, blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(
        upload_to=skill_logo_upload_path, blank=True, null=True
    )

    class Meta:
        verbose_name_plural = 'Skills Section'

    def __str__(self):
        return self.language

class Project(Base):
    technology = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(
        upload_to=project_upload_logo,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=90, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Projects Section'

    def __str__(self):
        return self.title

class LanguageIcons(Base):
    code = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Languages Icons'

    def __str__(self):
        return self.code

class ServicesOffred(Base):
    icon = models.ImageField(
        upload_to=service_upload_icon,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=40, blank=True, null=True)
    shadow_icon = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Services Section'

    def __str__(self):
        return self.name



class SocialMediaLinks(Base):
    name = models.CharField(max_length=80, blank=True, null=True)
    icon = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Icon (eg: bi-envelope)")
    link = models.URLField(blank=True, null=True),

    class Meta:
        verbose_name_plural = 'Social Media Links'

    def __str__(self):
        return self.icon


class ResumeUpload(Base):
    cv = models.FileField(
        upload_to=cv_upload_path,
        blank=True,
        null=True,
    )
    def __str__(self):
        return str(self.id)


class AboutMeSection(Base):
    heading = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(
        upload_to=aboutme_upload_logo,
        blank=True,
        null=True,
    )
    cv = models.ForeignKey(ResumeUpload, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'About Me Section'

    def __str__(self):
        return self.heading



class ReachOutForm(Base):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_no = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    query = models.TextField(max_length=10000, null=True, blank=True)
    ad_source = models.CharField(max_length=100, blank=True, null=True)
    client_ip = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reach Out Form'
        verbose_name_plural = 'Reach Out Form'

    def __str__(self):
        return f"{self.name.title()}"


class Testimonial(Base):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to=testimonial_upload_photo,
        blank=True,
        null=True,
    )
    company = models.CharField(max_length=100)
    content = models.TextField()
    ratings = models.PositiveIntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ['-weight']