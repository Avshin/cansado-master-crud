from conexion.conexion import Conexion
class CargosDao:
    def getCargos(self):
        sql = """
        SELECT id_cargo, detalle_cargo
        FROM public.cargos
        """
        lista=[]
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sql)
            tuplas_cargos = cur.fetchall()
            if len(tuplas_cargos)>0:
                for item in tuplas_cargos:
                    lista.append({'id_cargo': item[0], 'detalle_cargo': item[1]})
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return lista