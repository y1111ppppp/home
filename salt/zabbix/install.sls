#zabbix.tar.gz
zabbix_source:
    file.managed:
        - name: /tmp/zabbix-3.4.8.tar.gz
        - unless: test -e /tmp/zabbix-3.4.8.tar.gz
        - source: salt://zabbix/files/zabbix-3.4.8.tar.gz

#extract

extract_zabbix:
    cmd.run:
        - cwd: /tmp
        - names:
            - tar zxf zabbix-3.4.8.tar.gz
            - yum -y install curl-devel
        - unless: test -d /tmp/zabbix-3.4.8
        - require:
            - file: zabbix_source

#user

zabbix_user:
    user.present:
        - name: zabbix
        - uid: 1501
        - createhome: False
        - gid_from_name: True
        - shell: /sbin/nologin

#zabbix_pkgs

zabbix_pkgs:
    pkg.installed:
        - pkgs:
            - gcc
            - openssl-devel
            - pcre-devel
            - zlib-devel
            - gcc-c++
            - libcurl-devel

#zabbix_compile

zabbix_complile:
    cmd.run:
        - cwd: /tmp/zabbix-3.4.8
        - names:
            - ./configure --with-net-snmp --with-libcurl --enable-agent --prefix=/usr/local/zabbix
        - required:
            - pkg: zabbix_pkgs
            - cmd: extract_zabbix

zabbix_make:
    cmd.run:
        - cwd: /tmp/zabbix-3.4.8
        - names:
            - make && make install
        - required:
            - cmd: zabbix_compile
        - unless: test -d /usr/local/zabbix











 
