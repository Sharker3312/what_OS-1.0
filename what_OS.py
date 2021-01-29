
#!/usr/bin/python3

from os import name, truncate
import re, sys, subprocess



if len(sys.argv) !=2:
    
    print("\n[i] Uso: python3 " + "sys.argv[0]"+ " < ip_adress>\n" )
    sys.exit(1)
    
    
def get_ttl(ip_adress):
     
    
    proc= subprocess.Popen(["/usr/bin/ping -c 1 %s" %ip_adress , "" ], stdout=subprocess.PIPE, shell=True)
    (out,err)=proc.communicate() 
    
    out=out.split()

    out=out[12].decode('utf-8')
     
    ttl_value = re.findall(r"\d{1,3}", out)[0]
    
    return ttl_value

def get_OS(ttl):
    
    ttl=int(ttl)
    if ttl >=0 and ttl <= 64:
        return "LINUX"
    elif ttl >= 65 and ttl <=128:
        return "WINDOWS"
    else:
        return "Not Found"
    
def what_OS():
    ip_adress=sys.argv[1] 
    ttl=get_ttl(ip_adress)  
    os_name=get_OS(ttl)
    print("%s (ttl->%s): %s" % (ip_adress, ttl, "|"+os_name+"|"))
        

    
if __name__ == '__main__':
    what_OS()
    
    
    
