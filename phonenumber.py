import mysql.connector 
import urllib2
import json
import time

config = {
	'user': 'demo',
	'password': 'demo',
	'host': 'localhost',
	'database': 'rui_site',
}

try:
	db = mysql.connector.connect(**config)
except Exception , e:
	print e;


for i in range(6,10):
	for j in range(0,10):
		for k in range(0,10):
			for m in range(0,10):
				innerfix = ''+`i`+`j`+`k`+`m`
				prefix = "http://opendata.baidu.com/api.php?query=138"
				suffix = "2232&co=&resource_id=6004&t=1422254015296&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110208778024467173964_1422254010331&_=1422254010334"
	 			url = prefix + innerfix + suffix;
	 			try:
	 				print "start..." + innerfix
					response = urllib2.urlopen(url)
					html = response.read()
					lpos = html.find("[")
					rpos = html.rfind("]")
					html1 =  html[lpos:rpos+1]
					data = json.loads(html1,'gb2312')
					city =  data[0]["city"]
					prov =  data[0]["prov"]
					if len(prov) == 0 :
						prov = city 
					cursor = db.cursor()
					cursor.execute("insert into attributions(number, city, prov) values ('"+innerfix +"','"+city+"','"+prov+"')")
					db.commit()
					print "end..." + innerfix
					#time.sleep(0.01)
				except Exception , e:
					print e


db.close()