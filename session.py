import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어줍시다. (모두 문자열)
LOGIN_INFO = {
    'userID' : 'gustj2005',
    'userPassword' : 'wkehdck4937!'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html,'html.parser')
    csrf = soup.find('input',{'name':'_csrf'}) # input 태그 중에서 name이 _csrf인 것
    print(csrf['value']) 
    
    # (p.s.)Python3에서 두 dict를 합치는 방법은 {**dict1, **dict2} 으로 dict들을 unpacking하는 것입니다.
    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
    print(LOGIN_INFO)
    
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    print(login_req.status_code)