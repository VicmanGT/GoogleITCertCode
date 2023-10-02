#!/usr/bin/env python3
import re
import operator
import csv
error_msg={}
usr_entry={}
with open ("syslog.log") as file:
        for line in file:
                error_ptrn = r"ERROR ([a-zA-Z' ]+) \(([a-z.]+)\)"
                info_ptrn = r"INFO ([a-zA-Z ]+) \[#[\d]+\] \(([a-z.]+)\)"
                error_result = re.search(error_ptrn, line)
                info_result = re.search(info_ptrn, line)
                if error_result is not None:
                        if error_result.group(1) not in error_msg:
                                error_msg[error_result.group(1)] = 1
                        else:
                                error_msg[error_result.group(1)] +=1
                        if error_result.group(2) not in usr_entry:
                                usr_entry[error_result.group(2)]=[0,1]
                        else:
                                usr_entry[error_result.group(2)][1] +=1
                if info_result is not None:
                        if info_result.group(2) not in usr_entry:
                                usr_entry[info_result.group(2)] = [1,0]
                        else:
                                usr_entry[info_result.group(2)][0] +=1
order_error_msg = sorted(error_msg.items(), key=operator.itemgetter(1), reverse=True)
list_usr_entry = []
for i in usr_entry:
    list_usr_entry.append(i)
    for j in usr_entry[i]:
        list_usr_entry.append(j)
i = 0
j = 3
list_tuple_usr_entry = []
for k in range(int(len(list_usr_entry)/3)):
    list_tuple_usr_entry.append(tuple(list_usr_entry[i:j]))
    i += 3
    j += 3
order_usr_entry= sorted(list_tuple_usr_entry)
with open ("error_message.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Error", "Count"])
        writer.writerows(order_error_msg)
with open ("user_statistics.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Username","INFO", "ERROR"])
        writer.writerows(order_usr_entry)




