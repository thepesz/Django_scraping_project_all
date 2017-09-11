from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^stats/$', views.Word_freqListView.as_view(), name='subjects_list'),
    url(r'^Kamil_Chudy/$', views.User1ListView.as_view(), name='subjectsss_list'),
    url(r'^Jacek_Chmielewski/$', views.User2ListView.as_view(), name='subjectssss_list'),
    url(r'^Janusz_Gądek/$', views.User3ListView.as_view(), name='subjectsssss_list'),
    url(r'^Łukasz_Piłatowski/$', views.User4ListView.as_view(), name='subjectssssss_list'),
    url(r'^Andrzej_Piasecki/$', views.User5ListView.as_view(), name='subjectsssssss_list'),
    url(r'^Krzysztof_Krzysztofik/$', views.User6ListView.as_view(), name='subjectssssssss_list'),
    url(r'^Michał_Gryczka/$', views.User7ListView.as_view(), name='subjectsssssssss_list'),
    url(r'^Robert_Olejnik/$', views.User8ListView.as_view(), name='subjectssssssssss_list'),
    url(r'^Marta_Kozieł/$', views.User9ListView.as_view(), name='subjectsssssssssss_list'),
    url(r'^Paweł_Montwiłł/$', views.User10ListView.as_view(), name='subjectssssssssssss_list'),
]