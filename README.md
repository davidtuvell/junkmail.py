# junkmail.py
Simple Python script to make certain imap emails disappear. Uses ImapClient.

Shell or terminal "pip install imapclient" to get libraries.

Developed for use with Outlook.com, but should work for most IMAP servers except Gmail. Gmail would require significant changes.

See IMAP Search Fields for other possible filtering features.
I simply create a new entry for each individual filter. There's probably a more elegant way to handle the searches, and also probably a faster way (it's a little slow), but I'm going for simple and stupid here. The idea is not to use much effort adding new entries. All I do is run this script before I open my email, and then I don't have to deal with unwanted clutter or harassment. Works good as of 2019.09.09.
