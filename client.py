import socket

# Solicitar IP e porta do servidor ao usuário
IP_Servidor = input("Digite o endereço IP do servidor: ")
PORTA_Servidor = int(input("Digite a porta do servidor: "))

# Criar o socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Destino da conexão (IP + Porta)
DESTINO = (IP_Servidor, PORTA_Servidor)

try:
    # Conectar ao servidor
    tcp.connect(DESTINO)
    print(f"Conectado ao servidor {IP_Servidor}:{PORTA_Servidor}.")
    print("digite 'sair' para desconectar.")

    # Loop principal para enviar mensagens
    while True:
        print("\n")
        mensagem = input("Digite as cooerdenadas no formato [x y], sem colchetes: ")
        if mensagem.lower() == 'sair':
            print("Desconectando...")
            break
        tcp.send(bytes(mensagem, "utf8"))
        mensagemRecebida = tcp.recv(1024)
        print("\n")
        if mensagemRecebida:
            print(mensagemRecebida.decode("utf8"))
except socket.error as e:
    print(f"Erro ao conectar ou enviar dados: {e}")
finally:
    tcp.close()
    print("Conexão encerrada.")