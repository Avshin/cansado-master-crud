from conexion.conexion import Conexion
class paisDao:
    def getPaises(self):
        sql = """
        select id_pais, detalle_pais from public.pais
        """
        lista = []
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sql)
            tuplas_paises=cur.fetchall()
            if len(tuplas_paises)>0:
                for item in tuplas_paises:
                    lista.append({'id_pais':item[0], 'detalle_pais': item[1]})
        except con.Error as e:
            print(f"error codigo:{e.pgcode}, mensaje{e.pgerror}")
        finally:
            cur.close()
            con.close()
        return lista