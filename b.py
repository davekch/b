with type("Com",(),{"__enter__":lambda s:s,"sys":__import__("sys"),"re":__import__("re"),"it":__import__("itertools"),"__init__":lambda s:[None,setattr(s,"mem",[0 for i in range(3000)]),setattr(s,"ptr",0),setattr(s,"i",-1)][0],"__exit__":lambda s,e,v,t:1,"do":lambda com,code:[(lambda:setattr(com,"i",com.i+1) or (setattr(com,"ptr",com.ptr+1) if code[com.i]==">" else setattr(com,"ptr",com.ptr-1) if code[com.i]=="<" else com.mem.__setitem__(com.ptr,com.mem[com.ptr]+1) if code[com.i]=="+" else com.mem.__setitem__(com.ptr,com.mem[com.ptr]-1) if code[com.i]=="-" else com.sys.stdout.write(chr(com.mem[com.ptr])) if code[com.i]=="." else com.mem.__setitem__(com.ptr,ord(com.sys.stdin.read(1))) if code[com.i]=="," else setattr(com,"i",com.i+(lambda string:[i for i in zip([m.start() for m in com.re.finditer('\[',string)][1:]+[len(string)],[m.start() for m in com.re.finditer(']',string)]) if i[0]>i[1]][0][1])(code[com.i:])) if code[com.i]=="[" and com.mem[com.ptr]==0 else setattr(com,"i",len(code[:(com.i+1)])-(lambda string:[i for i in zip([m.start() for m in com.re.finditer(']',string)][1:]+[len(string)],[m.start() for m in com.re.finditer('\[',string)]) if i[0]>i[1]][0][1])(code[:(com.i+1)][::-1])-2) if code[com.i]=="]" and not com.mem[com.ptr]==0 else 1))() if com.i+1<len(code) else com.sys.exit() for _ in com.it.repeat(0)]})() as com: com.do("".join(filter(lambda x:x in "+-[]><.,",list(open(com.sys.argv[1]).read()))))
