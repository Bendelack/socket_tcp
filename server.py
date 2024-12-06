#!/usr/bin/python3
import socket
import threading
from JogoDaVelha import JogoDaVelha

MINHA_PORTA = int(input("Digite a porta que o servidor deve ouvir: "))
MEU_IP = ''

# Criar o socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)

tcp.bind(MEU_SERVIDOR)
tcp.listen(2)  # Começar a ouvir (permite dois clientes por vez)

print(f"Servidor ouvindo na porta {MINHA_PORTA}...")

jogo = JogoDaVelha(0)
jogo.mostrarTabuleiro()
jogadores = []
jogadorAtual = 0

def jogadorConectado(conexao, jogador_id):
    global jogadorAtual
    while True:
        try:
            mensagemRecebida = conexao.recv(1024)
            if mensagemRecebida:
                if jogadorAtual == jogador_id:
                    print(f'jogador {jogadorAtual + 1} mandou {mensagemRecebida.decode("utf8")}')
                    letra = 'X'
                    if jogadorAtual == 1:
                        letra = 'O'

                    coordenadas = mensagemRecebida.decode("utf8").split(' ')
                    x = int(coordenadas[0])
                    y = int(coordenadas[1])
                    if len(coordenadas) == 2 and jogo.testeJogada(x, y):
                        jogadorAtual = 1 - jogadorAtual
                        jogo.setJogada(x, y, letra)
                        jogo.mostrarTabuleiro()
                        if jogo.vencido():
                            print(f'O jogador {(1 - jogadorAtual) + 1} venceu! Parabéns!')
                            conexao.send(f'O jogador {(1 - jogadorAtual) + 1} venceu!'.encode())
                            break
                        elif jogo.empate():
                            print("Deu velha!")
                            conexao.send(f'Deu velha!'.encode())
                            break
                        else:
                            conexao.send(f'Vez do jogador {jogadorAtual + 1}'.encode())
                    else:
                        conexao.send('Por favor mande uma coordenada válida.'.encode())
                else:
                    conexao.send('Ops. Não chegou a sua vez de jogar.'.encode())
        except:
            break

print("Aguardando jogadores...")
while len(jogadores) < 2:
    conexao, endereco = tcp.accept()
    jogadores.append(conexao)
    print(f'jogador {len(jogadores)} conectado...')

    thread = threading.Thread(target=jogadorConectado, args=(conexao, len(jogadores) - 1,))
    thread.start()

print("O jogo começou!!")

