from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

web_url = 'https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off'

uClient = uReq(web_url) # uReq -> connection open and stored on variable uClient
page_html = uClient.read() # variable send to read function then gather all data that send to variable page_html
uClient.close() # connection is closed
page_soup = soup (page_html, "html.parser") # It's large html file of webpage

containers = page_soup.findAll("div", {"class": "_13oc-S"}) # get from main class from web that hold all the contentainers it also find div tag with the class
# print (len(containers)) # print the length of the containers

# print(soup.prettify(containers[0]))


container = containers[0]
# print(container.div.img["alt"])


price=container.findAll("div",{"class":"_4921Z t0pPfW"}) # price tag get from class
print(price[0].text)



ratings = container.findAll("div",{"class":"niHOFQ"}) # tag show the rating from web
print(ratings[0].text)

filename = "products.csv" # Creating file
f = open(filename,"w")  # Normal convention of f title

headers= "Product_Name, Pricing, Ratings\n" # CSV have headers, so just created manually that hold all info
f.write(headers)

for contrainer in containers: # for loop
    product_name = contrainer.div.img["alt"] # Get product name

    price_container = container.findAll("div", {"class":"col col-5-12 _2o7WAb"}) # set tag price
    price = price_container[0].text.strip() # get price of product

    rating_container = container.findAll("div", {"class":"niHOFQ"}) # set the rating tag
    rating = rating_container[0].text # know the rating of product

    # print("product_name:" + product_name)
    # print("price:" + price)
    # print("ratings:" + rating)

    #string parsing

    trim_price = ''.join(price.split(',')) # splitting the price
    rm_USD = trim_price.split("$")
    add_USD_price = "USD." + rm_USD[1] # price in USD
    split_price = add_USD_price.split('E') # If provide EMI option then need to setup E
    final_price = split_price[0]

    split_rating = ratings.split(" ")
    final_rating = split_rating[0] #

    print(product_name.replace(",", "|") + final_price + "," + final_rating + "\n") # replace function set the comma
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n") # concatenating and file save to the folder

f.close()
