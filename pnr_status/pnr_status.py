#!/usr/bin/python

import requests
from BeautifulSoup import BeautifulSoup

class pnr_status():
  
  def get_pnr_status(self, pnr):
    cookies = {
    'PHPSESSID': 'tjs27ifob4s2grph3j6ecs5u97',
    'I_R_WPHPSESSID': 'ihfidhljmgnmddpnolhdlknhgfbanjlbopfkkchkhgblfojmpiledcfhhjcbnlabjiakpgpnammc',
    'cqPKh4rwsO': 'MDAwM2IyNGQ2MWMwMDAwMDAwNmMweU1SPG4xNDUzMDIzNjAy',
    'Gp6c6Cbjt0': 'MDAwM2IyNGQ2MWMwMDAwMDAwNjMwQRQ5PlwxNDUzMDIzNjAy',
    'I_R_WGp6c6Cbjt0': 'ffonmpkgngjkhfokdfckepppbpnegalnabnoehieeghodfdgjndiooebelaanphmangolmbcamck',
    }

    headers = {
    'Origin': 'http://www.indianrail.gov.in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6,es;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://www.indianrail.gov.in/',
    'Connection': 'keep-alive',
    }
    data = 'lccp_pnrno1='+pnr+'&lccp_cap_value=24357&lccp_capinp_value=24357'
    page = requests.get('http://www.indianrail.gov.in/pnr_Enq.html', timeout = 300)
    soup1 = BeautifulSoup(page.text)
    action = soup1.find('form', id='form3').get('action')
    result = requests.post(action, headers=headers, cookies=cookies, data=data, timeout = 300)
    html = result.text
    return self.parse_response(html)
  
  def parse_response(self,html):
    soup = BeautifulSoup(html)
    tables = []
    i = 0
    for table in soup.findAll("table", "table_border"):
      tables.append(table)

    all_tds = []
    for table in tables:
      #dir(table)
      soup = BeautifulSoup(str(table))
      tds = soup.findAll('td', 'table_border_both')
      for td in tds:
	all_tds.append(td.getText())
      
    return all_tds
