from django.urls import path
from referral import views as referral_views


urlpatterns = [
    path('', referral_views.index.as_view(), name='home'),
    path('api/programs/', referral_views.program_list),
    path('api/staff/', referral_views.staff_list),
    path('api/programs/<int:pk>/', referral_views.program_detail),
    path('api/referrals/', referral_views.referral_list),
    path('api/referrals/program/<int:pk>/', referral_views.referral_list_by_program)
]