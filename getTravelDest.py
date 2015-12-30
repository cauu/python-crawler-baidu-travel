#coding:utf-8
import urllib
import re
import os
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

DEST = {
	# 'taiwan':'台湾',
	# 'anhui':'安徽',
	# 'guangxi':'广西',
	# 'neimenggu':'内蒙古',
	# 'aomen':'澳门',
	# 'hainan':'海南',
	# 'hebei':'河北',
	# 'henan':'河南',
	# 'hubei':'河北',
	# 'jilin':'吉林',
	# 'heilongjiang':'黑龙江',
	# 'ningxia':'宁夏',
	# 'shaanxi':'陕西',
	# 'yunnan':'云南',
	# 'sichuan':'四川',
	# 'shanxi':'山西',
	# 'liaoning':'辽宁',
	# 'jiangxi':'江西',
	# 'jiangsu':'江苏',
	# 'hunan':'湖南',
	# 'guizhou':'贵州',
	# 'gansu':'甘肃',
	# 'fujian':'福建',
	# 'shandong':'山东',
	# 'chongqing':'重庆',
	# 'zhejiang':'浙江',
	# 'guangdong':'广东',
	# 'xianggang':'香港',
	# 'tianjin':'天津',
	# 'shanghai':'上海',
	# 'beijing':'北京',
	# 'qinghai':'青海',
	# 'xinjiang':'新疆',
	# 'xizang':'西藏',
       #  'faguo': '法国',
       #  'xibanya': '西班牙',
       #  'meiguo': '美国',
       #  'yidali': '意大利',
       #  'yingguo': '英国',
       #  'deguo': '德国',
       #  'wukelan': '乌克兰',
       #  'tuerqi': '土耳其',
       #  'moxige': '墨西哥',
       #  'malaixiya': '马来西亚',
       #  'aodili': '奥地利',
       #  'eluosi': '俄罗斯',
       #  'jianada': '加拿大',
       #  'xila': '希腊',
       #  'bolan': '波兰',
       #  'taiguo': '泰国',
       #  'putaoya': '葡萄牙',
       #  'shatealabo': '沙特阿拉伯',
       #  'helan': '荷兰',
       #  'aiji': '埃及',
       #  'keluodiya': '克罗地亚',
       #  'nanfei': '南非',
       #  'xiongyali': '匈牙利',
       #  'ruishi': '瑞士',
       #  'riben': '日本',
       #  'xinjiapo': '新加坡',
       #  'aierlan': '爱尔兰',
       #  'moluoge': '摩洛哥',
       #  'alianqiu': '阿联酋',
       #  'bilishi': '比利时',
       #  'jieke': '捷克',
       #  'hanguo': '韩国',
       #  'yindunixiya': '印度尼西亚',
       #  'ruidian': '瑞典',
       #  'baojialiya': '保加利亚',
       # 'aodaliya': '澳大利亚',
       #  'baxi': '巴西',
       # 'yindu': '印度',
       #  'danmai': '丹麦',
       #  'agenting': '阿根廷',
       #  'balin': '巴林',
       #  'yuenan': '越南',
       #  'duominijia': '多米尼加',
       #  'nuowei': '挪威',
       #  'boduolige': '波多黎各',
       #  'dibai': '迪拜',
       # 'jianpuzhai': '柬埔寨',
       # 'feilvbin': '菲律宾',
       # 'niboer': '尼泊尔',
       # 'laowo': '老挝',
       # 'miandian': '缅甸',
       # 'sililanka': '斯里兰卡',
       # 'maerdaifu': '马尔代夫',
       # 'wenlai': '文莱',
       # 'fenlan': '芬兰',
       # 'bingdao': '冰岛',
       # 'lusenbao': '卢森堡',
       # 'guba': '古巴',
       # 'bilu': '秘鲁',
       # 'boliweiya': '玻利维亚',
       # 'zhili': '智力',
       # 'xinxilan': '新西兰',
       # 'kenniya': '肯尼亚'
       # 'yuedan': '约旦',
       # 'yilang': '伊朗'
       # 'tansangniya': '坦桑尼亚',
       # 'mengjialaguo': '孟加拉国',
       # 'yiselie': '以色列',
       # 'palao': '帕劳',
       # 'chaoxian': '朝鲜',
       # 'aisaiebiya': '埃塞俄比亚',
       # 'maoliqiusi': '毛里求斯',
       # 'jinbabuwei': '津巴布韦',
       # 'bahama': '巴哈马',
       # 'menggu': '蒙古',
       # 'luomaniya': '罗马尼亚',
       # 'gesidalijia': '哥斯达黎加',
       # 'xuliya': '叙利亚',
       # 'feiji': '斐济',
       # 'litaowan': '立陶宛',
       # 'aishaniya': '爱沙尼亚',
       # 'latuoweiya': '拉脱维亚',
       # 'yamaijia': '牙买加',
       # 'banama': '巴拿马',
       # 'weidimala': '危地马拉',
       # 'eguaduoer': '厄瓜多尔',
       # 'siluowenniya': '斯洛文尼亚',
       # 'siluofake': '斯洛伐克',
       # 'madajiasijia': '马达加斯加'
       # 'ouzhoumonage': '摩纳哥',
       # 'fandigang': '梵蒂冈',
       # 'budan': '不丹',
       # 'andaoer': '安道尔',
       'maerta': '马耳他'
}

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	# saveToFile('anhui.html', html)
	return html

def parseSpan(src):
	return src.split('>')[2].split('<')[0]

def getDetailDest(html,result):
	reg = r'<a href=".*" .*><span>.*</span></a>'
	destTagReg = re.compile(reg)
	tagSrc = re.findall(destTagReg, html)
	for s in tagSrc:
		#print s
		result.append(parseSpan(s))
	# saveToFile(destName+'.txt', tagSrc)
	# print tagSrc

def getDestUrl(destName):
	return "http://lvyou.baidu.com/"+destName+"/jingdian"

def saveToFile(filename,content):
	f = open(filename,'w')
	f.writelines(content);
	f.close()

def getAJAXHtml(url,destName):
	senicSpots = []
	driver = webdriver.Chrome("/Users/cauu/bin/chromedriver")
	driver.get(url)
	for i in range(2,20):
		try:
                        #等待view-comment组件加载完成
			element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"view-comment")))
		finally:
			searchBox = driver.find_element_by_id("J-view-list-container")
			innerText = searchBox.get_attribute('innerHTML')
			getDetailDest(innerText,senicSpots)
			# saveToFile('destName_'+str(i)+'.html', searchBox.get_attribute('innerHTML').encode('utf-8'))
                try:
                        close = driver.find_element_by_xpath('//a[@title="关闭"]')
                        close.click()
                except NoSuchElementException: 
                        print 'Cannot find close button'
                except WebDriverException: 
                        print 'Cannot press close button'

		try:
			link = driver.find_element_by_link_text(str(i)).click()
		except NoSuchElementException:
			# print destName+'has total'+str(i)+'pages'
			result = ''
			for i in senicSpots:
				#print 'senicSpots'+i.encode('utf-8')
				result = result + destName + ' ' + i.encode('utf-8')+'\n'
			saveToFile(destName+'.txt',result)
			driver.quit()
			break;

for k,v in DEST.items():
	getAJAXHtml(getDestUrl(k),v)







