import json 
def show(j_in):
    print(json.dumps(j_in,ensure_ascii=False,indent=2))
import time
import urllib.request

import facebook

token = 'CAACEdEose0cBADECGO4B3b8ygtFDrZCo9Xg7lJXWQnZC5oV1ZAIeRZCqfGoXt5xtSAa22REBYPzFaOFxxtLhw8VVZAY0KyXdEKfBZA2d4QiwnpcqJDemVMRrUO8vo4U3I9UmkeczzmRp4oSHRkPGishdtrtumKqmr8cAu0RV5ojI8osPhzZBqnBjwvWjdYPmF7eFVcJ5KeXrgZDZD'

graph=facebook.GraphAPI(token) 
page_hebe = '110958532292955'


while True:
	message_query = "SELECT message, actor_id, post_id,likes FROM stream WHERE " + "source_id=" + page_hebe
	after_fql = graph.fql(message_query)
	for i in range(len(after_fql['data'])):
		like_count = after_fql['data'][i]['likes']['count']
		mess = after_fql['data'][i]['message']
		po_id = after_fql['data'][i]['actor_id']

		name_s = graph.get_object(po_id)
		print(name_s['name'],'  ',like_count,'     \n')


