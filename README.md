# pnr_status
A Python script to fetch pnr status. An attempt to bypass captcha on http://www.indianrail.gov.in/pnr_Enq.html

# Dependencies

1. sudo pip install requests (http://docs.python-requests.org/en/latest/)
2. sudo pip install beautifulsoup (http://www.crummy.com/software/BeautifulSoup/)

# Usage

```sh
usage --
python pnr_status.py <PNR no.>
```

# Example

```sh
$python pnr_status.py 4416052206
```
```sh
[u'*12735', u'YPR GARIB RATH', u'21- 1-2016', u'SC', u'YPR', u'YPR', u'SC', u'3A', u'Passenger 1', u'G12 , 73,SS', u'CNF', u'CHART NOT PREPARED']
```

