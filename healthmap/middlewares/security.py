# Sets Custom Middlewares to be used within a authenticated session objects
from django.core.exceptions import SucpiciousOperation


class OwnerVerificationMiddleware:
    """ Verifies the created_by id is always set same as request.user. The user
    must be an authenticated user instance.
    """

    def __init__(self, get_response):
        # One Time initiation
        self.get_response = get_response

    def __call__(self, request):
        # Check if the method is POST (CREATE) PUT (Update) or PATCH (Partial)
        if request.method in "POST,PUT,PATCH":
            # Check if the Request Body has creadted_by attribute
            if 'created_by' in request.body:
                # Check if current session user matches the created_by attrib
                if request.user != request.body.get('created_by'):
                    raise SucpiciousOperation(
                        'created_by is modified externally')

        response = self.get_response(request)
        return response
