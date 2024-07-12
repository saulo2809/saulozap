# titulo: saulozap
# botao: Iniciar chat
    # popup/modal/alerta
        # titulo: Bem vindo ao saulozap
        # campo de texto: escreva seu nome no chat
        # botao: entrar no chat
            # sumir com o popup e o botao inicial
            # fechar o popup
            # criar o chat ('nome do usuario' entrou no chat)
            # embaixo do chat
                # campo de texto: digite sua mensagem
                # botao: enviar
                    # vai aparecer a mensagem no chat com o nome do usuario

# flet -> aplicativo/site/programa de computador

# importar o flet
import flet as ft

# criar a funcao principal do sistema
def main(pagina):
    # criar algo
    titulo = ft.Text('saulozap', size=40)

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    # cria o tunel de publicacao
    pagina.pubsub.subscribe(enviar_mensagem_tunel)    

    titulo_janela = ft.Text('Bem vindo ao saulozap!')
    campo_nome_usuario = ft.TextField(label='Escreva seu nome no chat')


    def enviar_mensagem(evento):
        texto = f'{campo_nome_usuario.value}: {texto_mensagem.value}'
        # enviar a mensagem no chat

        # enviar uma mensagem no tunel
        pagina.pubsub.send_all(texto)

        # limpar o campo de mensagem
        texto_mensagem.value = ''
        pagina.update()

    texto_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    chat = ft.Column()

    # colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    def entrar_chat(evento):
         # tirar o titulo
         pagina.remove(titulo)
         # tirar o botao iniciar
         pagina.remove(botao_iniciar)
         # fechar popup
         janela.open = False
         # criar o chat
         pagina.add(chat)
         # criar campo de texto de enviar mensagem
         # criar botao enviar mensagem
            # linha de mensagem:
         pagina.add(linha_mensagem)   

         # escrever a mensagem usuario entrou no chat
         texto_entrou_chat = f'{campo_nome_usuario.value} entrou no chat'
         pagina.pubsub.send_all(texto_entrou_chat)
         pagina.update()
        
    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario, 
        actions= [botao_entrar]
    )

    def abrir_popup(evento):
        # print('Clicou no botao')
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', height=50, width=200, on_click=abrir_popup)

    # colocar na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar seu sistema
ft.app(main, view=ft.WEB_BROWSER)