import pymysql

def obtener_conexion():
    return pymysql.connect(
        host="127.0.0.1",      
        user="root",         
        password="",           
        db="init",  
        port=3305,            
        charset='utf8mb4',    
        cursorclass=pymysql.cursors.DictCursor  
    )