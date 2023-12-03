import requests
import re

pattern = r'<h3[^>]*>([\s\S]*?)<\/h3>'
req = requests.get('http://www.columbia.edu/~fdc/sample.html')
ans = re.findall(pattern, req.text)
print(ans)
