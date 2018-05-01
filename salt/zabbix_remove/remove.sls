#zabbix_remove
zabbix_source:
    cmd.run:
        - names: 
            - rm -rf /tmp/zabbix-3.4.8
            - rm -f /etc/init.d/zabbix_agentd
            - rm -rf /usr/local/zabbix
            - yum -y remove curl-devel
        - onlyif: test -f /tmp/zabbix-3.4.8.tar.gz


#extract

#remove_zabbix:
#    cmd.run:
#        - cwd: /usr/local
#        - names:
#            - rm -rf zabbix 
#            - yum -y remove curl-devel
#        - onlyif: test -d /usr/local/zabbix
#        - require:
#            - file: zabbix_source

#user

#zabbix_user:
#    user.present:
#        - name: zabbix
#        - uid: 1501
#        - createhome: False
#        - gid_from_name: True
#        - shell: /sbin/nologin

#zabbix_pkgs

zabbix_pkgs:
    pkg.removed:
        - pkgs:
            - gcc
            - openssl-devel
            - pcre-devel
            - zlib-devel
            - gcc-c++
            - libcurl-devel

zabbix_clean:
    cmd.run:
        - names:
            - find / -name "zabbix*" -exec rm -rf {} \;
        - require:
            - pkg: zabbix_pkgs

#zabbix_compile

#zabbix_complile:
#    cmd.run:
#        - cwd: /tmp/zabbix-3.4.8
#        - names:
#            - ./configure --with-net-snmp --with-libcurl --enable-agent --prefix=/usr/local/zabbix
#        - required:
#            - pkg: zabbix_pkgs
#            - cmd: extract_zabbix

#zabbix_make:
#    cmd.run:
#        - cwd: /tmp/zabbix-3.4.8
#        - names:
#            - make && make install
#        - required:
#            - cmd: zabbix_compile
#        - unless: test -d /usr/local/zabbix











 
