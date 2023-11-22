from conexion.conexion import Conexion
class ciudadDao:
    def getCiudades(self):
        query = """
                select id_ciudad, detalle_ciudad
                from public.ciudad
        """
        lista = []
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query)
            tuplas_ciudades = cur.fetchall()
            if len(tuplas_ciudades)>0:
                for item in tuplas_ciudades:
                    lista.append({'id_ciudad': item[0], 'detalle_ciudad': item[1]})
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return lista
    
    
    def getCiudadesById(self):
        query = """
                select id_ciudad, detalle_ciudad
                from public.ciudad where id_ciudad=%s
        """
        
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (id,))
            ciudad = cur.fetchone()
            if ciudad:
                return{'id_ciudad': ciudad[0], 'detalle_ciudad': ciudad[1]}
            return None
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
