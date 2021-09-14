import sys #improtar librerias 

print('Hello, World!') #muestra texto en comillas 

print('The sum of 2 and 3 is 5.')#imprime comentario 

sum = int(sys.argv[1]) + int(sys.argv[2]) #realiza la suma 

print('The sum of {0} and {1} is {2}.'.format(sys.argv[1], sys.argv[2], sum))#se imprime el resultado de la suma 
