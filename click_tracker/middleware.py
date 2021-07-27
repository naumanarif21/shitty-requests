from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden


class IPWhitelistMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        ip_address = request.META.get('HTTP_X_REAL_IP', request.META.get('REMOTE_ADDR'))

        if not request.META.get('REMOTE_ADDR', ''):
            request.META['REMOTE_ADDR'] = ip_address

        response = self.get_response(request)

        return response
