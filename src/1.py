s = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. (map)"
for c in s:
    if not c.islower():
        print(c, end='')
    else:        
        print(chr((ord(c) - ord('a') + 2) % 26 + ord('a')), end='')
print()


