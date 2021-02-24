
# Vegas Housing Data

This project data mines housing information on zillow in the surrounding Las Vegas market.
Due to certain restrictions on zillow's own website selenium library is used in addition
to scrapy to draw the data. 

Mined data is contained in mysql database and viewed on webserver. The server will handle
information and update on the price changes on a weekly and monthly bases.

### *Note*
Make sure the chromedriver is the correct version and in directory mine/driver/.
