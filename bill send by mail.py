import yagmail
import os
import pandas  


sender= 'satyamsingh20942@gmail.com'
yag= yagmail.SMTP(user= sender, password=os.getenv('password'))

subject= "this is your electricity bill"

bill_owner= pandas.read_csv('bill.csv')

for index,row in bill_owner.iterrows():
    
    content= f""" Hi! {row['name']} this is your bill amount {row['bill']} and the bill is attached below \n {row['file']} \n THIS IS A SYSTEM GENERATED MAIL SO DO NOT REPLY !!!"""
    
    yag.send(to= row['email'],subject=subject, contents=content, attachments=row['file'])
    print("Email sent!")