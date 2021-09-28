import re
import urllib.request

s = """
someting something ......
dhrubi89@gmil.vom
vjnlkjljbu@jhjgjjk.Fddfg
vkjhj876987@erd4.bjk
sgfgfr657i89hjjg@fdfh.com
himmm3456@hotm.com
someting something ......
dhrubi89@gmil.vom
vjnlkjljbu@jhjgjjk.Fddfg
vkjhj876987@erd4.bjk
sgfgfr657i89hjjg@fdfh.com
himmm3456@hotm.com
someting something ......
dhrubi89@gmil.vom
vjnlkjljbu@jhjgjjk.Fddfg
vkjhj876987@erd4.bjk
sgfgfr657i89hjjg@fdfh.com
himmm3456@hotm.com
someting something ......
dhrubi89@gmil.vom
vjnlkjljbu@jhjgjjk.Fddfg
vkjhj876987@erd4.bjk
sgfgfr657i89hjjg@fdfh.com
himmm3456@hotm.com
dhruvinhp@gmail.com
"""

# strlink = urllib.request.urlopen("https://media.geeksforgeeks.org/wp-content/uploads/e-mail-1.txt")

# for line in strlink:
#     s = line.decode().strip()
#     reg = re.findall(r"[a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+ \.[A-Za-z]{2,4}", s)

#     print(reg)

# reg = re.findall(r"[a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+ [.][A-Za-z.0-9]+", s)
reg = re.findall(r'\w+@\s+\w', s)
print(reg)
