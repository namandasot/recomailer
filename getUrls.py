# -*- coding: utf-8 -*-

import requests
import MySQLdb
import csv
import re
class PropertyUrls():

	con = MySQLdb.connect("52.35.25.23","ITadmin","ITadmin","REDADMIN2",charset='utf8')
	cur = con.cursor()

	query = "select distinct Project_No, Project_Name from REDADMIN2.all_project_info where Config_Type != 'LAND'"
	cur.execute(query)


	def text_cleaner(self, string1):
		string1 = re.sub('[^A-Za-z0-9&/_ ]+', '', string1)
		string1 = re.sub('\s+', ' ', string1)
		# return string1.lower()
		return string1

	def getImageUrl(self):
		failed_csv = open('Failed_Data.txt', 'w')

		for rows in self.cur.fetchall():
			try:

				projNo 		= str(rows[0])
				projName 	= text_cleaner(rows[1])
				projName 	= projName.replace(' ', '_').replace('/', '_')


				imageUrl = 'https://www.hdfcred.com/project-images1/' + projNo + '/' + projNo + '_' + projName + '.jpg'
				req 	 = requests.get(imageUrl)
				
				if req.status_code == 200:
					continue

				elif req.status_code != 200:
					imageUrl = 'https://www.hdfcred.com/project-images1/' + projNo + '/' + projNo + '_' + projName + '_HD.jpg'
					req 	 = requests.get(imageUrl)
				
					if req.status_code == 200:
						continue

					elif req.status_code != 200:
						imageUrl = 'https://www.hdfcred.com/resale/images/user_uploaded/banners/' + projNo + '/235x300.jpg'
						req = requests.get(imageUrl)
						if req.status_code == 200:
							continue
					
					else:
						failed_csv.write(imageUrl + '\n')
						print imageUrl

			except Exception, ex:
				print projNo
				import pdb;pdb.set_trace()
				print ex

	def getProjUrl(self):
			my_csv = csv.writer(open('Missing_Urls11.csv', 'w'))
			headers = ['Project Id', 'Project Url']
			my_csv.writerow(headers)

			for rows in self.cur.fetchall():
				projNo 		= str(rows[0])
				propertyUrl = 'https://www.hdfcred.com/pid-' + projNo

				req = requests.get(propertyUrl)

				if req.status_code == 200:
					continue

				else:
					my_csv.writerow([projNo, propertyUrl])
					print propertyUrl


if __name__ == "__main__":
	pUrls = PropertyUrls()

	# pUrls.getImageUrl(projNo, projName)
	pUrls.getProjUrl()


