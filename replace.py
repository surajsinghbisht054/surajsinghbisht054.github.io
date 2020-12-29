import os

l = os.listdir('_posts/')
for p in l:
  con = open('_posts/'+p).readlines()
  ltag = con.index('---\n',1)
  ul = con[ltag-1][47:-1]
  rul = "redirect_from: \"{}\"".format(ul)
  print(rul)
  con.insert(con.index('---\n',1), rul)
  out = open('_posts/'+p, 'w')
  out.write('\n'.join(con))
  out.close()
