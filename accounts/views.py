
from django.contrib.auth.views import LoginView


class PayrollLoginView(LoginView):
    template_name = "login.html"
