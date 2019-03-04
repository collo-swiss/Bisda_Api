from rest_framework.views import exception_handler


def mesozi_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        errors = []

        for field, value in response.data.items():
            errors.append("{} : {}".format(field, " ".join(value)))

        response.data = {}
        response.data['errors'] = errors
        response.data['status'] = response.status_code

    return response
