# -*- coding: utf-8 -*-
import re

re_email = re.compile(r'^[\w]+?\.?[\w]+?@[\w]+?\.com$')
def is_valid_email(addr):
    if re_email.match(addr):
        return True
    else:
        return False
    

# 测试:
assert is_valid_email('someone@example.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@gmail.com')
print('ok')

re_name_mail = re.compile(r'^<?([\w]+\s*[\w]*)>?\s*[\w]*@[\w]+\.org$')
def name_of_email(addr):
    result = re_name_mail.match(addr)
    if result:
        return result.group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
