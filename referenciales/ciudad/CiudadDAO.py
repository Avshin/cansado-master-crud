from conexion.conexion import Conexion

class ciudadDao:
    def getCiudades(self):
        query = """
                SELECT id_ciudad, detalle_ciudad
                FROM public.ciudad
        """
        lista = []
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query)
            lista_ciudad = cur.fetchall()
            if len(lista_ciudad)>0:
                for item in lista_ciudad:
                    lista.append({'id_ciudad': item[0], 'detalle_ciudad': item[1]})
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return lista




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
                values(%s)
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (descripcion,))
            con.commit()
            return True
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return False
    
    
    def deleteCiudad(self, id):
        query = """
                DELETE FROM public.ciudad
                WHERE id_ciudad=%s;
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
    # retorno falso en el caso de que haya un error al eliminar no solo muestre el error en consola sino 
    #que tambien detenga el procedimiento
    
    def updateCiudad(self, id, descripcion):
        query = """
                UPDATE public.ciudad
                SET  detalle_ciudad=%s
                WHERE id_ciudad=%s;
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (descripcion, id,))
            con.commit()
            return True
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return False
    
    