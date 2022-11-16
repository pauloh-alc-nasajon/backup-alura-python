from leitor import LeitoDeArquivo


# try:
#     leitor = LeitoDeArquivo('arquivo.txt')
#     leitor.ler_proxima_linha()
#     leitor.ler_proxima_linha()
#     leitor.ler_proxima_linha()
# #
# # except IOError:
# #     print('Excecao do tipo IOError capturada e tratada')
# finally:
#     if 'leitor' in locals():
#         leitor.fechar()

with LeitoDeArquivo("aquivo.txt") as leitor:
    leitor.ler_proxima_linha()
