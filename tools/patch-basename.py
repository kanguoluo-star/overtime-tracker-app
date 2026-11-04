import sys

p = "www/assets/index-ByDp_M3i.js"
s = open(p, encoding="utf-8").read()

old = "basename:`/app/app_17hd6e8s6j5`"
if old not in s:
    sys.exit("basename pattern not found")
s = s.replace(old, "basename:`/`")

cdn = "https://lf-miaoda-static.feishucdn.com/app_17hd6e8s6j5/2/client/"
s = s.replace(cdn, "./assets/")

open(p, "w", encoding="utf-8").write(s)
print("patched basename count:", s.count("basename:`/`"))
print("remaining cdn refs:", s.count("lf-miaoda-static"))
