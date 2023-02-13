#访问IBT项目的列表数据
import re

import pytest
import requests

from commons.request_util import RequestUtil


class TestApi:
 @pytest.mark.smoke
 def test_ContentList(self):
     urls="https://user-test.imeik.com/ibt/admin/content/list"
     datas ={
        "limit":1,
        "page":2,
        "params":3,
        "sourceType":"1"
     }
     headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
     cookie={'Cookie':'p_h5_u=28C95E8A-D96F-4137-97C1-D6302E3559EF; selectedStreamLevel=FD; p_h5_upload_u=24127CAB-41CA-4DE7-89F5-821500C8FFB7; p_h5_upload_clientId=F0A77D78-EF7A-49A7-BFBE-F21262F23C10; imeik-token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwMDMyMDM3NSIsImF1ZCI6ImFkbWluIiwiY3JlYXRlZCI6MTY3NjE4Mzg2MjEyOH0.evj70MN39SHX7wHfrw-ZgjXECGs1PQ-5dqS7G_kKIrUgQLQWxjOXgwqkxT7ZIk_w6rx1PgwPgXC1GVvPRDsbTQ'}
     res=RequestUtil().all_send_request("get",url=urls,headers=headers,cookies=cookie,params=datas)
     # res=TestApi.session.get(url=urls)

     assert res.status_code==200
     print("_________"+res.text)

# 访问首页接口
#  def test_baidu(self):
#      urls="http://user-test.imeik.com/login?redirect=%2F"
#      headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
#      res=requests.get(url=urls,headers=headers)
#      result=res.text
#
#      re.search('name="1" value="(.*?)"',result).group(1) #(.*?)正则表达式取值
#      print(res.text)

# if __name__ == '__main__':
#     TestApi().test_baidu()



