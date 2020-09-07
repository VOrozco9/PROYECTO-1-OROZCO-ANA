from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches


print("Bienvenido a LifeStore\n")
for k in range(9):
  if k <=4:
    for j in range(k+1):
      print("*", end=" /")
  elif k==5:
    print("\n Disfruta tu Avenida\n   Que vida solo hay Una\n     Tú eliges como vivirla")
  else:
    for j in range(9-k):
      print("*",end="/ ")
  print()
print("")
usuarios_clientes=[("Ana","123")]
usuarios_administrador=["Admin1","M1ll4"],["Admin2","M3tr0"]

usuario_entrada=input('Favor de ingresar tu usuario: ')
usuario_password=input('Favor de ingresar tu contraseña: ')

es_admin=0
correcta=0
#Aqui se hace una comparacion primero con los administradores 
#ya que si no esta dentro de la lista de administradores, se pasa directo a la de clientes
for usuario in usuarios_administrador:
  if usuario[0]==usuario_entrada: 
    if usuario[1]== usuario_password:
      
      print("\nBienvenido a lifestore Administrador: "+ usuario[0])
      es_admin=1
      #Una vez que entramos como administrador en el siguiente bloque se habla de los permisos o habilidades que puede hacer el administrador



      print("\nCuentas con las siguientes opciones a realizar: \n 1)Agregar nuevo cliente\n 2)Reporte - Más vendidos \n 3)Reporte - Los mas Buscados \n 4)Reporte - Los menos vendidos \n 5)Reporte - Los menos buscados \n 6)Reporte - Mejores Reseñas\n 7)Reporte - Peores Reseñas\n 8)Reporte de Totales")
      opcion_seleccionada=input("\n Opcion: ")
      #Hacemos un while para que repita el preguntar las opciones a realizar si esta incorrecta o no
      
      while correcta !=1:
        if opcion_seleccionada=="1":
          print("Seleccionaste Agregar un nuevo cliente")
          correcta=1
          agregar_usuario=input("¿Desea crear un nuevo usuario? (si/no): ")
          while agregar_usuario =="si":
            nuevo_usuario=input("Ingresa nombre: " )
            nueva_password=input("Ingresa password: ")
            usuarios_clientes.append((nuevo_usuario, nueva_password))
            print("Usuario agregado con exito")
            agregar_usuario=input("¿Deseas agregar otro usuario? (si/no): ")
            print(usuarios_clientes[1])
            continue

        elif opcion_seleccionada=="2":
          print("Seleccionaste Más vendidos")
          correcta=1
          
          contador=0
          total_ventas=[]
          #Codigo que cuenta los productos, asi sabremos cuantas veces se adquirio dicho producto

          for producto in lifestore_products: #for 1 busca en la lista productos
              for venta in lifestore_sales: #for 2 busca en la lista de ventas
                if producto[0]== venta[1]:
                  contador+=1
              formato_ideal=[producto[0], contador,producto[1]]# le damos el formato que vamos a necesitar, en este caso [Id, Contador,Nombre]
              total_ventas.append(formato_ideal)
              contador=0

          #print("El resultado del reporte: \n Total de ventas\n")

          ordenados=[]

          while  total_ventas:
            maximo=total_ventas[0][1]
            lista_actual=total_ventas[0]
            for grupo in total_ventas:
                if grupo[1]>maximo:
                    maximo=grupo[1]
                    lista_actual=grupo
            ordenados.append(lista_actual)
            total_ventas.remove(lista_actual)
          print("\n Ordenados los datos: \n")
          for indice in range(0,50):
            contador+=1
            print("\n No. ",contador,"|| Nombre: ",ordenados[indice][2])
           


        elif opcion_seleccionada=="3":
          print("Seleccionaste Los Más Buscados")
          correcta=1
          total_busquedas=[]
          ordenados_busquedas=[]
          contador=0
          print("\nIniciamos con los productos de mayor busqueda\n")
          for producto in lifestore_products: #for 1
            for buscar in lifestore_searches: #for 2
              if producto[0]== buscar[1]:
                contador+=1
            formato_ideal_busquedas=[producto[0], contador,producto[1]]
            total_busquedas.append(formato_ideal_busquedas)
            contador=0
          
          while total_busquedas:
            maximo=total_busquedas[0][1]
            lista_actual1=total_busquedas[0]
            for grupo in total_busquedas:
              if grupo[1]>maximo:
                maximo=grupo[1]
                lista_actual1=grupo
            ordenados_busquedas.append(lista_actual1)
            total_busquedas.remove(lista_actual1)
          print("\n Ordenados los datos: \n")

          for idx in range(0,50):
            contador+=1
            print(contador,".- ","||Busquedas: ", ordenados_busquedas[idx][1])
            print("Nombre producto: ", ordenados_busquedas[idx][2])


        elif opcion_seleccionada=="4":
          print("Seleccionaste Los menos Vendidos")
          correcta=1
          contador=0
          total_ventas=[]

          for producto in lifestore_products: #for 1
              for venta in lifestore_sales: #for 2
                if producto[0]== venta[1]:
                  contador+=1
              formato_ideal=[producto[0], contador,producto[1]]
              total_ventas.append(formato_ideal)
              contador=0

          #print("El resultado del reporte: \n Total de ventas\n")

          ordenados=[]

          while  total_ventas:
            minimo=total_ventas[0][1]
            lista_actual=total_ventas[0]
            for grupo in total_ventas:
                if grupo[1]<minimo:
                    minimo=grupo[1]
                    lista_actual=grupo
            ordenados.append(lista_actual)
            total_ventas.remove(lista_actual)
          print("\n Ordenados los datos: \n")
          for indice in range(0,50):
            contador+=1
            print(".\n",contador,".- ","|| Nombre: ",ordenados[indice][2])
           

        elif opcion_seleccionada=="5":
          print("Seleccionaste Los menos buscados")
          correcta=1
          
          total_busquedas=[]
          ordenados_busquedas=[]
          contador=0
          print("\nIniciamos con los productos de menor busqueda\n")
          for producto in lifestore_products: #for 1
            for buscar in lifestore_searches: #for 2
              if producto[0]== buscar[1]:
                contador+=1
            formato_ideal_busquedas=[producto[0], contador,producto[1]]
            total_busquedas.append(formato_ideal_busquedas)
            contador=0
          
          while total_busquedas:
            minimos=total_busquedas[0][1]
            lista_actual1=total_busquedas[0]
            for grupo in total_busquedas:
              if grupo[1]<minimos:
                minimos=grupo[1]
                lista_actual1=grupo
            ordenados_busquedas.append(lista_actual1)
            total_busquedas.remove(lista_actual1)
          print("\n Ordenados los datos: \n")

          for idx in range(0,50):
            contador+=1
            print(contador,".- ","||Busquedas: ", ordenados_busquedas[idx][1])
            print("Nombre producto: ", ordenados_busquedas[idx][2])



        elif opcion_seleccionada=="6":
          print("Seleccionaste Mejores reseñas")
          correcta=1
          contador=0
          mejores_resenas=[]
          ordenadas_resenas=[]
          suma=0
          print("\n Iniciamos con los productos de mejores Reseñas\n")

          for producto in lifestore_products: #for 1
            for mejores in lifestore_sales: #for 2
              if producto[0]== mejores[1]:
                contador+=1
                suma+=mejores[2]
            media=suma/contador
            formato_ideal_mejores_resenas=[media,producto[1],producto[0],]
            mejores_resenas.append(formato_ideal_mejores_resenas)

          #print(mejores_resenas)

          #for ind in range(0,20):
          # print("Resena",mejores_resenas[ind][1],"no:",mejores_resenas[ind][2])

          while mejores_resenas:
            mejor=mejores_resenas[0][2]
            lista_actual1=mejores_resenas[0]
            for grupo in mejores_resenas:
              if grupo[0]<mejor:
                  mejor+=grupo[2]
                  lista_actual1=grupo
                  
            ordenadas_resenas.append(lista_actual1)
            mejores_resenas.remove(lista_actual1)
          print("\n Ordenados los datos:  de las mejores reseñas\n")

          for idx in range (0,21):
            print("Nombre: ",ordenadas_resenas[idx][1])
            print("Reseña: ",ordenadas_resenas[idx][0])
          print("FIN REPORTE")


        elif opcion_seleccionada=="7":
          print("Seleccionaste Peores Reseñas")
          correcta=1
          contador=0
          #Para hacer las peores reseñas
          contador=0
          peores_resenas=[]
          ordenadas_resenas=[]
          suma=0

          print("\n Iniciamos con los productos de peores Reseñas\n")

          for producto in lifestore_products: #for 1
            for peores in lifestore_sales: #for 2
              if producto[0]== peores[1]:
                contador+=1
                suma+=peores[2]
            media=suma/contador
            formato_ideal_peores_resenas=[media,producto[1],producto[0],]
            peores_resenas.append(formato_ideal_peores_resenas)

          #print(peores_resenas)

          #for ind in range(0,20):
          # print("Resena",peores_resenas[ind][1],"no:",peores_resenas[ind][2])

          while peores_resenas:
            peor=peores_resenas[0][2]
            lista_actual1=peores_resenas[0]
            for grupo in peores_resenas:
              if grupo[0]>peor:
                  peor+=grupo[2]
                  lista_actual1=grupo
                  
            ordenadas_resenas.append(lista_actual1)
            peores_resenas.remove(lista_actual1)
          print("\n Ordenados los datos:  de las mejores reseñas\n")

          for idx in range (0,21):
            print("Nombre: ",ordenadas_resenas[idx][1])
            print("Reseña: ",ordenadas_resenas[idx][0])


        elif opcion_seleccionada=="8":
          print("Seleccionaste Reporte de totales")
          #Aqui se mostrara el total de ingresos y ventas promedio menduales, total anual y meses con mas ventas al año

        else:
          print("Opcion incorrecta")
          opcion_seleccionada= input("\nEscoge una opcion valida: ")
      break
    else:
      print("Error en el password")
      break
  if es_admin==0:
 # else:
    for usuario in usuarios_clientes:
      if usuario[0]==usuario_entrada and usuario[1]==usuario_password:
        print("Bienvenido a Lifestore Cliente " + usuario[0])
        es_admin=1
        
      else:
        print("No existe")
        es_admin=0
    
  
#en el siguiente bloque de codigo nos enfocaremos al desarrollo de otras actividades
#son solo referencias de como poder hacer algo



## while usuario_entrada and usuario_password == True:
#   print("Buen Admin1")
  

# print("cierra ciclo")


# if usuario_entrada == usuarios_administrador[1] and usuario_password==usuarios_administrador[2]:
#   print("usuario correcto"+ usuarios_administrador[1])
# else:
#   print("Error")


# agregar_usuario=input("¿Desea crear un nuevo usuario? (si/no): ")
# while agregar_usuario =="si":
#   nuevo_usuario=input("ingresa nombre: " ) 
#   nueva_password=input("Ingresa password: ")
#   usuarios_clientes.append((nuevo_usuario, nueva_password))

#   print("Usuario agregado con exito")
#   agregar_usuario=input("¿Deseas agregar otro usuario? (si/no): ")

# print(usuarios_clientes)
  

# # for producto in lifestore_products:
# #   for venta in lifestore_sales:
# #     if producto[0]== venta[1]:
# #       print("hola")


# # lista_fechas=["14/02/2020","02/05/1997","05/07/2021"]
# # lista_años=[]# lista de listas que tenga mes y año
# # listaordea=[]


# # for año in lista_fechas:
# #   lista_años.append([año[3:3], año[6:10]])
# # print(lista_años)

# # lista_ordenada= sorted(lista_años, reverse=True)

# # print(lista_ordenada)