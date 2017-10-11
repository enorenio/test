import hashlib
import time
def encode(s):
  s = s.encode("utf-8")
  md5 = hashlib.md5()
  md5.update(s)
  return md5.hexdigest()
key = "yzbqklnj"
for i in range(1, 999999):
  h = encode(key +str(i));
  #print(h)
  if(h.startswith("00000")):
    print(str(i))
    time.sleep(5)