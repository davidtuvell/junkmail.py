import imapclient

i = imapclient.IMAPClient('imap-mail.outlook.com')
i.login('USER@outlook.com', 'PASSWORD;')


#INBOX Handler
i.select_folder('INBOX')

##SUBJECT Filters
uids = i.search(['SUBJECT', 'YourSearchString'])
i.delete_messages(uids)

##FROM Filters
uids = i.search(['FROM', 'YourSearchString'])
i.delete_messages(uids)

##TEXT Filters Include Body and Subject
uids = i.search(['TEXT', 'YourSearchString'])
i.delete_messages(uids)


#JUNK Folder Handler
i.select_folder('JUNK')

##SUBJECT Filters
uids = i.search(['SUBJECT', 'YourSearchString'])
i.delete_messages(uids)

##FROM Filters
uids = i.search(['FROM', 'YourSearchString'])
i.delete_messages(uids)

##TEXT Filters Include Body and Subject
uids = i.search(['TEXT', 'YourSearchString'])
i.delete_messages(uids)


#END of Filters Now Clean Up
i.expunge()
i.logout()
