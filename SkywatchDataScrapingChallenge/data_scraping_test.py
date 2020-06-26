# Test to see how long it takes me to get list of datasources from skywatch.com
# Note: Comments explaining my procedure were added after I had written the code 

# Started with this tutorial: 
#https://docs.python-guide.org/scenarios/scrape/

from lxml import html
import requests

page = requests.get('https://www.skywatch.co/data')
tree = html.fromstring(page.content)

# Inspected the above web page in chrome, saw that all data sources had id='contact Subhead'
# Reasoned out the text required in tree.xpath based on two examples in the tutorial 
providers = tree.xpath('//p[@id="contactSubhead"]/text()')

# Print the list of all data providers 
for pro in providers:
    print(pro)
    
########################################
# Completed it in 6 minutes, 17 seconds#
########################################
    
# Limitations of this approach
    # Assumes the HTML structure will not change in the future (divs, spans, ids, etc.)
    
# Try counting number of views on Youtube Playlists 
from selenium import webdriver
browser = webdriver.Firefox()   
browser.get('https://youtube-playlist-analyzer.appspot.com/')