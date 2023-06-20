from django.urls import path
from . import views


urlpatterns = [
     path('jumbo/', views.get_jumbo, name='jumbo'),
     path('me/', views.get_me, name='about-me'),
     path('works-todo/',
          views.get_works_todo, name='works'),
     path('projects/',
          views.get_all_projects, name='projects'),
     path('contact-us/',
          views.get_contacted, name='contact_us'),
     path('social-media/',
          views.get_social_media, name='social_media'),
     path('progress-bar/',
          views.get_progress_bar, name='progress'),
     path('technologies/',
          views.get_technologies_icon, name='technologies_icons'),
     path('testimonials-list/',
         views.get_testimonials, name='testimonials'),
     path('reach-me/',
         views.reach_me_form, name='reach_me_form'),
]
