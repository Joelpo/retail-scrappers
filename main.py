# Main method: gets links and outputs product information.
# Linking google sheets to python scripts in order to store and gather information from GSheetsFiles
# Takes the links in sheet 1 and outputs the prices and names in sheet2.
# @Joelpo

from retailer_scrapper import getDartyInfo, getAmazonInfo, getFnacInfo
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

# first we need to set scope and connect to G-Sheets
scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

# client = gspread.oauth()
creds = ServiceAccountCredentials.from_json_keyfile_name('retail-scrappers-672af2654900.json',scope)
client = gspread.authorize(creds)

spreadSheet = client.open('python-scrapper')

#Sheet 1 contains links
sheet1 = spreadSheet.get_worksheet(0)

#Sheet 2 contains results
sheet2 = spreadSheet.get_worksheet(1)

## MAIN METHOD
def main():
    today = date.today()
    print("Today's date:", today)

    links = getLinks()
    print('The links are {}'.format(links))
    for link in links:
        updateResults(getAmazonInfo(link))

# updates sheet2 with the scrapped information and timestamp
# format ['time_stamp', 'product_name','price']
def updateResults(result):
    print('updating result : {}'.format(result))
    len = len(sheet2.col_values(1))
    sheet2.update_cell(len+1,1,result[0])
    sheet2.update_cell(len+1,2,result[1])

# returns a list of links to scrape
def getLinks():
    print('getting links')
    links = sheet1.col_values(1)
    links.remove("Links")
    return links

if __name__ == '__main__':
    main()
