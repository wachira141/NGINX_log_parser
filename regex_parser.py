#!/usr/bin/env python3
import re


def parser(logger_string):
    '''parse a string with regex pattern matching
    '''
    
    regex_pattern_format = (
        #r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
        r'(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
        r'\s*\[(?P<date>\d+\-\d+\-\d+\s*\d+:\d+:\d+\.\d+)\]\s*',
        r'\"\s*(?P<resource>\S+\s*\S+\s*\S+)\"',
        r'\s*(?P<status_code>\d+)\s*',
        r'\s*(?P<file_size>\s*\d+\s*)\s*'
       )
    
    ip_address = regex_pattern_format[0]
    date_t = regex_pattern_format[1]
    resource = regex_pattern_format[2]
    status_code = regex_pattern_format[3]
    file_t = regex_pattern_format[4]

    log_format = '^{} \-\- {}{}{}{}$'.format(ip_address, date_t, resource, status_code, file_t)

    x = re.fullmatch(log_format, logger_string)

    print(x.group('ip_address'), flush=True)
    print(x.group('date'))
    print(x.group('resource'), flush=True)
    print(x.group('status_code'), flush=True)
    print(x.group('file_size'), flush=True)
