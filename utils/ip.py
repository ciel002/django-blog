import requests
from lxml import etree


def ip2_region_by_taobao(ip):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
    response = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip={0}".format(ip), headers=headers)
    try:
        country = response['data']['country']
        region = response['data']['region']
        city = response['data']['city']
        county = response['data']['county']
        isp = response['data']['country']
        ip_region = country + ' ' + region + ' ' + city + '' + county + ' | ' + isp
    except:
        ip_region = '未知区域'
    return ip_region


def ip2_region_by_138(ip):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
    response = requests.get("https://www.ip138.com/iplookup.asp?ip={0}&action=2".format(ip), headers=headers)
    html = etree.HTML(response.content.decode('gbk'))
    try:
        ip_region = html.xpath("//ul[@class='ul1']/li[1]/font/text()")[0].split("：")[-1]
    except:
        ip_region = '未知区域'
    return ip_region
