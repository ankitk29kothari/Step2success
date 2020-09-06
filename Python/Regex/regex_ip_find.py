import re
ip='ip 127.0.0.1 & 202.0.0.1 ,999.3.3.2,egreg  255.255.255.254 '



pattern=re.compile(r'\b(([2][5][0-5]|[2][0-4][0-9]|[0-]?[0-9][0-9]?)[.]\d\d?\d?[.]\d\d?\d?[.]\d\d?\d?)\b')
pattern1 = re.compile(r'\b(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
matches=pattern1.findall(ip)

print(matches)






