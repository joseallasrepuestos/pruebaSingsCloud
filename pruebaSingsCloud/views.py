
from django.http import HttpResponse
import MySQLdb 

datos = ["127.0.0.1", "root", "123456", "prueba"] 
con = MySQLdb.connect(*datos)


def saludo(request): #vista
    return HttpResponse("hola alumnos.")

    
def ft_get_stores(request):
    cursor = con.cursor()
    cursor.execute("SELECT `ft_get_stores`()")
    data = cursor.fetchall()
    return HttpResponse(data)

def ft_get_deals(request):
    cursor = con.cursor()
    cursor.execute("SELECT `ft_get_deals`('1')")
    data = cursor.fetchall()
    cursor.close() 
    return HttpResponse(data)

def ft_get_brands(request):
    cursor = con.cursor()
    cursor.execute("SELECT `ft_get_brands`()")
    data = cursor.fetchall()
    cursor.close() 
    return HttpResponse(data)

def ft_proc_inst_store_users(request):
    cursor = con.cursor()
    cursor.execute("CALL `ft_proc_inst_store_users`('1', '1')")
    data = cursor.fetchall()
    cursor.close() 
    return HttpResponse(data)

def ft_get_users_suscrip_store(request):
    cursor = con.cursor()
    cursor.execute("SELECT `ft_get_users_suscrip_store`('1')")
    data = cursor.fetchall()
    cursor.close() 
    return HttpResponse(data)



