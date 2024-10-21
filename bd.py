import pymysql

def obtener_conexion():
    return pymysql.connect(
        host="127.0.0.1",      
        user="root",         
        password="",           
        db="smi_mx",  
        port=3306,            
        charset='utf8mb4',    
        cursorclass=pymysql.cursors.DictCursor  
    )