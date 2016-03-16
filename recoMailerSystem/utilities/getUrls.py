# -*- coding: utf-8 -*-

import requests
import re

# 	con = MySQLdb.connect("52.35.25.23","ITadmin","ITadmin","REDADMIN2",charset='utf8')
# 	cur = con.cursor()
# 
# 	query = "select distinct Project_No, Project_Name from REDADMIN2.all_project_info where Config_Type != 'LAND'"
# 	cur.execute(query)


class PropertyUrls():

	def textCleaner(self, string1):
		string1 = re.sub('[^A-Za-z0-9&/_ ]+', '', string1)
		string1 = re.sub('\s+', ' ', string1)
		# return string1.lower()
		return string1

	def checkReqStatus(self, url):
		req = requests.get(url)	
		if req.status_code == 200:
			return True
		
	def getImageUrl(self, projNo, projectName):
		projName = self.textCleaner(projectName)
		projName = projName.replace(' ', '_').replace('/', '_')
		
		imageUrl = 'https://www.hdfcred.com/project-images1/' + projNo + '/' + projNo + '_' + projName + '.jpg'
				
		if self.checkReqStatus(imageUrl) == True:
			return imageUrl
		
		else:
			imageUrl = 'https://www.hdfcred.com/project-images1/' + projNo + '/' + projNo + '_' + projName + '_HD.jpg'
			
			if self.checkReqStatus(imageUrl) == True:
				return imageUrl
		
			else:
				imageUrl = 'https://www.hdfcred.com/resale/images/user_uploaded/banners/' + projNo + '/235x300.jpg'
				
				if self.checkReqStatus(imageUrl) == True:
					return imageUrl
				else:
					return False

	def getProjUrl(self, projNo):
		propertyUrl = 'https://www.hdfcred.com/pid-' + projNo
		
		if self.checkReqStatus(propertyUrl) == True:
			return propertyUrl
		else:
			return False


# if __name__ == "__main__":
# 	pUrls = PropertyUrls()
# 
# 	# pUrls.getImageUrl(projNo, projName)
# 	pUrls.getProjUrl()


