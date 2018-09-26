

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
url(r'^signup/$', views.signup, name='signup'),
	path('',views.index, name='index'),
	path('entreprises/',views.EntrepriseList.as_view(),name='entreprises'),
	path('entreprise/<int:pk>',views.EntrepriseDetail.as_view(),name='entreprise'),
	]
urlpatterns += [ 
    path('activites/',views.ActiviteList.as_view(),name='activites'),
    path('activite/<int:pk>',views.ActiviteDetail.as_view(),name='activite'),
	path('activite/<int:pk>/commentaire/', views.CommentaireCreate.as_view(), name='blog-comment'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
