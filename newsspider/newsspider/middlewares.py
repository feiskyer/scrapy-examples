# Importing base64 library because we'll need it ONLY in case if the proxy 
# we are going to use requires authentication
import base64 
import random

class ProxyMiddleware(object): 
    # overwrite process request 
    def process_request(self, request, spider): 
        data = file('proxies.txt','r').readlines()
        length = len(data)
        index  = random.randint(0, length -1)
        item   = data[index]
        arr    = item.split()
        request.meta['proxy'] = "http://%s:%s" % (arr[0], arr[1]) 
        
        # Use the following lines if your proxy requires authentication 
        # proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_passwq#

