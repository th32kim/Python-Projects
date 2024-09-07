from Zillow_Scrape import Zillow_Scrape
from google_Form import Google_Form_Interaction
GOOGLE_FORM_URL ='https://docs.google.com/forms/d/e/1FAIpQLSeHokBb4i6vYIJXagcEFbQnnaHc2XCJicCq63TPogOk-eNAcQ/viewform?usp=sf_link'
ZILLOW_URL = 'https://www.zillow.com/san-francisco-ca/rentals/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.536739%2C%22east%22%3A-122.32992%2C%22south%22%3A37.707608%2C%22north%22%3A37.842914%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A666779%7D%7D%2C%22isListVisible%22%3Atrue%7D'
GOOGLE_FORM_RESULT = 'https://docs.google.com/forms/d/1S97jS2uv3mtpFW-krv-UUHu-VzVmCcSlTTqmeyiErPA/edit#responses'

web_scrape = Zillow_Scrape(ZILLOW_URL)
urls = web_scrape.link_list[0:5]
addresses = web_scrape.address_list[0:5]
prices = web_scrape.price_list[0:5]

web_bot = Google_Form_Interaction(GOOGLE_FORM_URL, addresses, prices, urls, GOOGLE_FORM_RESULT)