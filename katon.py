import os
import re
import sys
import time
import bcrypt
import socket
import string
import random
import hashlib
import telebot 
import getpass
import smtplib
import platform
import telnetlib
import mysql.connector
from datetime import datetime
from mysql.connector import errorcode
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 

api_id = '1811260'
api_hash = 'ac0179d0690aad26956e44e82b4ac20c'
token = "1252699993:AAGSV7-0Fb8HMA7Ld22-HbcJlYV7bBfyspQ"
phone = '+55 11 9 46543738'

client = TelegramClient('session', api_id, api_hash) 
client.connect() 

if not client.is_user_authorized(): 
    client.send_code_request(phone) 
    client.sign_in(phone, input('Entre com o codigo recebido em seu dispositivo: ')) 

def telgram ():
    try: 
        #receiver = InputPeerUser(788783751,-1972388975124423645)
        receiver1 = InputPeerUser(599782063,-6324027267714872446)
        receiver2 = InputPeerUser(529392635,-6354106180302249604)
        #client.send_message(receiver, 'A(s) porta(s) '+ str (a) +' \npara o endereço '+ endrrr +' \nestá '+ doorime + '\nVERIFIQUE AS REGRAS DE FIREWALL !!!', parse_mode='html') 
        client.send_message(receiver1, 'A(s) porta(s) '+ str (a) +' \npara o endereço '+ endrrr +' \nestá '+ doorime + '\nVERIFIQUE AS REGRAS DE FIREWALL !!!', parse_mode='html') 
        client.send_message(receiver2, 'A(s) porta(s) '+ str (a) +' \npara o endereço '+ endrrr +' \nestá '+ doorime + '\nVERIFIQUE AS REGRAS DE FIREWALL !!!', parse_mode='html') 

    except Exception as e: 
        print(e)
    #client.disconnect()

pc = platform.node()
maquina = platform.machine()
plataforma = platform.platform()
sistema: platform.system()
data_hora = datetime.now()
data_format = str(data_hora.strftime(' %d/%m/%Y às %H:%M:%S'))
tentativas = int(0)

con = mysql.connector.connect(
    host='177.152.84.139',
    user='katon',
    password=open('C:\\Users\\Administrador.WIN-542JQ3AL7AI\\AppData\\Local\\50844c3646d6f9f33e6ced3ba897666c.txt').read().strip(),
    database='katon'
)
cursor = con.cursor()

class Usuarios():
    def __init__(self,usuario,senha):    
        self.login = usuario
        self.senha = senha

class Equipamentos():
    codigo = 0
    nome = ''
    tipo = ''
    modelo = ''
    endereco_ip = ''

    def __init__(self,codigo,nome,tipo,modelo,endereco_ip):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.modelo = modelo
        self.endereco_ip = endereco_ip

    def info(self):
        os.system('cls')
        print("1 - Código do equipamento........", self.codigo)
        print("2 - Nome do equipamento..........", self.nome)
        print("3 - Ipo do equipamento...........", self.tipo)
        print("4 - Modelo do equipamento........", self.modelo)
        print("5 - Endereço IP do equipamento...",self.endereco_ip)
    pass

def funcoes():
    while True:
        os.system('cls')
        print("Olá ",str(nome_user),"! Bem vindo ao sistema Katon 🔥.\n")
        print("[1] Usuários")
        print("[2] Dispositivos")
        print("[3] Scan de portas")
        print("[4] Brute force")
        print("[5] Log's")
        print('[6] Portas TCP/UDP')
        print('[7] Alterar sua senha')
        print("[8] Sair do progama")
        print('[9] Logoff')
        print()
        opc = input('Digite a opção desejada: ')
        os.system('cls')    
        if opc == '1':
            metodos_user()
        elif opc == '2':
            metodos_equipamento()
        elif opc == '3':
            metodos_scan()
        elif opc == '4':
            Att()
        elif opc == '5':
            logs() 
        elif opc == '6':
            metodos_portas() 
        elif opc == '7':
            while True:
                os.system('cls')
                senha_antiga = getpass.getpass('Digite a senha antiga: ')
                nova_senha = getpass.getpass('\nDigite a nova senha: ')
                nova_senha_conf = getpass.getpass('Repita a senha: ')    
                cursor.execute(f"SELECT `senha` FROM `katon`.`usuarios` WHERE `id_usuario` = '{id_usuario}';")
                consulta = cursor.fetchall()
                for row in consulta:
                    pass
                if criptografar(senha_antiga) == row[0] and nova_senha == nova_senha_conf:     
                    cursor.execute(f"UPDATE `katon`.`usuarios` SET `senha`='{criptografar(nova_senha)}' WHERE  `id_usuario`={id_usuario};")
                    con.commit()
                    os.system('cls') 
                    log_usuario_atividade(f"Senha alterada ")
                    print('Dados alterados com sucesso!')
                    time.sleep(1)
                    break
                else:
                    print('As senhas não conferem!')
                    os.system('pause')
        elif opc == '8':
            exit() 
        elif opc == '9':
            autenticar()
        else:
            print('Opção inválida!')
                 
def home_equipamento():
    os.system('cls')
    print(nome_user,'> Home > Equipamentos')
    print()
    print('[1] Consultar')
    print('[2] Cadastrar')
    print('[3] Alterar')
    print('[4] Excluir')
    print('[5] Voltar\n')

def metodos_user():
    while True:
        os.system('cls')
        print(nome_user,'> Home > Usuários\n')
        print('[1] Consultar')
        print('[2] Cadastrar')
        print('[3] Alterar')
        print('[4] Excluir')
        print('[5] Voltar\n') 
        opc = input('Digite a opção desejada: ')                  
        if opc == '1':
            os.system('cls')        
            print(nome_user,'> Home > Usuários > Consulta\n')
            consultar_user()
            print()
            os.system('pause')            
        elif opc =='2':
            while True:
                try:
                    os.system('cls')
                    print(nome_user,'> Home > Usuários > Cadastro - [0] para sair\n')
                    nome = input('Nome: ')
                    if nome == '0' or nome == '':
                        break
                    sobrenome = input('Sobrenome: ')
                    if sobrenome == '0' or sobrenome == '':
                        break
                    while True:
                        try:
                            dia = input('Dia do nascimento: ')
                            mes = input('Mês do nascimento: ')
                            ano = input('Ano do nascimento: ')
                            datanascimento = f'{ano}{mes}{dia}' 
                            break
                        except ValueError:
                            print('Somente numeros!')
                            time.sleep(1)
                    cargo = input('Cargo: ')
                    email = input('E-mail: ')
                    login = input('Login: ')       
                    cursor.execute(f'SELECT login FROM `katon`.`usuarios`;')    
                    consulta = cursor.fetchall()
                    for row in consulta:
                        if row[0] == login:
                            print('\nLogin ja cadastrado!')
                            time.sleep(1) 
                            exit()
                    senha = getpass.getpass('Senha: ')
                    senha_conf = getpass.getpass('Repita a senha: ')
                    if senha == senha_conf:
                        cadastrar_user(nome,sobrenome,datanascimento,cargo,email,login,criptografar(senha))
                        os.system('cls')
                        print('\nUsuario cadastrado com sucesso!')
                        time.sleep(1)
                        break
                    else:
                        print('Senhas não conferem! Digite novamente.')
                        time.sleep(1)
                except:
                    os.system('cls')
                    print('\nErro ao cadastrar usuário!')
                    time.sleep(2)
        elif opc =='3': 
            while True:
                os.system('cls')
                print(nome_user,'> Home > Usuários > Alterar - [0] para voltar\n')
                consultar_user()                                                
                id_user = input('\nInforme o ID do usuario: ')
                if id_user == '0':
                    break
                elif id_user == '':
                    os.system('cls')
                    print('\nDigite uma opção!')
                    time.sleep(2)
                else: 
                    os.system('cls')
                    print(nome_user,'> Home > Usuários > Alterar - [0] para voltar\n')
                    consultar_user_where(id_user)
                    campo_alteracao = input('\nInforme o campo que quer alterar: ')
                    while True:
                        if campo_alteracao == '1':
                            campo_alteracao = 'nome'
                            break
                        elif campo_alteracao == '2':
                            campo_alteracao = 'sobrenome'
                            break
                        elif campo_alteracao == '3':
                            campo_alteracao = 'cargo'
                            break
                        elif campo_alteracao == '4':
                            campo_alteracao = 'email'
                            break
                        elif campo_alteracao == '5':
                            campo_alteracao = 'login'
                            break
                        elif campo_alteracao == '6':
                            campo_alteracao = 'senha'
                            break
                        else:
                            print('Campo incorreto!')
                            os.system('pause')
                            break
                    
                    if campo_alteracao == 'senha':
                        cursor.execute(f"SELECT `cargo` FROM `katon`.`usuarios` WHERE `id_usuario`='{id_usuario}';")    
                        consulta = cursor.fetchall()            
                        for row in consulta:
                            pass
                        if row[0] != 'Sysadmin':
                            print('\nVoce não tem autorização para resetar senhas!')
                            time.sleep(2)
                        else:
                            while True:
                                os.system('cls')
                                print(nome_user,'> Home > Usuários > Alterar - Novos Dados\n')
                                novo_campo = getpass.getpass('Digite a nova senha: ')
                                novo_campo_conf = getpass.getpass('Repita a senha: ')                        
                                if novo_campo == novo_campo_conf:
                                    alterar_user(id_user,campo_alteracao,criptografar(novo_campo))
                                    os.system('cls')
                                    print('Dados alterados com sucesso!')
                                    time.sleep(1)
                                    os.system('cls')
                                    print(nome_user,'> Home > Usuários > Alterar - Novos Dados\n')
                                    consultar_user_where(id_user)
                                    break
                                else:
                                    print('As senhas não conferem!')
                                    os.system('pause')
                    else:
                        print()
                        novo_campo = input(f'Novo dado: ')
                        alterar_user(id_user,campo_alteracao,novo_campo)
                        os.system('cls')
                        print(nome_user,'> Home > Usuários > Cadastro - Novos Dados\n')
                        print('='*25)
                        print('{:^25}'.format(u'Dados Atualizados'))
                        print('='*25)
                        consultar_user_where(id_user)
                        os.system('pause')
                        break
        elif opc =='4':
            os.system('cls')
            print(nome_user,'> Home > Usuários > Excluir\n')
            consultar_user()
            id_user = input('Informe o codigo do usuário que quer excluir: ')
            excluir_user(id_user)
            os.system('pause')
        elif opc =='5':
            funcoes()
        else:
            print('\nOpção inválida!')
            time.sleep(1)

def metodos_equipamento():
    while True:
        home_equipamento()
        opc = int(input('Digite a opção: '))
        if opc == 1:
            os.system('cls')
            print(nome_user,'> Home > Equipamentos > Consulta\n')
            consultar_equip()
            os.system('pause')
                    
        elif opc == 2:
            while True:
                os.system('cls')
                print(nome_user,'> Home > Equipamentos > Cadastro - [0] para sair\n')
                time.sleep(1.25)
                os.system('cls')
                nome = input('\nNome do dispositivo: ')
                marca = input('Marca: ')
                tipo = input('Tipo: ')
                modelo = input('Modelo: ')
                ip = input('Endereço IP [X.X.X.X]: ')
                descricao = input('Descrição (Opcional): ')
                if nome == '0' or marca == '0' or tipo == '0' or modelo =='0' or ip == '0':
                    funcoes()           
                else:                      
                    os.system('cls')
                    cadastrar_equip(nome,marca,tipo,modelo,ip,descricao)
                    print()
                    cad = input('Deseja fazer novo cadastro? [S/N]: ')
                    if cad.upper() == 'S':
                        pass
                    else:
                        metodos_equipamento()            
                        
        elif opc == 3:
            while True:
                os.system('cls')
                print(nome_user,'> Home > Equipamentos > Alterar\n')
                while True:
                    try:
                        consultar_equip()
                        id_equip = int(input('Digite o codigo do dispositivo: '))
                        break
                    except ValueError:
                        print('''
                        Somente numeros!
                        ''')
                        time.sleep(1)
                        os.system('cls')
                os.system('cls')
                while True:
                    try:
                        consultar_equip_where(id_equip)
                        campo_alteracao = int(input('Digite o campo que deseja atualizar: '))      
                        break          
                    except ValueError:
                        print('''
                        Somente numeros validos
                        ''')     
                        time.sleep(1)
                while True:
                    if campo_alteracao == 1:
                        campo_alteracao = 'nome'
                        break
                    elif campo_alteracao == 2:
                        campo_alteracao = 'marca'
                        break
                    elif campo_alteracao == 3:
                        campo_alteracao = 'tipo'
                        break
                    elif campo_alteracao == 4:
                        campo_alteracao = 'modelo'
                        break
                    elif campo_alteracao == 5:
                        campo_alteracao = 'ip'
                        break
                    elif campo_alteracao == 6:
                        campo_alteracao = 'descricao'
                        break
                    elif campo_alteracao == 7:
                        break
                    else:
                        os.system('cls')
                        print('Opção inválida!')
                        time.sleep(1)
                novo_campo = input('Digite o novo dado: ')
                alterar_equip(id_equip,campo_alteracao,novo_campo)
                os.system('cls')
                print('''
                
                Dados Atualizados
                
                ''')
                time.sleep(1)
                os.system('cls')
                print('Dados Atualizados\n')
                consultar_equip_where(id_equip)
                print()
                rep = input('Deseja alterar mais algum dispositivo? [S/N]: ')
                if rep.upper() == 'S':
                    pass
                else:
                    break
                
        elif opc == 4:
            os.system('cls')
            print(nome_user,'> Home > Equipamentos > Excluir - [0] para sair\n')
            consultar_equip()
            id_equip = input('\nInforme o codigo do dispositivo que quer excluir: ')
            if id_equip == '' or id_equip == '0':
                metodos_equipamento()
            os.system('cls')
            conf = input('Tem certeza que deseja excluir este item? [S/N]: ')
            if conf.upper() == 'S':
                excluir_equip(id_equip)
                time.sleep(1)
            else:
                pass    
        elif opc == 5:
            funcoes()
        else:
            pass

def metodos_scan():
    def escanear(ip,host):
        portas_vulneraveis = []
        os.system('cls')
        print ("Verificando conexao...\n")
        # ip = row[0]
        # host = row[1]
        cmd = "ping " + ip
        r = ("".join(os.popen(cmd).readlines()))
        try:
            re.search ("64 bytes from", r)
        except:
            print (f"Sem respota do endereço {ip}")
        else:
            print (f"O endereço {ip} esta respondendo\n")
            cursor.execute(f'SELECT * FROM `katon`.`portas` LIMIT 1000;')
            consulta = cursor.fetchall()
            portas_db = []
            for row in consulta:
                portas_db.append(row[0])
                pass
            for porta in portas_db:
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                tcp.settimeout(2)
                conexao = tcp.connect_ex((ip, porta))
                if conexao == 0:
                    print( f'A porta {porta} está aberta')
                    portas_vulneraveis.append(porta)
                else:
                    print(f'A porta {porta} está fechada ')
            portas_rede = str(portas_vulneraveis) 
            log_equipamento(host,ip,portas_rede)
            log_usuario_atividade(f"Scan {ip} ")
            if portas_vulneraveis != []:
                cont = int(0)
                for x in portas_vulneraveis:
                    cont += 1
                if cont > 1:
                    print(f'\nAs portas {str(portas_rede)} estão abertas!', end=' ')
                else:
                    print(f'\nA porta {str(portas_rede)} esta aberta!', end=' ')
                email_porta = input('Deseja enviar uma notificação ao administrador da rede? [S/N]: ')
                while True:
                    global a
                    global doorime
                    global endrrr
                    if email_porta.upper() == 'S':
                        cursor.execute(f"SELECT `email` FROM `katon`.`usuarios` WHERE `cargo`='Sysadmin';") 
                        consulta = cursor.fetchall()
                        app = input('\nPor onde deseja enviar a notificação? E-mail, Telegram ou Ambos? [E/T/A]: ')
                        if app.upper() == 'E':
                            for row_ in consulta:
                                toaddress = str(row_[0])
                                enviar_notificacao_scan(toaddress,portas_rede,ip,host)
                                pass
                            os.system('cls')
                            print('\nE-mail enviado aos administradores de rede\n!')
                            log_usuario_atividade('E-mail enviado aos administradores ')
                            os.system('pause')
                            break
                        elif app.upper() == 'T':
                            a = portas_rede
                            endrrr = ip
                            doorime = "aberta!!!"
                            telgram()
                            print('\nMensagem enviada aos administradores de rede!\n')
                            log_usuario_atividade('Mensagem enviada para o telegram dos administradores ')
                            os.system('pause')
                            break
                        elif app.upper() == 'A':
                            a = portas_rede
                            endrrr = ip
                            doorime = "aberta!!!"
                            telgram()
                            for row_ in consulta:
                                toaddress = str(row_[0])
                                enviar_notificacao_scan(toaddress,portas_rede,ip,host)
                                pass
                            os.system('cls')
                            print('\nNotificação enviada aos administradores de rede!\n')
                            log_usuario_atividade('Notificação enviada aos administradores ')
                            os.system('pause')
                            break
                        else:
                            os.system('cls')
                            print('\nOpção inválida!')       
                            time.sleep(1)                 
                    elif email_porta.upper() == 'N':
                        break
            else:
                print('\nTodas as portas escaneadas estão em conformidade!')
                log_usuario_atividade('Scan executado, equipamento em conformidade')
            time.sleep(2.5)
    while True:
        try:
            while True:
                os.system('cls')
                print(nome_user,'> Home > Scan - [0] para sair\n')
                consultar_equip_porta()
                cod_equip = input("Informe o codigo do equipamento que deseja escanear\nou digite [IP] para inserir um endereço: ") 
                
                if cod_equip == '0' or cod_equip == '':
                    # os.system('cls')
                    # print('\nCodigo inválido!')
                    # time.sleep(1)
                    funcoes()
                elif cod_equip.upper() == 'IP':
                    ip = input('\nInsira o endereço IP da maquina a ser escaneada [X.X.X.X]: ')
                    host = input('\nInsira o nome do Host: ')
                    escanear(ip,host)
                else:
                    cursor.execute(f"SELECT `ip`,`nome` FROM `katon`.`equipamentos` WHERE `id`='{cod_equip}';")    
                    consulta = cursor.fetchall()
                    for row in consulta:
                        pass
                    ip_host = row[0]
                    host = row[1]
                    escanear(ip_host,host)
        except UnboundLocalError:
            print('Erro ao consultar equipamento')
            log_usuario_atividade('Erro ao consultar equipamento')
            time.sleep(1)

def cadastrar_user(nome,sobrenome,datanascimento,cargo,email,login,senha):    
    try: 
        cursor.execute(f'''
            INSERT INTO `katon`.`usuarios` (`nome`, `sobrenome`, `datanascimento`, `cargo`, `email`, `login`, `senha`) 
            VALUES ('{nome}', '{sobrenome}', '{datanascimento}', '{cargo}', '{email}', '{login}', '{senha}');
        ''')
        con.commit()
        print('Usuário cadastrado com sucesso!')
        log_usuario_atividade(f'Usuário {nome} cadastrado ')
    except:
        print('Erro ao cadastrar usuario!' + Exception)
        log_usuario_atividade(f'Erro ao cadastrar o usuario {nome}')
        os.system('pause')

def cadastrar_equip(nome,marca,tipo,modelo,ip,descricao):
    try: 
        cursor.execute(f'''
            INSERT INTO `katon`.`equipamentos` (`nome`, `marca`, `tipo`, `modelo`, `ip`, `descricao`) 
            VALUES ('{nome}', '{marca}', '{tipo}', '{modelo}', '{ip}', '{descricao}');
        ''')
        con.commit()
        print('Equipamento cadastrado!')
        log_usuario_atividade('Equipamento cadastrado ')
    except:
        print('Erro ao cadastrar equipamento!')
        log_usuario_atividade('Falha ao cadastrar equipamento')
 
def consultar_user():   
    cursor.execute(f'SELECT * FROM `katon`.`usuarios` LIMIT 1000;')    
    consulta = cursor.fetchall()
    print(f"{'ID Usuario':.<15}{'Nome':.<15}{'Sobrenome':.<25}{'Cargo':.<25}{'E-mail':.<30}{'Login'}\n")
    for row in consulta:
        print(f"{row[0]:.<15}{row[1]:.<15}{row[2]:.<25}{row[4]:.<25}{row[5]:.<30}{row[6]}")
    
def consultar_equip():
    cursor.execute(f'SELECT * FROM `katon`.`equipamentos` LIMIT 1000;')    
    consulta = cursor.fetchall()
    print(f"{'ID':.<5}{'Nome':.<25}{'Marca':.<20}{'Tipo':.<20}{'Modelo':.<20}{'Endereço IP':.<20}{'Descrição'}")
    for row in consulta:
        print(f"{row[0]:.<5}{row[1]:.<25}{row[2]:.<20}{row[3]:.<20}{row[4]:.<20}{row[5]:.<20}{row[6]}")
    print()

def consultar_equip_porta():
    cursor.execute(f'SELECT * FROM `katon`.`equipamentos` LIMIT 1000;')    
    consulta = cursor.fetchall()
    print(f"{'ID':.<5}{'Nome':.<25}{'Endereço'}\n")
    for row in consulta:
        print(f"{row[0]:.<5}{row[1]:.<25}{row[5]}")
    print()

def consultar_user_where(id_user):
    try:
        cursor.execute(f"SELECT * FROM `katon`.`usuarios` WHERE `id_usuario`= {id_user}")
        consulta = cursor.fetchall()
        for row in consulta:
            print(f'1 - Nome:\t{row[1]: >5}')
            print(f'2 - Sobrenome:\t{row[2]: <5}')
            print(f'3 - Cargo:\t{row[4]: <5}')
            print(f'4 - E-mail:\t{row[5]: <5}')
            print(f'5 - Login:\t{row[6]: <5}')
            print(f'6 - Senha\n')
    except:
        print('Não foi possivel encontrar o usuario.')

def consultar_equip_where(id_equip):
    try:
        cursor.execute(f"SELECT * FROM `katon`.`equipamentos` WHERE `id`= {id_equip}")
        consulta = cursor.fetchall()
        for row in consulta:
            print(f'[1] Nome:\t{row[1]: <5}')
            print(f'[2] Marca:\t{row[2]: <5}')
            print(f'[3] Tipo:\t{row[3]: <5}')
            print(f'[4] Modelo:\t{row[4]: <5}')
            print(f'[5] Endereço IP:\t{row[5]: <5}')
            print(f'[6] Descrição:\t{row[6]: <5}')
            print(f'[7] Voltar\n')
            return row
    except:
        print('Não foi possivel encontrar o usuario.')

def alterar_user(id_user,campo_alteracao,novo_campo):
    try:
        cursor.execute(f"UPDATE `katon`.`usuarios` SET `{campo_alteracao}`='{novo_campo}' WHERE  `id_usuario`={id_user};")
        con.commit()
        log_usuario_atividade('Usuario atualizado ')
    except:
        print('Erro ao cadastrar usuario')
        log_usuario_atividade('Erro ao atualizar usuario ')

def alterar_equip(id_equip,campo_alteracao,novo_campo):
    try:
        cursor.execute(f"UPDATE `katon`.`equipamentos` SET `{campo_alteracao}`='{novo_campo}' WHERE  `id`='{id_equip}';")
        con.commit()
        print('Registro atualizado!')
        log_usuario_atividade('Equipamento atualizado ')
    except:
        print('Erro ao atualizar equipamento.')
        log_usuario_atividade('Falha ao atualizar equipamento ')

def excluir_user(id_user):
    try:            
        cursor.execute(f'DELETE FROM `katon`.`usuarios` WHERE  `id_usuario`= {id_user};')    
        con.commit()
        print('Usuário excluido com sucesso!')
        log_usuario_atividade('Usuário excluido ')
    except:
        print('Não foi possivel excluir o usuario!')
        log_usuario_atividade('Falha ao excluir usuario ')

def excluir_equip(id_equip):
    # try:            
    cursor.execute(f'DELETE FROM `katon`.`equipamentos` WHERE `id`= {id_equip};')    
    con.commit()
    os.system('cls')
    print('Equipamento excluido com sucesso!')
    log_usuario_atividade('Equipamento excluido ')
    time.sleep(1)
    # except:
    #     print('Não foi possivel excluir o equipamento!')

def logs():
    while True:
        os.system('cls')
        try:
            print('[1] Logs de usuários')
            print('[2] Logs de equipamentos')
            print('[3] Voltar')
            opc_log = int(input('\nInsira uma opção: '))
            if opc_log == 1:
                os.system('cls')
                cursor.execute(f'SELECT `login`,`atividade` FROM `katon`.`log_usuarios` LIMIT 1000;')    
                consulta = cursor.fetchall()
                print(f"{'Usuário': <15}{u'Atividade': <100}")
                for row in consulta:
                    print(f"{row[0]: <15}{row[1]: <100}\n")
                os.system('pause')
            elif opc_log == 2:
                os.system('cls')
                cursor.execute(f'SELECT `host`,`data_varredura`,`ip`,`portas_vulneraveis` FROM `katon`.`log_equipamento` LIMIT 1000;')    
                consulta = cursor.fetchall()
                print(f"{'Host': <25}{'Data Varredura': <25}{'Endereço IP': <25}{'Portas Vulneráveis'}\n")
                for row in consulta:
                    print(f"{row[0]: <25}{str(row[1]): <25}{row[2]: <25}{row[3]}")
                os.system('pause')
            elif opc_log == 3:
                break
            else:
                print('Opção inválida!')
                time.sleep(1)
        except ValueError:
            print('Digite somente numeros!')
            os.system('cls')

def logs_usuarios_login(id_usuario,login,atividade):
    data_hora = datetime.now()
    data_format = str(data_hora.strftime(' %d/%m/%Y às %H:%M:%S'))
    cursor.execute(f'''
        INSERT INTO `katon`.`log_usuarios` (`id_usuario`,`login`,`atividade`) 
        VALUES ('{id_usuario}','{login}', '{atividade + data_format}');
    ''')
    con.commit()

def log_usuario_atividade(atividade_atual):
    cursor.execute(f"SELECT `id_log` FROM `katon`.`log_usuarios` WHERE `id_log` =(select MAX(`id_log`) FROM `log_usuarios`);")    
    consulta = cursor.fetchall()
    for row in consulta:
        pass
    id_log = row[0]
    cursor.execute(f"SELECT `atividade` FROM `katon`.`log_usuarios` WHERE `id_log` = {id_log};")    
    consulta = cursor.fetchall()
    for row_ in consulta:
        pass
    atividade = str(row_[0])
    atividade_atual_ = str(atividade_atual)
    atividade_nova = f"{atividade}\n{atividade_atual_}"
    data_hora = datetime.now()
    data_format = str(data_hora.strftime(' %d/%m/%Y às %H:%M:%S'))
    cursor.execute(f"UPDATE `katon`.`log_usuarios` SET `atividade`='{atividade_nova + data_format}' WHERE `id_log`={id_log};")
    con.commit()

def log_equipamento(host,ip,portas_vulneraveis):
    data_hora = datetime.now()
    # data_format = str(data_hora.strftime(' %d/%m/%Y às %H:%M:%S'))
    cursor.execute(f'''
        INSERT INTO `katon`.`log_equipamento` (`host`,`ip`,`data_varredura`,`portas_vulneraveis`) 
        VALUES ('{host}','{ip}', '{data_hora}','{portas_vulneraveis}');
    ''')
    con.commit()

def Att():
    def telnet(HOST,user):
        os.system('cls')
        # user = 'root'
        cont = int(0)
        for y in b:
            cont += 1
            password = y
            try:
                tn = telnetlib.Telnet(HOST,23)
                tn.read_until(b"login: ")
                tn.write(user.encode('ascii') + b"\n")
                if password:
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\n")
            except EOFError:
                print('Conexão Telnet encerrada.')
            except ConnectionRefusedError:
                print(f'Tentativa {cont}. Conexão recusada.')
            except ConnectionResetError:
                print('Foi forçado o cancelamento de uma conexão existente pelo host remoto')
                time.sleep(1)
            except KeyboardInterrupt:
                print('Sessão finalizada por usuário.')
                time.sleep(1)
                break
            except TimeoutError:
                print('O host conectado não respondeu.')
                time.sleep(1)
            except BlockingIOError:
                print('Operação de soquete sem bloqueio não pode ser concluida imediatamente')
                time.sleep(1)
            except ConnectionAbortedError:
                print('Conexão estabelecida foi anulada pelo usuario.')
            else:                
                tn.write(b"ls\n")
                tn.write(b"exit\n")
                print(tn.read_all().decode('ascii'))
                os.system('pause')
    try:
        # while True:
        a = open('login.txt', 'r')
        b = a.readlines()
        a.close()
        os.system('cls')
        print(nome_user,'> Home > Brute Force - [0] para sair\n')
        consultar_equip_porta()
        cod_equip = input('Digite o codigo do equipamento que deseja invadir\nou digite [IP] para entrar com um endereço: ')        
        if cod_equip == '0' or cod_equip == '':
            funcoes()
        elif cod_equip.upper() == 'IP':
            HOST = input('\nInsira o endereço IP da maquina [X.X.X.X]: ')
            user = input('Informe o usuário remoto: ')
            telnet(HOST,user)
        else:
            user = input('Informe o usuário remoto: ')
            cursor.execute(f"SELECT `ip` FROM `katon`.`equipamentos` WHERE `id`='{cod_equip}';")    
            consulta = cursor.fetchall()
            for row in consulta:
                pass
            HOST = str(row[0])
            telnet(HOST,user)
        # user = input('Insira o usuario remoto: ')
        
    except KeyboardInterrupt:
        print('Sessão finalizada por usuário.') 
    except ConnectionAbortedError:
        print('Conexão estabelecida foi anulada pelo host.')
    print('\nWorld list completa')
    time.sleep(2)
    Att()     

def metodos_portas():
    while True:
        try:
            os.system('cls')
            print('[1] Conferir portas cadastradas')
            print('[2] Cadastrar portas')
            print('[3] Alterar portas')
            print('[4] Excluir portas')
            print('[5] Voltar\n')
            opc_porta = int(input('Selecione uma opção: '))
            if opc_porta == 1:   
                os.system('cls')
                consultar_portas()
                os.system('pause')

            elif opc_porta == 2:
                while True:
                    os.system('cls')
                    num_porta = int(input('Insira o numero da porta: '))
                    nome_porta = input('Insira o nome da porta: ')
                    cadastrar_portas(num_porta,nome_porta)
                    print('\nPorta cadastrada com sucesso!')
                    time.sleep(1)
                    os.system('cls')
                    opc = input('Deseja cadastrar outra porta? [S/N]: ')
                    if opc.upper() == 'S':
                        pass
                    else:
                        break
                break
                
            elif opc_porta == 3:
                os.system('cls')
                consultar_portas()
                num_porta = int(input('\nInsira o numero da porta que deseja alterar: '))
                print('[1] Porta')
                print('[2] Nome')
                campo_alteracao = int(input('\nQual campo deseja alterar? '))
                novo_campo = input('Insira o novo dado: ')
                alterar_porta(campo_alteracao,novo_campo,num_porta)
                time.sleep(1)

            elif opc_porta == 4:
                consultar_portas()
                num_porta = int(input('\nInsira o numero da porta que deseja excluir: '))
                excluir_porta(num_porta)
                time.sleep(1)

            elif opc_porta == 5:
                funcoes()
        except ValueError:
            print('Opção inválida!')
            time.sleep(1)

def consultar_portas():
    cursor.execute(f'SELECT * FROM `katon`.`portas` ORDER BY num_porta ASC;')    
    consulta = cursor.fetchall()
    print(f"{'Porta': <10}{'Nome'}\n")
    for row in consulta:
        print(f"{row[0]: <10}{row[1]}")

def cadastrar_portas(num_porta,nome):
    cursor.execute(f'''
    INSERT INTO `katon`.`portas` (`num_porta`, `nome`) VALUES ('{num_porta}', '{nome}');''')
    con.commit()

def alterar_porta(campo_alteracao,novo_campo,num_porta):
    cursor.execute(f"UPDATE `katon`.`portas` SET `{campo_alteracao}`='{novo_campo}' WHERE `num_porta`={num_porta};")
    con.commit()
    log_usuario_atividade(f"Fez alterações nas configurações de porta")
    print('Registro atualizado!')

def excluir_porta(num_porta):
    cursor.execute(f'DELETE FROM `katon`.`portas` WHERE  `num_porta`= {num_porta};')    
    con.commit()
    print('Porta excluida com sucesso!')

def gerador_senha(tam=6,caracteres=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(caracteres) for _ in range(tam))

def enviar_notificacao_senha(toaddress,senha,login):
    fromaddress = 'projeto.katon@gmail.com'
    # toaddress = ''
    username = 'projeto.katon@gmail.com' 

    msg = MIMEMultipart()
    msg['From'] = fromaddress
    msg['To'] = toaddress
    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,open('C:\\Users\\Administrador.WIN-542JQ3AL7AI\\AppData\\Local\\50844c3646d6f9f33e6ced3ba897666c.txt').read().strip())
    cursor.execute(f"SELECT `nome`,`sobrenome` FROM `katon`.`usuarios` WHERE `login`='{login}';")    
    consulta = cursor.fetchall()            
    for row in consulta:
        pass
    nome_user = row[0]
    sobrenome = row[1]
    texto = f'''    
    Prezado(a) {nome_user} {sobrenome},

    A senha de acesso ao sistema Katon foi redefinida com sucesso.

    Insira o código para alterar sua senha no proximo login: {senha}

    Caso não tenha feito esta alteração ou acredita que um usuário não autorizado tenha acessado sua conta, 
    entre em contato com os administradores para redefinir sua senha imediatamente. 

    Caso precise de ajuda adicional, contate a equipe Katon.
    Atenciosamente,
    Suporte Katon


    Equipe Katon

    Cel.: (11) 97070-7070
    Tel.: (11) 7070-7070
    E-mail: projeto.katon@gmail.com
    '''
    msg.attach(MIMEText(texto, 'plain'))
    msg['Subject'] = 'Grupo Katon | Alteração de senha'
    server.sendmail(fromaddress,msg['To'].split(','),msg.as_string())
    server.quit

def enviar_notificacao_scan(toaddress,portas_vulneraveis,ip,host):
    fromaddress = 'projeto.katon@gmail.com'
    # toaddress = ''
    username = 'projeto.katon@gmail.com' 
    msg = MIMEMultipart()
    msg['From'] = fromaddress
    msg['To'] = toaddress
    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,open('C:\\Users\\Administrador.WIN-542JQ3AL7AI\\AppData\\Local\\50844c3646d6f9f33e6ced3ba897666c.txt').read().strip())
    texto = f'''
    Cuidado!

    O scan de portas foi executado e identificamos as seguintes vulnerabilidades: 
    
    Operador: {nome_user}
    Portas Abertas: {portas_vulneraveis} 
    Nome do host: {host}
    Endereço: {ip}

    Reveja as regras de firewall!'''
    msg.attach(MIMEText(texto, 'plain'))
    msg['Subject'] = 'Grupo Katon | Portas vulneráveis!'
    server.sendmail(fromaddress,msg['To'].split(','),msg.as_string())
    server.quit

def criptografar(senha):
    # senha = input('Senha: ')
    senha = senha.encode('utf-8')
    senha_criptografada = hashlib.md5(senha).hexdigest()
    # print(senha_criptografada)
    return senha_criptografada

def autenticar():
    global login
    tentativa = int(0)
    while True:
        os.system('cls')
        print('='*25)
        print('{:^25}'.format(u'Login - [0] para sair'))
        print('='*25)
        login = input('Usuário: ')
        if login == '0':
            exit()
        senha = getpass.getpass('Senha: ')
        print('='*25)

        cursor.execute(f"SELECT `login`,`senha`,`nome`,`id_usuario`,`email` FROM `katon`.`usuarios` WHERE `login`='{login}';")    
        consulta = cursor.fetchall()            
        for row in consulta:
            pass
        global nome_user
        global id_usuario
        global toaddress
        
        id_usuario = row[3]
        logs_usuarios_login(row[3],row[0],f"Login ")     
        criptografar(senha)
        if login == row[0] and criptografar(senha) == row[1]:
            
            nome_user = row[2]
            log_usuario_atividade(f"Login com sucesso ")
            funcoes()
            break
        else:
            print('\nLogin ou senha incorreta\n')
            log_usuario_atividade(f"Senha incorreta ")
            time.sleep(1)
            tentativa += 1
            if tentativa == 3:
                rec = input('Gostaria de redefinir sua senha? [S/N]: ')
                if rec.upper() == 'S':
                    nova_senha = str(gerador_senha())
                    cursor.execute(f"UPDATE `katon`.`usuarios` SET `senha`='{criptografar(nova_senha)}' WHERE  `id_usuario`={row[3]};")
                    con.commit()
                    toaddress = str(row[4])
                    enviar_notificacao_senha(toaddress, nova_senha,login)
                    os.system('cls')
                    print('\nSenha enviada no e-mail cadastrado. Insira no proximo login.\n')
                    tentativa = 0
                    os.system('pause')
                else:
                    tentativa = 0
                    pass
            else:
                pass
    return(login)

#=================================Inicio do codigo============================================

autenticar()