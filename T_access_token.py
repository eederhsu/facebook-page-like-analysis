import facebook 

FB.login(func, {scope: 'manage_pages publish_stream photo_upload'})

#server side:
from core.libs import facebook

user = facebook.get_user_from_cookie(self.request.cookies, <api_key>, <client_secret>)

graph = facebook.GraphAPI(user["access_token"])
result = graph.extend_access_token(<api_key>, <client_secret>)
graph2 = facebook.GraphAPI(result['access_token'])
result2 = graph2.request(page_id, {'fields': 'access_token'})
# long-lived token: result2['access_token'])