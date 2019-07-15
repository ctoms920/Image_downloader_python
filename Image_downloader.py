import urllib.request

url = str(input('Enter Url '))
filename = input('Enter File Name ')
print('Downloading Image...')

def downloader(image_url,file_name): 
    full_file_name = str(file_name) + '.jpg'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
    req = urllib.request.Request(image_url, headers=headers)
    resp = urllib.request.urlopen(req)
    output = open(full_file_name,"wb")
    output.write(resp.read())
    output.close()
    
try:
 downloader(url,filename)
 print('Done')
 
except Exception as Error:
 print("Can't Download Image")
 print(Error) 
