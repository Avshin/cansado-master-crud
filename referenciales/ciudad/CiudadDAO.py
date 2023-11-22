from conexion.conexion import Conexion

class ciudadDao:
    def getCiudades(self):
        query = """
                SELECT id_ciudad, detalle_ciudad
                FROM public.ciudad
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e:
            print(f"pgcode = {e.pgcode}, mensaje ={e.pgerror}")
        finally:
            cur.close()
            con.close()


    def getCiudadesById(self, id):
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




    def insertCiudad(self, descripcion):
        query = """
                insert into public.ciudad (detalle_ciudad)
                values=(%s)
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (id,))
            con.commit()
            return True
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return False