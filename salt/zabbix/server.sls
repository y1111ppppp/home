include:
    - zabbix.install
    
server:
    file.managed:
        - name: /etc/init.d/zabbix_agentd
        - user: zabbix
        - mode: 755
        - unless: test -d /etc/init.d/zabbix_agentd
        - source: salt://zabbix/files/zabbix_agentd
    service.running:
        - name: zabbix_agentd
        - enable: True
        - reload: True
        - watch:
            - file: /etc/init.d/zabbix_agentd
