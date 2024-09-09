# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        email_list = re.split(r'[,\s]+', self.email_addresses)
        
        email_list = [email for email in email_list if email]
        
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        
        valid_emails = [email for email in email_list if email_pattern.match(email)]
        unique_sorted_emails = sorted(set(valid_emails))
        
        return unique_sorted_emails
