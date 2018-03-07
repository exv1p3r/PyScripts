####################################################
#               Script para SVN-Dextra             #
#               Autor: Edson Cervantes             #
####################################################
import paramiko
#import socket
def get_connection():
    passwd = open("date.txt", "r")
    ssh = paramiko.SSHClient()         #Se declara el cliente SSH
    ssh.load_system_host_keys()        #Se agrega al listado de los host conocidos
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.30.108', username='root', password=passwd.read(), port=2022)
    return 0

#def restart_nginx(ssh_obj):
#    stdin, stdout, stderr = ssh_obj.exec_command("sudo service nginx restart")

#def reload_supervisor(ssh_obj):
#    stdin, stdout, stderr = ssh_obj.exec_command("sudo supervisorctl reload")

def start_apache(ssh_obj):
    ssh_obj.exec_command("/etc/init.d/apache2 start")

def restart_services():
    print "Iniciamos la conexion"
    ssh_obj = get_connection()
#   print "Reiniciamos nginx"
#   restart_nginx(ssh_obj)
#   print "Recargamos el supervisor"
#   reload_supervisor(ssh_obj)
    print "Iniciamos el servicio de apache"
    start_apache(ssh_obj)
    print "Finalizado correctamente"

if __name__ == '__main__':
    restart_services()