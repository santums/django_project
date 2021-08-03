from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    #Escalation Details
    path('escadd/', views.esc_upload, name='upload_em'),
    path('escmat/',views.searchesc, name = 'search-em'),
    path('escedit/',views.show1, name = 'search-escedit'),
    path('editesc/<int:id>',views.editesc, name = 'search-edit'),
    path('delete/<int:id>',views.destroy, name = 'search-delete'),
    path('update/<int:id>',views.update, name = 'search-update'),
    #SOP
    path('sops/', views.sop_list, name='sop_list'),
    path('sop_upload/', views.upload_sop, name='upload_sop'),
    path('sopedit/',views.show, name = 'search-sopedit'),
    path('editsop/<int:id>',views.editsop, name = 'search-editsop'),
    path('deletesop/<int:id>',views.destroysop, name = 'search-deletesop'),
    path('updatesop/<int:id>',views.updatesop, name = 'search-updatesop'),
    #training docs
    path('docs/', views.train_doc, name='training_list'),
    path('train_upload/', views.upload_train, name='upload_train'),
    path('train_edit/',views.train_edit, name = 'train_edit'),
    path('deletetrain/<int:id>',views.destroytrain, name = 'deletetrain'),
    #Shift images
    path('roster/', views.shift_img, name='shift_roster'),
    path('shift_upload/', views.upload_shift, name='upload_shift'),
    path('shift_edit/',views.shift_edit, name = 'shift_edit'),
    path('editshift/<int:id>',views.editshift, name = 'search-editshift'),
    path('deleteshift/<int:id>',views.destroyshift, name = 'deleteshift'),
    path('updateshift/<int:id>',views.updateshift, name = 'search-updateshift'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
