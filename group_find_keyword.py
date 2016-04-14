import json 
def show(j_in):
    print(json.dumps(j_in,ensure_ascii=False,indent=2))
import time

import send_gmail as send_to
import facebook
token='CAAPa5UAeB24BAFVxkFZCcbtLksXQ3ImK6XZBHsKNw1ZCf72cO8BKZCieZCsJyGtUDBxxknSKb9UYFV832ml9QGQweyiotGLVMcgdWws8dYPsz7pVGhczRXCP6lGVDv6lpQMlQj7mln9AqFeDsY7qVZBXxxVlgEvJ30z5QXT2n9r5bz9JJYdPKiZCUiikfZCRWn7GeDgUHAWLcgZDZD'
graph=facebook.GraphAPI(token) 

#group_id = '400948843346851'	#出清台大
group_id = '763162137038548'	

keywords = ['香水']

subject = ''
mail_message = ''
toaddrs = 'w19940503@gmail.com'
####


def find_name(po_id):
	po_name = graph.fql("SELECT name FROM profile WHERE id =" +po_id)
	return po_name['data'][0]['name']


while True:
	message_query = "SELECT message, actor_id, permalink FROM stream WHERE " + "source_id=" + group_id +"ORDER BY scheduled_publish_time "+ " LIMIT 3"
	after_fql = graph.fql(message_query)
	for i in range(len(after_fql['data'])):
		post_data = after_fql['data'][i]
		print(post_data['message'])
		for keywd in keywords:
			if post_data['message'].find(keywd) != -1:
				subject = 'Find '+keywd
				Po_name = find_name(post_data['actor_id'])
				mail_message = Po_name + ' \n'+post_data['message']+'\n\n'

				print (mail_message)
#				send_to.send_email(mail_message,subject,toaddrs)
			else:
				print ('no keyword ')
	time.sleep(30)

