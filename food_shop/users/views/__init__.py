from users.views.address_views import CreateAddress
from users.views.client_views import (EnterCodeView, EnterPhoneNumberView,
                                      logout_user, resend_code)
from users.views.profile_views import ProfileView, ProfieEditView


__all__ = [
    'CreateAddress',
    'EnterCodeView',
    'EnterPhoneNumberView',
    'logout_user',
    'resend_code',
    'ProfileView',
    'ProfieEditView'
]
