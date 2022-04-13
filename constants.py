class BlueprintName:
    """ Blueprint names """
    LOGIN = "login"


class Random:
    SECRET_KEY = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='


class Endpoint:
    """ Route endpoints """
    USER_LOGIN = "UserLogin"
    LOGIN = "Login"
    REGISTER = "Register"
    LOGOUT = "Logout"
    CREATE_ACCOUNT = "create_account"
    NEW_REGISTER = "newRegister"


class HTMLUserDetail:
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    E_MAIL_ID = "E-mail"
    PASSWORD = "password"
    CONTACT_NUMBER = "contact_no"


class DBDetail:
    ID = "_id"
    NAME = "Name"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    E_MAIL_ID = "email"
    PASSWORD = "password"
    CONTACT_NUMBER = "contact_no"
    CREATED_BY = "_created_by"
    CREATED_AT = "_created_at"
    MODIFIED_BY = "_modified_by"
    MODIFIED_AT = "_modified_at"
    DELETED = "_is_deleted"


class Date:
    DEFAULT_FORMAT = "%Y-%m-%dT%H:%M:%S"
    FORMAT_WITH_GMT_TIME_ZONE = "%Y-%m-%dT%H:%M:%SZ"


class HttpStatusCodes:
    # success
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    MULTI_STATUS = 207

    # redirection
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308

    # client error
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    UNSUPPORTED_MEDIA_TYPE = 415
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    LIMIT_EXCEEDED = 429

    # server errors
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504


class HTTP_REQUESTS_CONSTANTS:
    POST = 'POST'
    GET = 'GET'
    HEAD = 'HEAD'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'
    HTTP_STATUS = HttpStatusCodes
    HTTP_PROTOCOL = 'http://'
    HTTPS_PROTOCOL = 'https://'
