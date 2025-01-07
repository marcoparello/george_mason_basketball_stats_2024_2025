# import html from lxml
from bs4 import BeautifulSoup
# import requests
import requests
# import regular expressions for text processing
import re


def get_omnirankings(url1,url2,wbb_or_mbb):
    print("Mason's chances of winning against each opponent and projected record via Omni Rankings\n")
    # Put headers to bypass security
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
    page = requests.get(url1,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # if womens
    if(wbb_or_mbb == "wbb"):
        td_element = soup.find_all('td',class_='xl13016044')
        # get the win percentages
        percentages = [td.text.strip() for td in td_element if '%' in td.text]
        # for some reason Towson had a different ID on the website than the other competitors
        td_elements_class1 = soup.find_all('td', class_='xl10116044')
        td_elements_class2 = soup.find_all('td',class_='xl10216044')
        # get the opponents
        opps1 = [td.find('span').text for td in td_elements_class1 if td.find('span') is not None]
        opps2 = [td.find('span').text for td in td_elements_class2 if td.find('span') is not None]
        opps = opps1 + opps2
        # get the projected record
        td_elements_projected = soup.find( 'span', style='mso-spacerun:yes')
        projected_record = td_elements_projected.next_sibling
        # correct projected record as there is a newline in "Projected season record: 24 - 4 overall, 15\n  - 3 A-10"
        corrected_projected_record = re.sub(r"\s*\n\s*", " ", projected_record)

        # for some reason the website does not list the percentages before Mount St Mary's
        opps_with_percentages = opps[4:-1]
        
        # Print win percentages
        print("\t \t RECORD PREDICTIONS")
        for i in range(len(opps_with_percentages)):
            print(f" Mason's chance of winning against {opps_with_percentages[i]} is {percentages[i]}\n")
        # Print projected record
        print(f" {corrected_projected_record}")
        
        # find NCAA tournament chances
        page = requests.get(url2,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        team_name = "George Mason"
        # Find specific column that contains George Mason data
        for row in soup.find_all("tr"):
            if team_name in row.get_text():
                team_row = row
                break
        
        # if team row is found, extract the seeding and percentages    
        try:
            print("\n \t \t TOURNAMENT PREDICTIONS")

            if team_row:
                # extract the seeding from the top row
                seeding = team_row.find("td", class_="xl7726690").text.strip()

                print(f"George Mason is predicted to be in the NCAA tournament as an {seeding} seed:\n")
                # Extract percentages from the specific row

                percentages = [td.text for td in team_row.find_all("td", class_="xl9026690")]
            
            # print NCAA tournment chances
            print(f"George Mason's chances of reaching the Round of 32 in the NCAA tournament are: {percentages[0]}\n")
            print(f"George Mason's chances of reaching the Sweet Sixteen in the NCAA tournament are: {percentages[1]}\n")
            print(f"George Mason's chances of reaching the Elite Eight in the NCAA tournament are: {percentages[2]}\n")
            print(f"George Mason's chances of reaching the Final Four in the NCAA tournament are: {percentages[3]}\n")
            print(f"George Mason's chances of reaching the National Championship in the NCAA tournament are: {percentages[4]}\n")
            print(f"George Mason's chances of winning the National Championship in the NCAA tournament are: {percentages[5]}")
        # if team row is not found, print error message
        except:

            print("\n George Mason is not predicted to be in the NCAA tournament\n")
    else:
        #if mens
        # find the td elements that contain the win percentages
        td_element = soup.find_all('td',class_='xl12512650')
        # get the win percentages
        percentages = [td.text.strip() for td in td_element if '%' in td.text]
        #For some reason NC Central is not listed in the same class as the other opponents
        td_elements_class1 = soup.find_all('td', class_='xl10212650')
        td_elements_class2 = soup.find_all('td',class_='xl10312650')
        # get the opponents
        opps1 = [td.find('span').text for td in td_elements_class1 if td.find('span') is not None]
        opps2 = [td.find('span').text for td in td_elements_class2 if td.find('span') is not None]
        opps = opps1 + opps2
        # get the projected record
        td_elements_projected = soup.find( 'span', style='mso-spacerun:yes')
        projected_record = td_elements_projected.next_sibling
        # correct projected record as there is a newline in "Projected season record: 24 - 4 overall, 15\n  - 3 A-10"
        corrected_projected_record = re.sub(r"\s*\n\s*", " ", projected_record)

        # for some reason the website does not list the percentages before East Carolina
        opps_with_percentages = opps[5:-1]
        
        # Print win percentages
        print("\t \t RECORD PREDICTIONS")
        for i in range(len(opps_with_percentages)):
            print(f" Mason's chance of winning against {opps_with_percentages[i]} is {percentages[i]}\n")
        # Print projected record
        print(f" {corrected_projected_record}")
        
        # find NCAA tournament chances
        page = requests.get(url2,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        team_name = "George Mason"
        # Find specific column that contains George Mason data
        for row in soup.find_all("tr"):
            if team_name in row.get_text():
                team_row = row
                break
        
        # if team row is found, extract the seeding and percentages    
        try:
            print("\n \t \t TOURNAMENT PREDICTIONS")

            if team_row:
                # extract the seeding from the top row
                seeding = team_row.find("td", class_="xl7726690").text.strip()

                print(f"George Mason is predicted to be in the NCAA tournament as an {seeding} seed:\n")
                # Extract percentages from the specific row

                percentages = [td.text for td in team_row.find_all("td", class_="xl9026690")]
            
            # print NCAA tournment chances
            print(f"George Mason's chances of reaching the Round of 32 in the NCAA tournament are: {percentages[0]}\n")
            print(f"George Mason's chances of reaching the Sweet Sixteen in the NCAA tournament are: {percentages[1]}\n")
            print(f"George Mason's chances of reaching the Elite Eight in the NCAA tournament are: {percentages[2]}\n")
            print(f"George Mason's chances of reaching the Final Four in the NCAA tournament are: {percentages[3]}\n")
            print(f"George Mason's chances of reaching the National Championship in the NCAA tournament are: {percentages[4]}\n")
            print(f"George Mason's chances of winning the National Championship in the NCAA tournament are: {percentages[5]}")
        # if team row is not found, print error message
        except:

            print("\n George Mason is not predicted to be in the NCAA tournament\n")

  


