py-gmail
========

python script to send email to a gmail id

Requirements
============

* This script requires the gmail id of sender and the password of the id
* If you don't have 2 step verification activated in your gmail account then just replace all the required information in 
  script with your desired information
* If 2 step verification settings is enabled for your gmail id then generate an "Application Specific Password" for "SMTP"
      * Go to https://support.google.com/mail/answer/1173270?hl=en and click on the link  Authorizing applications & sites         page
      * At the bottom - in the "generate application specific password" section, in the name field type SMTP and generate         the password just copy and paste the generated password in the password variable in the script
        For eg : if your generated password is "bfowdafbynfwfgmz" , then paste this password in the password variable of 
                 the script password = "bfowdafbynfwfgmy" and this will be the password for your gmail id if "You have 2                   step verification activated"
