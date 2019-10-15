#Finding phone number and email in a string using REGEX


import pyperclip
import re

#Regex is short for regular expression and is a module used to locate specific strings
#You can read more about how to write them at:
#https://www.geeksforgeeks.org/write-regular-expressions/

#Creating a regex object for phone numbers:

phoneregex = re.compile(r'''(
	(\d{3}|(\d{3}\))? 
	(\s|-|\.)? 
	(\d{3}) 
	(\s|-|\.) 
	(\d{4}) 
	(\s*(ext|x|ext.)\s*(\d{2,5}))? 
	)''', re.VERBOSE)

#Creating a regex object for emails:


emailregex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ 
	@+ 
	[a-zA-Z0-9.-]+ 
	[\.[a-zA-Z]{2,4}])) 
	)''', re.VERBOSE)

# You can test your own regex at:
#https://www.regexpal.com/


text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8]!=' ':
		phoneNum += ' x' + groups[8]
	matches.append(groups[0])


#TODO :COPY RESULTS TO CLIPBOARD

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email adresses found.')

