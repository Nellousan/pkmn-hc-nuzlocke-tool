import sys
import save


f = open(sys.argv[1], "rb")
content = f.read()

sa = None
sb = None

save_a = content[0:0xE000]
save_b = content[0xE000:0x1C000]

if save.check_empty_save(save_a):
    print("save_a empty")
else:
    sa = save.Save(save_a)
    print(sa)

if save.check_empty_save(save_b):
    print("save_b empty")
else:
    sb = save.Save(save_b)
    print(sb)
