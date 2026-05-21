import tkinter as tk

root = tk.Tk(); #cria a janela
root.title("Calculadora"); #titulo da janela
root.geometry("280x350"); #tamanho da janela  
root.config(bg="#F48F68"); #configura a cor de fundo da janela

display = tk.StringVar(value="0"); 
#variavel para armazenar o valor exibido no display da calculadora

tk.Label(root,  
textvariable=display, 
font=("Arial", 24, "bold"), 
bg="#F48F68", 
fg="#FFF6DE").pack(
    fill="x", 
    padx=10, 
    pady=10); 
#tk.Label é um widget do tkinter usado para exibir texto ou imagens.
#textvariable=display vincula a variável display ao texto exibido no label,
#bg="#111" define a cor de fundo do label, fg="#0ff" define a cor do texto,
#pack() é um método de layout que organiza os widgets na janela, fill="x" faz com que o label preencha horizontalmente, padx e pady adicionam espaçamento ao redor do label.

def click(btn): 
    current = display.get() 
    if btn == "C": display.set("0")
    elif btn == "=":
        try: 
            display.set(str(eval(current)))
        except: 
            display.set("Erro")
    else:
        display.set(current + btn if current 
                    != "0" else btn)

#função para lidar com os cliques dos botões da calculadora
#obtém o valor atual do display usando display.get()
#se o botão clicado for "C", o display é resetado para "0"  
#se o botão clicado for "=", a expressão atual é avaliada usando eval() e o resultado é exibido no display. Se houver um erro na avaliação, "Erro" é exibido.
#para outros botões, o valor do botão é adicionado ao display. Se o display atual for "0", ele é substituído pelo valor do botão.
#display.set() é usado para atualizar o valor exibido no display da calculadora.

buttons = [
    ["C", "", "", "/"],
    ["7", "8", "9", "*",],
    ["4", "5", "6", "-",],
    ["1", "2", "3", "+",],
    ["0", ".", "", "="]
]
#lista de botões da calculadora organizados em linhas

for i, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#F48F68")
    frame.pack(fill="x", padx=10, pady=2)
    for j, btn in enumerate(row):
        color = ("#8BDFDD" if btn in "/*-+=%" 
        else "#FFF6DE" if btn == "C" 
        else "#FFE394")

        btn_widget = tk.Label(frame, text=btn, font=("Arial", 14, ), bg=color, fg="#000", width=5, height=2, relief="flat")

        btn_widget.bind("<Button-1>", lambda e, b=btn: click(b))
        btn_widget.pack(side="left", padx=2)

#for i, row in enumerate(buttons) itera sobre cada linha de botões, criando um frame para cada linha e empacotando-o na janela.
#frame.pack(fill="x", padx=10, pady=2) organiza o frame horizontalmente com espaçamento ao redor.
#for j, btn in enumerate(row) itera sobre cada botão na linha, criando um widget de label para cada botão com a cor de fundo e texto apropriados.
#btn_widget.bind("<Button-1>", lambda e, b=btn: click(b)) vincula o evento de clique do mouse ao widget do botão, chamando a função click() com o valor do botão quando clicado.


#https://colorhunt.co/palette/fff6de8bdfddf48f68ffe394 - PALETA USADA 
root.mainloop(); #mantem a janela aberta, sem isso a janela apareceria e sumiria imediatamente