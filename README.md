**WARNING**: This program can damage your files! My recommendation is to read the guides and only run it on a virtual machine ***at your own risk***. I cannot be hold responsible for any file damage due to running this file on any machine.

# Simple Python Ransomware
![Generic badge](https://img.shields.io/badge/Version-1.0.0-RED.svg)

According to [**McAffe**](https://www.mcafee.com/enterprise/en-us/security-awareness/ransomware.html#:~:text=Ransomware%20is%20malware%20that%20employs,a%20victim's%20information%20at%20ransom.&text=A%20ransom%20is%20then%20demanded,quickly%20paralyze%20an%20entire%20organization. "McAffe"):
> Ransomware is malware that employs encryption to hold a victim's information at ransom. 

**Simple Python Ransomare** is a simple tool built in Python that does exactly that, in under 100 lines of code. This highlights both the power of Python, but also the the ease of building such a virus.

## Prerequisites
**Simple Python Ransomare** is build in under 100 lines of code, mostly thanks to packages [Cryptography](https://cryptography.io/en/latest/ "cryptography") (`pip install cryptography`) && [python-dotenv](https://github.com/theskumar/python-dotenv "python-dotenv"), but also other packages (argparse, getpass, os, pathlib, smtplib, platform, email).

Before you begin, ensure you have met the following requirements:
* You have [Python 3.X.X](https://www.python.org/downloads/ "Python 3.X.X") installed
* You have a Gmail account set to [allow less secure apps](https://support.google.com/accounts/answer/6010255?hl=en "allow less secure apps")
* You have read the guide from bellow

## Installing Simple Python Ransomware
To install **Simple Python Ransomare**, follow these steps:
```
git clone <repo> && cd <repo-name>
pip3 install -r requirements.txt
```
## Using Simple Python Ransomware
**Simple Python Ransomare** is used both to encrypt and to decrypt files. Before running the script, head over to the `.env` file and update the following lines using your own information:
```
gmail_account='<YOUR_GMAIL_ADDRESS>'
gmail_password='<YOUR_GMAIL_PASSWORD>'
```
#### Ecryption Mode
After saving the file, you can run the script in the **encryption mode** by typing:
```
python3 ransomware.py --directory <DIRECTORY_NAME> [optional] --backup [optional]
```
Where:
* `--directory` or `-d` takes as an parameter a string, which is the Location / Folder you are targeting (ie. Desktop, Downloads etc.). If letft blank, **Simple Python Ransomare** will automatically target the Desktop. For specific subirectories, specify the main directory first (ie. `python3 ransomware.py --d Downloads/Subdirectory `).

* `--backup` or `-b` doesn't take any parameter and is used to bypass the deletion of the cryptographic key from the system. If used, the key will be stored in the same directory as `ransomware.py`

**ATTENTION**! The program will encrypt ALL files in thetargeted directory and its subdirectories. **The encryption key is set to delete** after the script completes! This can lead to poossible file damage or loss. **USE AT YOUR OWN RISK**!

If successful, the script will:
:ballot_box_with_check: Encrypt all the files 
:ballot_box_with_check: Send an email with the cryptoghraphic key to your gmail account.

#### Decryption Mode
In order to decrypt the files encrypted before, all you need to do is to pass the cryptographic key as a string to the program, as follows:
```
python3 ransomware.py --key <YOUR_CRYPTOGHRAPHIC_KEY>
```
You can retriev the cryptographic key either from the email sent before, or from the `cryptographic_key.key` file, if you used the `--backup` argument.

**ATTENTION**! The directory should be also specified using the `-d `argument, provided that it was used to encrypt files in directories other that Desktop.

## Screenshots
##### The 'Downloads' folder before the encryption
![before_encryption](https://user-images.githubusercontent.com/43548656/152325073-a56f5b26-be40-4719-8fa6-254ca941d04c.gif)
#####  Running encryption on Downloads:
```
python3 ransomware.py -d Downloads  
```
Email received by attacker:
![email_received](https://user-images.githubusercontent.com/43548656/152325898-8f57e21e-39ca-42d5-a209-3bc841caf57f.png)

Files encrypted on all levels under 'Downloads':
![after_encryption](https://user-images.githubusercontent.com/43548656/152326088-6f26a1ac-402d-4200-9e51-f30d06473b7a.gif)

#####  Running decryption on Downloads:
```
python3 ransomware.py --key 70ZAg0MsYFtoXckQa-T1mydyZja3zdKJaOj8pZr8ypE= -d Downloads
```
**[ ! ]** Note that the key is the same one received in the email. In a real world scenario, the attacker would have to deliver the key to the victim in order to decrypt the files.

Files decrypted on all levels under 'Downloads':
![before_encryption](https://user-images.githubusercontent.com/43548656/152325073-a56f5b26-be40-4719-8fa6-254ca941d04c.gif)
