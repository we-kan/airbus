
class CorsMiddleware(object):
    """This middleware updates response header for cross origin resource sharing."""

    def process_response(self, request, response):
        """
        This method updates response object for cross origin resource sharing.

        :param request: django request object
        :param response: django request object
        :return: django response object
        """
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST,GET,PUT,DELETE,OPTIONS,PATCH'
        response['Access-Control-Allow-Credentials'] = False
        response['Access-Control-Allow-Headers'] = 'X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept, Authorization'
        if request.method == 'OPTIONS':
            response.status_code = 200
        return response


