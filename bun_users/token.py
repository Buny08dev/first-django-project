# prarol:
# zcpt fdiq xnfu ilcn

from django.contrib.auth.tokens import PasswordResetTokenGenerator

class EmailGenerator(PasswordResetTokenGenerator):
    pass

account_activation_token=EmailGenerator()
account_activation_token.make_token()
# account_activation_token.check_token()