
from django.conf import settings
from django.contrib import auth
from django.utils import timezone

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current user
        user = auth.get_user(request)

        # Check if the user is logged in
        if user.is_authenticated:
            # Get the user's last activity time from the session
            last_activity = request.session.get('last_activity')

            # If there's no last activity time in the session, set it to the current time
            if not last_activity:
                request.session['last_activity'] = timezone.now()

            # Calculate the elapsed time since the user's last activity
            elapsed_time = timezone.now() - request.session['last_activity']

            # If the elapsed time is greater than the logout time, log the user out
            if elapsed_time.seconds > settings.AUTO_LOGOUT_TIME:
                auth.logout(request)

            # Update the last activity time in the session
            request.session['last_activity'] = timezone.now()

        # Call the next middleware or view in the chain
        response = self.get_response(request)
        return response