# Global business error handler
# Example
# access to /api/get_images, would get a error with message in json format
# access to /api/get_images?number=5, would get a sucess response

class InvalidAPIError(Exception):
    status_code = 0

    def __init__(self, message="Unknow Error", status_code=0):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        rv['error'] = self.status_code
        return rv