import re

text='''Sh ver
Cisco IOS XE Software, Version 16.09.05
Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.5, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 30-Jan-20 18:53 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2020 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License (""GPL"") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or ""License Notice"" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON
BOOTLDR: System Bootstrap, Version 16.9.1r[FC4], RELEASE SOFTWARE (P)

WAVNDCD01Z01BG uptime is 29 weeks, 5 hours, 11 minutes
 --More-- '''




pattern=re.compile(r'[897]0\d[.-]\d{3}[.-]\d*')
pattern=re.compile(r'\w[a]\w[,]')

pattern1=re.compile(r'\w\w\w\w?\w?.\d\d\d\d?\d?\d?')

matches=pattern1.findall(text2)
matches_str=' '.join(matches)
print(matches_str)



'''
Ques1
#cat,bat,mat,lat,ank,kot
output=cat,mat,lat
3 digit
1 alpha 

ans [^b]at
'''

