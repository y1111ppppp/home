# $language = "python"
# $interface = "1.0"

def main(filename):
    i = 0
    with open(filename,'r') as fp:
        while True:
            i += 1
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            line = line.split()
            hostname = line[0]
            username = line[1]
            password = line[2]
            username1 = line[3]
            newpassword = line[4]
            cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES utf-8 %s" % (username,password,hostname)
            crt.Session.ConnectInTab(cmd)
            x = crt.GetTab(i)
            x.Activate
            logpath = "E:\log\centos"
            x.Session.LogFileName = logpath + hostname + ".log"
            x.Session.Log(True)
            cmd1 = 'echo {0}|passwd --stdin {1}'.format(line[4],line[3])
            cmd2 = 'LANG=zh_CN.GB18030'
            cmd3 = 'LANGUAGE=zh_CN.GB18030:zh_CN.GB2312:zh_CN'
            cmd4 = 'free -m'
            cmd5 = "sed -i 's/id: SN2018-04-134/id: {0}/g' /etc/salt/minion".format(hostname)
            cmd6 = 'grep ^[^#] /etc/salt/minion'
            #x.Screen.Send(cmd2 + '\r')
            #x.Screen.WaitForString('#') 
            #x.Screen.Send(cmd3 + '\r')
            #x.Screen.WaitForString('#')
            x.Screen.Send(cmd5 + '\r')
            x.Screen.WaitForString('#')
            x.Screen.Send(cmd6 + '\r')
            #x.Session.Log(False)
            
main('E:/python/centos.txt')
