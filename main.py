import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura_tela = 600
altura_tela = 400
fonte = pygame.font.Font(None, 36)

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Lista de imagens relacionadas ao Powtoon
imagens_quebracabeça = [r"C:\Users\Aline\PycharmProjects\quebracabeça\imagens_quebracabeça\tanjiro.jpg"]

# Escolhe uma imagem aleatória
imagem_escolhida = random.choice(imagens_quebracabeça)

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Quebra-Cabeças")

# Carrega a imagem
imagem = pygame.image.load(imagem_escolhida)
imagem = pygame.transform.scale(imagem, (largura_tela, altura_tela))

# Divide a imagem em peças
def dividir_imagem(imagem):
    pecas = []
    largura_peca = largura_tela // 3
    altura_peca = altura_tela // 3

    for i in range(3):
        for j in range(3):
            peca = imagem.subsurface(j * largura_peca, i * altura_peca, largura_peca, altura_peca)
            pecas.append(peca)

    return pecas

# Lista de peças do quebra-cabeças
pecas_quebra_cabeca = dividir_imagem(imagem)
random.shuffle(pecas_quebra_cabeca)

# Função para desenhar as peças do quebra-cabeças
def desenhar_quebra_cabeca():
    for i, peca in enumerate(pecas_quebra_cabeca):
        linha = i // 3
        coluna = i % 3
        tela.blit(peca, (coluna * largura_tela // 3, linha * altura_tela // 3))

# Função principal
def main():
    rodando = True
    peca_selecionada = None

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicao_clique = evento.pos
                coluna_clique = posicao_clique[0] // (largura_tela // 3)
                linha_clique = posicao_clique[1] // (altura_tela // 3)
                indice_clique = linha_clique * 3 + coluna_clique

                if peca_selecionada is None:
                    peca_selecionada = indice_clique
                else:
                    pecas_quebra_cabeca[indice_clique], pecas_quebra_cabeca[peca_selecionada] = pecas_quebra_cabeca[peca_selecionada], pecas_quebra_cabeca[indice_clique]
                    peca_selecionada = None

        tela.fill(branco)
        desenhar_quebra_cabeca()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
