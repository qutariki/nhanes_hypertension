import os
from requests import get
from bs4 import BeautifulSoup
from tqdm import tqdm

# create the download directory
if not os.path.isdir("download"): 
    os.makedirs("download") 

# get the webpage
parent_link = "https://wwwn.cdc.gov"
dataset_link = parent_link + "/nchs/nhanes/search/datapage.aspx"
html = get(dataset_link)

# make the soup, find the target table
soup = BeautifulSoup(html.text, features="html.parser")
dt_class = "table table-bordered table-header-light table-striped table-hover table-hover-light nein-scroll"
dt_table = soup.find("table", {"class": dt_class})

relevants = ['BPX', 'BMX', 'DEMO', 'BPQ', 'DIQ', 'SMQ', 'ALQ', 'PAQ']

# parse the table for xpt links and download relevant files
# i've omitted files that had names such as BPX2, etc.
for a in tqdm(dt_table.findAll('a')):
    link = a['href']
    if(".XPT" in link.upper()):
        filename = link.split('/')[-1]
        if any(rel in filename.split('_') for rel in relevants):
            file = get(parent_link+link)
            open("download/" + filename, 'wb').write(file.content)       