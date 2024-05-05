from django.urls import path

from myapp.views import(
    homepage,
    account_verification,
    main_portal,
    resend_otp,
    simple_login,
    voter,
    create_user,
    vote_casting,
    watch_video,
    contact_page,
    complete,
    ecp_overview,
    registration,
    verify_registration,
    check_registration,
    detail,
    double_verification
    )
urlpatterns = [
    path('ECP/',homepage),
    path('verify_registration/',verify_registration),
    path('verify_registration/ECP_overview/',ecp_overview),
    path('verify_registration/registration/',registration),
    path('verify_registration/verify_registration/',double_verification),
    path('registration/',registration),
    path('ECP_overview/',ecp_overview),
    path('login_verification/Admin/complete_data/',complete),
    path('contact/',contact_page),
    path('watch_video/',watch_video),
    path('Account_verification/main_portal/cast_vote/',vote_casting),
    path('Account_verification/main_portal/cast_vote/send_detail/',detail),
    path('Account_verification/',account_verification),
    path('Account_verification/otp_reverification/',resend_otp),
    path('Account_verification/main_portal/',main_portal),
    path('login/',simple_login),
    path('login/main_portal/',main_portal),
    path('login/main_portal/cast_vote/',vote_casting),
    path('login/main_portal/cast_vote/send_detail/',detail),
    path('login/send_detail/',detail),
    path('login_verification/Admin/',voter),
    path('login_verification/Admin/check_registration/',check_registration),
    path('login_verification/',create_user)
]
 