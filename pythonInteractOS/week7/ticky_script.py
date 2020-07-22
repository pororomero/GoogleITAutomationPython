#!/usr/bin/env python3

import re
import csv
import operator

errors_dict = {}
users_dict = {}
error_pattern = r"ticky: ERROR ([\w' ]*) "
info_pattern = r"ticky: INFO ([\w ]*) "
user_pattern = r" \(([\w.]*)\)"
with open("syslog.log") as logfile:
    for line in logfile:
        username = re.search(user_pattern, line).groups()[0]
        if username not in users_dict:
            users_dict[username] = {"INFO": 0, "ERROR": 0}
        if "ERROR" in line:
            error = re.search(error_pattern, line).groups()[0]
            errors_dict[error] = errors_dict.get(error, 0) + 1
            users_dict[username]["ERROR"] += 1
        if "INFO" in line:
            info = re.search(info_pattern, line).groups()[0]
            users_dict[username]["INFO"] += 1

# errors_dict = dict(sorted(errors_dict.items(), key=operator.itemgetter(1), reverse=True))
# users_dict = dict(sorted(users_dict.items(), key=operator.itemgetter(0)))

print(errors_dict)
print(users_dict)

# Creating an error message csv file
with open('error_message.csv', 'w') as file:
    file.write("Error,Count\n")
    for key, value in sorted(errors_dict.items(), key=operator.itemgetter(1), reverse=True):
        file.write(key + ',' + str(value) + '\n')
    file.close()

# Creating a user statistics csv file
with open('user_statistics.csv', 'w') as file:
    file.write("Username,INFO,ERROR\n")
    for key, value in sorted(users_dict.items(), key=operator.itemgetter(0)):
        file.write(key + ',' + str(value["INFO"]) + ',' + str(value["ERROR"]) + '\n')
    file.close()
