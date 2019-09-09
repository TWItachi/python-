import requests

headers ={
    'Cookie' : '_zap=4468d1c1-b070-47cf-81ba-eafb7f174245; d_c0="ABApkjaNdQ-PTqDdq066Gu5K99kKG5L64h4=|1558366793"; q_c1=22719635f120441583db7a5a20fd60f0|1558366794000|1558366794000; __gads=ID=225eeb284214a26c:T=1558366796:S=ALNI_MYSWpCkLXMOFiECrlhu8zcV-3kOmg; l_n_c=1; _xsrf=ab1d2480c0fa46443f387716993c41f6; n_c=1; __utma=51854390.622405854.1558625061.1558625061.1558625061.1; __utmc=51854390; __utmz=51854390.1558625061.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20190520=1; _xsrf=4jPGvLlEWqcqyVv5JCZ2woKOQJcH5Ydj; capsion_ticket="2|1:0|10:1558701115|14:capsion_ticket|44:OWEzYjQ3YjcyYjU4NDUwY2JlODYyZGU4NDc0NmU4ZjU=|3536d5dc8b2dd788d8d431ed0cf9b37b28c91038d035d39cdc5d3c116d67efde"; r_cap_id="ODk2ZWVhMGFkZjE5NGViOWEwYjY3OWI3OWU5NDU0ODk=|1558701120|00da8774e872b783f276eb5ab4a33e36ff2172ea"; cap_id="Y2NmZDQyMWExZDVhNDY0NTk0ZTYzNzMyZDdlOTQzODM=|1558701120|6fb17d5479dea560ff6fd67322de9cd86e729642"; l_cap_id="Y2I0OTdjODZkYWVmNDUyNThhMTNhYTdjOTE3MGU2YWE=|1558701120|3cbb623866e65ef920534946ea68a1ca3a2af3f8"; z_c0=Mi4xbnRKQ0RBQUFBQUFBRUNtU05vMTFEeGNBQUFCaEFsVk5SVExWWFFCY1h4aTZmOXVrUjM5bHpaVl9FYVdlNDB1dHFB|1558701125|19a87796c67f5dd28fff9ed9fcfb1b7697d7ccf4; tst=r; tgw_l7_route=7c109f36fa4ce25acb5a9cf43b0b6415',
    'host': 'www.zhihu.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

r = requests.get('http://www.zhihu.com', headers=headers)

print(r.text)