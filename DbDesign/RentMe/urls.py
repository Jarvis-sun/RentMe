# coding:utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RentMe import views


urlpatterns = {
    url(r'^licenses/$',views.license_list),
    url(r'licenses/(?P<pk>[0-9]+)$',views.license_detail),
    url(r'^model/$',views.model_info_list),
    url(r'^model/(?P<pk>[0-9]+)$',views.model_info_detail),
    url(r'^user/$',views.user_info_list),
    url(r'^user/(?P<pk>[0-9]+)$',views.user_info_detail),
    url(r'^admins/$',views.AdminList.as_view()),
    url(r'^admins/(?P<pk>[0-9]+)$',views.AdminDetail.as_view(),name='admin-detail'),

    #url(r'^stores/$',views.StoreList.as_view()),
    #url(r'^stores/(?P<pk>[0-9]+$)',views.StoreDetail.as_view()),
    #url(r'^cars/$',views.CarList.as_view()),
    #url(r'^cars/(?P<pk>[0-9]+)$',views.CarDetail.as_view()),
    url(r'^login/$',views.login),
}


urlpatterns = format_suffix_patterns(urlpatterns)