from flask import Flask, request, render_template
import pandas as pd
from bs4 import BeautifulSoup
import requests
#import os
#import time

#
# page_link ='https://www.alma.be/nl/restaurant/alma-1'
# # fetch the content from url
# page_response = requests.get(page_link, timeout=5)
# # parse html
# page_content = BeautifulSoup(page_response.content, "html.parser")
#
#
# print (page_content)
#
# links_articles = page_content.find_all("a", {"class": "link-live"})

app = Flask(__name__)


@app.route('/')
def my_form():
    page_link ='https://www.alma.be/nl/restaurant/alma-1'
    #fetch the content from url
    page_response = requests.get(page_link, timeout=5)
    #parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")
    tag = page_content.find("td", text="Kaaskroketten")
    try:
        parent = tag.find_parent('div')
        parent_2 = parent.find_parent('div')
        date = parent_2.findAll("div", {"class": "meta__item-menu"})
        date_text = "Ja! :) op " + date[0].text
        image = "static/images/kaaskroketten_edit.png"
    except AttributeError:
        date_text = "Nee! :("
        image = "static/images/geen_kaaskroketten.png"
    return  """  
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
        <style> 

    .big {
        margin-top:40 px;
        text-align: center;
        font-size: 80px;
          font-weight: bold;
          margin-bottom: 0;
    }
    #kroket {
        margin-top: 20px;

    }
    
    td {
    }
    
    table {
        margin-top: 0;
        text-align: center;
            margin-left:auto; 
    margin-right:auto;
    }
    

    
    p {
    text-align: center;
    }
    
    
    </style> 

    </head>
     <body>
    <p class="big"> Zijn er <u>kaaskroketten</u> in Alma 1?  </p> 
    <table>
        <tr> <td id="test"> </td>
        <td id="test2">
        <p class="big">  %s </p>
    <img src=%s id="kroket"> </td>
        <td id="test3"> </td>
        </tr> 
    </table>
    
    <p> Meer weten? <a href="https://www.alma.be/nl/restaurant/alma-1"> Klik hier!</p>
    </body>
    </html>
    """% (date_text, image)





    #return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    # """
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #     <meta charset="UTF-8">
    #     <style>
    #     h1, p {
    #     text-align: center;
    #     }
    #     </style>
    #     </head>
    #      <body>
    #     <h1> Alma Scraper <h1>
    #     <p> Je kan <u> Kaaskroketten </u>  eten in de Alma op:  </p>
    #     <p> %s </p>
    #     </body>
    #     </html>"""