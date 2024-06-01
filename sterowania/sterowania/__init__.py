#Le permite a django funcionar sin problemas con pyMySQL como controlador de mysql
#Se agrego esto para permitir la conexion con mysql ya que django tiene su propia base de datos Sqlite, pero se utilizo mysqls
import pymysql
 
pymysql.install_as_MySQLdb()