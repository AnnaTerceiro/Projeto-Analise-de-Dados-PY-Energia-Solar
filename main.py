import json
import urllib.request as req
import matplotlib.pyplot as plt

def graficolinha(x, y):
  plt.plot(x, y)
  plt.title('Grafico Diário')
  plt.xlabel('Horas')
  plt.ylabel('Potência(kW)')
  plt.grid(True)
  plt.savefig('linha.png')
  plt.show()
  plt.close()

def graficobarra(x, y):
  plt.bar(x, y)
  plt.title('Gráfico Mensal')
  plt.xlabel('Dias')
  plt.ylabel('Energia Gerada(kWh)')
  plt.savefig('barras.png')
  plt.show()
  plt.close()

def graficobox(x, y):
  plt.boxplot(y)
  plt.title('SEU TÍTULO')
  plt.xlabel('NOME DO EIXO X')
  plt.ylabel('NOME DO EIXO Y')
  plt.savefig('boxplot.png')
  plt.show()
  plt.close()

dadosmes = []
list_pot_efet = []
num = 0

url = "http://albertocn.sytes.net/2019-1/pi/projeto/arquivos.json"
dados = req.urlopen(url).read().decode()
dados_proc = json.loads(dados)

print('Deseja ver a lista de dias que houve geração de energia? Responda com S ou N')
show_energy_list = input()
if show_energy_list == 'S':
  print('Dias em que houve geração de energia:')
  for i in dados_proc:
    i = i.replace('dia_', '')
    i = i.replace('_', '/')
    i = i.replace('.json', '')
    print(i)
    

print('Insira o Ano:')
yr = input()
print('Mostrar gráfico semestral? Responda com S ou N')
show_box_graph = input()

print('Insira o Mês:')
mth = input()
print('Mostrar gráfico mensal? Responda com S ou N')
show_bar_graph = input()

print('Insira o Dia:')
day = input()
print('Mostrar gráfico diário? Responda com S ou N')
show_line_graph = input()


link = 'http://albertocn.sytes.net/2019-1/pi/projeto/dia_X_Y_Z.json'
for X in link:
  link2 = link.replace('X', yr)
for Y in link2:
  link3 = link2.replace('Y', mth)
for Z in link3:
  link4 = link3.replace('Z', day)

#try:
if show_box_graph == 'S':
  print('teste')

if show_bar_graph == 'S':
  if Y == '04' or Y == '06':
    for i in range(1,10):
      i = str(i)
      linkmes10 = link3.replace('Z', '0'+ i)
      arquivo = req.urlopen(linkmes10).read().decode()
      arquivo_proc = json.loads(arquivo)
      dados10 = arquivo_proc['energiaDia']
      if dados10 == -1:
        dados10 = 0
      dadosmes.append(dados10)
    for i in range(11, 31):
      i = str(i)
      linkmes31 = link3.replace('Z', i)
      arquivo = req.urlopen(linkmes31).read().decode()
      arquivo_proc = json.loads(arquivo)
      dados31 = arquivo_proc['energiaDia']
      if dados31 == -1:
        dados31 = 0
      dadosmes.append(dados31)
    num = len(dadosmes)
    graficobarra(range(num), dadosmes)
  elif Y == '01' or Y == '03' or Y == '05':
    for i in range(1,10):
      i = str(i)
      linkmes10 = link3.replace('Z', '0'+ i)
      arquivo = req.urlopen(linkmes10).read().decode()
      arquivo_proc = json.loads(arquivo)
      dados10 = arquivo_proc['energiaDia']
      if dados10 == -1:
        dados10 = 0
      dadosmes.append(dados10)
    for i in range(11, 32):
      i = str(i)
      linkmes31 = link3.replace('Z', i)
      arquivo = req.urlopen(linkmes31).read().decode()
      arquivo_proc = json.loads(arquivo)
      dados31 = arquivo_proc['energiaDia']
      if dados31 == -1:
        dados31 = 0
      dadosmes.append(dados31)
    num = len(dadosmes)
    graficobarra(range(num), dadosmes)
  else:
    for i in range(1,10):
      if i == -1:
        i = 0
      i = str(i)
      linkmes10 = link3.replace('Z', '0'+ i)
      arquivo = req.urlopen(linkmes10).read().decode()
      arquivo_proc = json.loads(arquivo)
      dados10 = arquivo_proc['energiaDia']
      if dados10 == -1:
        dados10 = 0
      dadosmes.append(dados10)
    for i in range(11, 29):
      i = str(i)
      linkmes31 = link3.replace('Z', i)
      arquivo = req.urlopen(linkmes31).read().decode()
      arquivo_proc = json.loads(arquivo)
      dados31 = arquivo_proc['energiaDia']
      if dados31 == -1:
        dados31 = 0
      dadosmes.append(dados31)
    num = len(dadosmes)
    graficobarra(range(num), dadosmes)


if show_line_graph == 'S':
  arquivo = req.urlopen(link4).read().decode()
  arquivo_proc = json.loads(arquivo)
  dadospot = arquivo_proc["potencia"]
  for i in dadospot:
    if i != -1:
      list_pot_efet.append(i)
  num = len(list_pot_efet)    
  graficolinha(range(num), list_pot_efet)

#except:
#print('Ops! Algo deu errado :/')
#print('Tente colocar uma data que esteja na lista')