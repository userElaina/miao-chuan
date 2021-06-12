import os
import sys
import hashlib

def hsh_b(pth,type="md5",block_size=1024*1024,bg_size=256*1024):
	'''md5, sha1, blake2b, blake2s, 
	sha224, sha256, sha384, sha512, 
	sha3_224, sha3_256, sha3_384, sha3_512, 
	shake_128, shake_256, '''
	hsh=hashlib.new(type,b"")
	with open(pth,'rb') as f:
		data=f.read(bg_size)
		hsh.update(data)
		m1=hsh.hexdigest()
		while True:
			data=f.read(block_size)
			if not data:
				break
			hsh.update(data)
		return [m1,hsh.hexdigest(),]

# 76fc6c2b0f984432e3407535c8d7f3c0#e5febdb4176dc043b89b1cc3db36c270#1150934733#loki1.mp4
# pth=r'C:\All\Down\loki1.mp4'

pth=sys.argv[1] if len(sys.argv)>1 else input()
_l=hsh_b(pth)
_ll=[str(i) for i in [_l[1],_l[0],os.path.getsize(pth),os.path.basename(pth)]]
ans='#'.join(_ll)

print(ans)
input()

