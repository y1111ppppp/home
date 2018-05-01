#-*- conding: utf-8 -*-

通过saltstack来批量安装zabbix_agentd,也可以通过修改top.sls来卸载zabbix_agentd
1.salt '*' pkg.install pcre*
2.salt '*' state.highstate -v
