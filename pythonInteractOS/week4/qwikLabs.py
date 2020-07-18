  GNU nano 2.7.4                                                              File: find_error.py

#!/usr/bin/env python3

import re
import os
import sys

def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file :
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()

    return returned_errors

def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)





^G Get Help     ^O Write Out    ^W Where Is     ^K Cut Text     ^J Justify      ^C Cur Pos      ^Y Prev Page    M-\ First Line  M-W WhereIs Next^^ Mark Text
^X Exit         ^R Read File    ^\ Replace      ^U Uncut Text   ^T To Linter    ^_ Go To Line   ^V Next Page    M-/ Last Line   M-] To Bracket  M-^ Copy Text
