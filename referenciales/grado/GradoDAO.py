from conexion.conexion import Conexion
class GradoDao:
    def getGrado(self):
        sql = """
        SELECT id_gacademico, detalle_gacademico
        FROM public.grados_academicos
        """
        lista=[]
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sql)
            tuplas_grado = cur.fetchall()
            if len(tuplas_grado)>0:
                for item in tuplas_grado:
                    lista.append({'id_gacademico': item[0], 'detalle_gacademico': item[1]})
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return lista