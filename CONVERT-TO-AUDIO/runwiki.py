'''
Wikipedia Text To Audio Program
# Wikipedia: Python thrid-party library that makes it easy to access and parse data from Wikipedia
'''

import wikipedia

# To get the summary of a title 
# result = wikipedia.summary('Egypt', sentences=2)

# To search title and suggestions
# result = wikipedia.search('Japan', results= 10)

# To change the language of the wikipedia page
wikipedia.set_lang('ja')
result = wikipedia.summary('Atari', sentences=4)
print(result)
