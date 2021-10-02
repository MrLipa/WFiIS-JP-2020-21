import matplotlib.pyplot as plt
with open("dataout.txt") as pl:
  line=pl.readlines()
  x=list( float(i.split(" ")[0]) for i in line )
  y=list( float(i.split(" ")[1]) for i in line )
  dy=list( float(i.split(" ")[2]) for i in line )
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnoœciami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format okreœlony przez rozszerzenie w nazwie
plt.savefig('res.pdf')
  