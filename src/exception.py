import sys
#sys module provides access to variables and functions that interact closely with Python interpreter and runtime environment. It allows developers to manipulate various aspects of program execution and interpreter itself.
import logging
from src import logger

def error_message_detail(error, error_detail:sys): #error_detail will be present inside the sys module
    _,_,exc_tb = error_detail.exc_info() #exc_info() returns a tuple containing information about the exception that is currently being handled.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message