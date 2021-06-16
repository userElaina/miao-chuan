import os
import sys
import hashlib

def hash_f(pth:str,api:str='md5',block_size:int=1024*1024,head_size:int=256*1024)->list:
	with open(pth,'rb') as f:
		hsh=hashlib.new(api,f.read(head_size))
		head=hsh.hexdigest()
		while True:
			data=f.read(block_size)
			if not data:
				break
			hsh.update(data)
		return [hsh.hexdigest(),head,]

def _file(pth:str)->str:
	_ll=[str(i) for i in hash_f(pth)+[os.path.getsize(pth),os.path.basename(pth)]]
	ans='#'.join(_ll)
	return os.path.abspath(pth)+' :\n'+ans+'\n'

def _dir(pth:str)->str:
	ans=list()
	for r,d,f in os.walk(pth):
		for i in f:
			ans.append(_file(os.path.join(r,i)))
	return '\n'.join(ans)

def mian(pth:str)->str:
	if os.path.isfile(pth):
		return _file(pth)
	if os.path.isdir(pth):
		return _dir(pth)
	return 'No such file or directory: "'+os.path.abspath(pth)+'"\n'


ipt=lambda :input('>>> ')
pth=sys.argv[1] if len(sys.argv)>1 else ipt()

# pth=r'C:\All\Down\loki1.mp4'
# 76fc6c2b0f984432e3407535c8d7f3c0#e5febdb4176dc043b89b1cc3db36c270#1150934733#loki1.mp4

while True:
	print(mian(pth))
	pth=ipt()
