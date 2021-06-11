import time
import os


def error_log(exception_):
    named = time.localtime()
    time_string = time.strftime("%m-%d-%Y_%H-%M", named)
    path = r'logs'  # to logs folder
    file_name = 'error_log_%s.txt' % time_string
    file = os.path.join(path, file_name)
    file = open(file, "a")  # creates the new file if not exists
    file.write(str(exception_))  # write the exception on the new file
    file.close()
