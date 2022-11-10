logo = open('C:/Users/paulo-alc/OneDrive/Pictures/Minhas-fotos/paulo2.jpeg', 'rb')
data = logo.read()
logo.close()

logo2 = open('copia.jpeg', 'wb')
logo2.write(data)
logo2.close()
