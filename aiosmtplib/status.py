'''
SMTP status codes, as constants for code readability.
'''
SMTP_211_SYSTEM_STATUS_OK = 211
SMTP_214_HELP_MESSAGE = 214
SMTP_220_READY = 220
SMTP_221_CLOSING = 221
SMTP_235_AUTH_SUCCESSFUL = 235
SMTP_250_COMPLETED = 250
SMTP_251_WILL_FORWARD = 251
SMTP_252_CANNOT_VRFY = 252
SMTP_334_AUTH_CONTINUE = 334
SMTP_354_START_INPUT = 354
SMTP_421_DOMAIN_UNAVAILABLE = 421
SMTP_450_MAILBOX_UNAVAILABLE = 450
SMTP_451_ERROR_PROCESSING = 451
SMTP_452_INSUFFICIENT_STORAGE = 452
SMTP_500_UNRECOGNIZED_COMMAND = 500
SMTP_501_UNRECOGNIZED_PARAMETERS = 501
SMTP_502_COMMAND_NOT_IMPLEMENTED = 502
SMTP_503_BAD_COMMAND_SEQUENCE = 503
SMTP_504_PARAMETER_NOT_IMPLEMENTED = 504
SMTP_521_DOMAIN_DOES_NOT_ACCEPT_MAIL = 521
SMTP_530_ACCESS_DENIED = 530  # Sendmail specific
SMTP_550_MAILBOX_DOES_NOT_EXIST = 550
SMTP_551_USER_NOT_LOCAL = 551
SMTP_552_STORAGE_EXCEEDED = 552
SMTP_553_MAILBOX_NAME_INVALID = 553
SMTP_554_TRANSACTION_FAILED = 554
SMTP_555_SYNTAX_ERROR = 555


def is_success_code(code):
    return 200 <= code < 300


def is_temporary_error_code(code):
    return 400 <= code < 500


def is_permanent_error_code(code):
    return 500 <= code < 600
