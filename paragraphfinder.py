

url = 'https://en.wikipedia.org/wiki/Main_Page'
values = {'s':'basics', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resdata = resp.read().decode('utf-8')
#print(resdata)
parag = re.findall(r'<p>(.*?)</p>', resdata)
print (parag)
print("-----------------------------------------------------")
st = ""
for pp in parag:
    st+=re.sub('<.*?>', "", pp)
print (st)
