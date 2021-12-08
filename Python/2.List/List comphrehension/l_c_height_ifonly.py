# for lopp result - before forloop
#if -right of forloop -result left side for loop
#if else- left side -if result if left -else right 

#square
############################################################

lc=[ x*x  for x in range(0,20)  ]


#even odd

lc=[ i if (i%2==0)   else 'False'  for i in range(0,20)  ]


#####################################################

heights = [144, 180, 165, 120, 199]
tall = [h for h in heights if h > 160]
print(tall)


