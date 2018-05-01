include:
    - zabbix.install
    
config:
    file.managed:
        - name: /usr/local/zabbix/etc/zabbix_agentd.conf
        - user: root
        - mode: 644
        - source: salt://zabbix/files/zabbix_agentd.conf
        - template: jinja
