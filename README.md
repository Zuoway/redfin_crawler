# Redfin Crawler

This is a python3 and Scrapy based crawler on Redfin.com. It automatically gather information of properties sold within last 6 months across the US. The information includes:
  - Address
  - City
  - State
  - Zipcode
  - Sold Date
  - Property Type
  - Price
  - Year Built
  - Square ft.
  - Lot Size
  - Bath
  - Beds
  - Days on Market

### Implementation

Comments are available in source code. A couple approaches is used for anti-banning, including limiting concurrent request per domain, delaying downloading for 1 sec, and disabling cookies. Rotating ip-proxy, and rotating user agent modules are used. The ip proxy module is not activated in this build due to limited reliability and availability of free proxies.

### To Run The Crawler (for Lofty)

```sh
$ docker run -v /home/LoftyCode/InternResults:/usr/src/app/Result zhuang02/redfin:1
```

After initiating, the console outputs crawler information and running states. A .csv file will be generated within a desired folder during crawling. 

One can type <kbd>CTRL</kbd>+<kbd>C</kbd> to abort crawling prematurely and still be able to see partial .csv file for testing purposes.
