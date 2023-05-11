import sys


def error_message_datail(error, error_detail: sys):
    _, _, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error_message [{2}]".format(
        file_name,
        exc_traceback.tb_lineno,
        str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_datail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message