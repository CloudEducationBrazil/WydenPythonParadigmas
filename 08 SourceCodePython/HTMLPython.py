import cgi
pagina=open("index.html", "w")
pagina.write("<html lang=\"pt-BR\">\n")

pagina.write("<head>\n")
pagina.write("<title>Teste</title>\n")
pagina.write("</head>\n")
pagina.write("Contagem de 10 números\n")
for i in range(10):
    pagina.write("<p>%d</p>\n" % i)

pagina.write("</body>\n")
pagina.write("</html>\n")
pagina.close()