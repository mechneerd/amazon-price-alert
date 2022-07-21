from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.in/realme-narzo-Mint-Green-Storage/" \
      "dp/B09FKDH6FS/ref=sr_1_3?brr=1&qid=1658378372&rd=1&sr=8-3&th=1"
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Accept-Language': 'en-US,en;q=0.5'
}
my_email = 'email@gmail.com'
my_password = "urpassword"


rp = requests.get(url=url, headers=header)
data = rp.text


alert_price = float(input('price needed for alert : '))

soup = BeautifulSoup(data, "html.parser")
price_tag = soup.find(name="span", class_="a-offscreen")
price_string = price_tag.string[1:]

price = price_string.replace(',', '')
price = float(price)

if price <= alert_price:
    r = smtplib.SMTP("smtp.gmail.com")
    r.starttls()
    r.login(user=my_email, password=my_password)
    r.sendmail(msg=f"subject:amazon alert\n\n "
                   f"Your price is below the set price ₹{alert_price} order now!\n {url} ",
               from_addr=my_email, to_addrs='targetmailid')
