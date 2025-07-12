import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from youtube_functions import DownloadAudio
from youtube_functions import DownloadVideo
import customtkinter


def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    root.geometry(f"{largura}x{altura}+{x}+{y}")


window = customtkinter.CTk()
window.resizable(False, False)
largura_janela = 600
altura_janela = 400
centralizar_janela(window, largura_janela, altura_janela)

# Titulo da Janela
window.title("Youtube Download")

# Váriaveis
style = ttk.Style()
check_var = tk.StringVar()


# Função para pegar o valor do radio clicado
def on_checkbox_click():
    selected_value = check_var.get()
    return selected_value


# Function para poder escolher local para salvar o arquivo
def escolher_local_salvar():
    local_salvar = filedialog.askdirectory()

    if local_salvar:
        label_resultado.configure(text=f"Local de Salvar: {local_salvar}")
        global caminho_salvar
        caminho_salvar = local_salvar
    else:
        label_resultado.configure(text="Nenhum local de salvar selecionado")


# Function para limpar a mensagem de download concluido ou de erro
def limpar_mensagem():
    label_resultado.configure(text=caminho_salvar)


# Função para está fazendo download do audio ou video quando for clicado no botão
def Download():
    link = entry.get()
    check_selected = on_checkbox_click()

    if not link:
        label_resultado.configure(text="Erro: insira um link do Youtube válido")
        return
    try:
        if check_selected == "Audio":
            DownloadAudio(link, caminho_salvar)
            label_resultado.configure(text="Download do áudio concluido.")

        elif check_selected == "Video":
            DownloadVideo(link, caminho_salvar)
            label_resultado.configure(text="Download do video concluido.")
        window.after(3000, limpar_mensagem)
    except Exception as e:
        label_resultado.configure(text=f"Erro: {str(e)}")
        print(e)
        window.after(3000, limpar_mensagem)


label = customtkinter.CTkLabel(
    master=window, text="Link do YouTube", font=("Roboto", 24)
)
label.pack(pady=10)

entry = customtkinter.CTkEntry(
    master=window,
    width=520,
    placeholder_text="Link do youtube",
    height=34,
    font=("Roboto", 16),
)
entry.pack(pady=10)

check_button1 = customtkinter.CTkRadioButton(
    window,
    text="Audio",
    variable=check_var,
    value="Audio",
    command=on_checkbox_click,
    font=("Roboto", 20),
    hover_color="red",
    fg_color="red",
    border_width_checked=11,
    border_width_unchecked=3,
)
check_button1.pack(pady=3)

check_button2 = customtkinter.CTkRadioButton(
    master=window,
    text="Video",
    variable=check_var,
    value="Video",
    command=on_checkbox_click,
    font=("Roboto", 20),
    hover_color="red",
    fg_color="red",
    border_width_checked=11,
    border_width_unchecked=3,
)
check_button2.pack()

botao_escolher = customtkinter.CTkButton(
    master=window,
    text="Escolher Local de Salvar",
    command=escolher_local_salvar,
    font=("Roboto", 24),
    height=52,
    fg_color="#ff0000",
    hover_color="#5e0000",
    corner_radius=25,
)
botao_escolher.pack(pady=10)

label_resultado = customtkinter.CTkLabel(
    master=window, text="Nenhum local de salvar selecionado", font=("Roboto", 24)
)
label_resultado.pack()

buttonDownload = customtkinter.CTkButton(
    master=window,
    text="Download",
    command=Download,
    font=("Roboto", 24),
    height=52,
    fg_color="#ff0000",
    hover_color="#5e0000",
    corner_radius=24,
)
buttonDownload.pack(pady=25)

window.mainloop()
