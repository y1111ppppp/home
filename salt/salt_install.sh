#master
rpm -Uvh http://ftp.linux.ncsu.edu/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum install salt-master -y
chkconfig salt-master on
service salt-master start
iptables -I INPUT -m state --state new -m tcp -p tcp --dport 4505 -j ACCEPT
iptables -I INPUT -m state --state new -m tcp -p tcp --dport 4506 -j ACCEPT

#vim /etc/salt/master
#interface：192.168.1.133
#auto_accept：True
#file_roots：
#    base：
#        - /srv/salt

service salt-master restart







#minion
rpm -Uvh http://ftp.linux.ncsu.edu/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum install salt-minion -y
chkconfig salt-minion on
service salt-minion start


#vim /etc/salt/minion
#master：192.168.1.133
#id：SN2013-08-021

service salt-minion restart
