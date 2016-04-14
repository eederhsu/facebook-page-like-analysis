import json 
def show(j_in):
    print(json.dumps(j_in,ensure_ascii=False,indent=2))
import time
import urllib.request

import send_gmail as send_to
import facebook

#暫時個人
#token = 'CAACEdEose0cBAOOHiI2VyqSpvbWtbYrNKifocVp0Maiho3bm0UXtT0TUMrLZBT2MKyNiwkFdtwhNfIKUxh6iJwhsu7e9ZCRPWq0n1ZATZCXjd66XAdELva8HKPgvo3iQTdK7tbWRTIYNQ8pwaQyRcNUhCoZC5YIrcYHQCEaPDuWgqweDppTAT0cHSKUPXviYkEsJdW3eVAI60oLNGBJtfpgVvf36YIf4ZD'

#永久token
token='CAAPa5UAeB24BAFVxkFZCcbtLksXQ3ImK6XZBHsKNw1ZCf72cO8BKZCieZCsJyGtUDBxxknSKb9UYFV832ml9QGQweyiotGLVMcgdWws8dYPsz7pVGhczRXCP6lGVDv6lpQMlQj7mln9AqFeDsY7qVZBXxxVlgEvJ30z5QXT2n9r5bz9JJYdPKiZCUiikfZCRWn7GeDgUHAWLcgZDZD'

graph=facebook.GraphAPI(token) 

fan = 'himhebe'
#group_id = '763162137038548' #
#group_id = '400948843346851' #出清
#group_id = '890661937659454' #台大交流版

keywords = ['dd']

#show(graph.get_object('jay'))
#####=========#####
#group_query = "SELECT like_info.like_count, post_id, message, actor_id, comment_info FROM stream WHERE " + \
#                  "source_id=" + '763162137038548' + " LIMIT 50"


'''
#send_to.send_email('cool','good_findit','w19940503@gmail.com')
while True:
	message_query = "SELECT message, actor_id FROM stream WHERE " + "source_id=" + group_id +"ORDER BY scheduled_publish_time "+ " LIMIT 3"
	after_fql = graph.fql(message_query)
	for i in range(len(after_fql['data'])):
		mess = after_fql['data'][i]['message']
		print(mess)
#		if mess.find('機車環島') != -1:
#			print ('cool       ',str(mess.find('機車環島')))
#		else:
#			print ('GGG         ')
	time.sleep(30)
#'''



###
page = graph.get_object('himhebe')
show(page)
###
#show(graph.get_object('antiblacktw',fields='feed.limit(1)')) 


#group_info = graph.get_connections(fan,connection_name='feed')
#show(group_info)
#print(group_info['name'])



#http://graph.facebook.com/search?q=chennaifoodies&type=group&access_token=ACCESS_TOKEN
#show(graph.get_object('antiblacktw',fields='feed.limit(1)')) 
#show(graph.get_object('me',fields='id,name,email')) 
#show(graph.get_connections('me','friends')) 
#graph.put_object('me','feed',message='Hello from class \ngg boring!')
