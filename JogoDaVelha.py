class JogoDaVelha():
    def __init__(self, jogador):
        self.jogador_atual = jogador
        self.tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def mostrarTabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro[0][0]} │ {self.tabuleiro[0][1]} │ {self.tabuleiro[0][2]} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro[1][0]} │ {self.tabuleiro[1][1]} │ {self.tabuleiro[1][2]} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro[2][0]} │ {self.tabuleiro[2][1]} │ {self.tabuleiro[2][2]} │")
        print("└───┴───┴───┘")

    def setJogada(self, x, y, jogada):
        self.tabuleiro[x][y] = jogada

    def testeJogada(self, x, y):
        if 0 <= x <= 2 and 0 <= y <= 2:
            if self.tabuleiro[x][y] == ' ':
                return True
            return False
        return False
    
    def vencido(self):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
                return True
        
        # Verificar colunas
        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] and self.tabuleiro[0][col] != ' ':
                return True
        
        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] != ' ':
            return True
        
        return False

    def empate(self):
        if self.tabuleiro[0][0] != ' ' and self.tabuleiro[0][1] != ' ' and self.tabuleiro[0][2] != ' ' and self.tabuleiro[1][0] != ' ' and self.tabuleiro[1][1] != ' ' and self.tabuleiro[1][2] != ' ' and self.tabuleiro[2][0] != ' ' and self.tabuleiro[2][1] != ' ' and self.tabuleiro[2][2] != ' ':
            return True
        return False