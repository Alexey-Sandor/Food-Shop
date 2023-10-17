from django.urls import path
from django.views.generic import TemplateView
from users import views

app_name = 'users'


urlpatterns = [
    path('login/', views.EnterPhoneNumberView.as_view(), name='login'),
    path('login/confirm', views.EnterCodeView.as_view(), name='confirm'),
    path('logout/', views.logout_user, name='logout'),
    path('privacy-policy', TemplateView.as_view(
        template_name='users/privacy_policy.html'), name='privacy-policy'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('resend-code/', views.resend_code, name='resend_code'),
    path('add-address/', views.CreateAddress.as_view(), name='add-address'),
    path('profile/edit/', views.ProfieEditView.as_view(), name='profile-edit'),
]
