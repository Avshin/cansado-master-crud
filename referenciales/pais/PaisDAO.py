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
    
    
    
    def insertPais(self, descripcion):
        query = """
                insert into public.pais (detalle_pais)
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
    
    
    
    def deletePais(self, id):
        query = """
                DELETE FROM public.pais
                WHERE id_pais=%s;
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


    def updatePais(self, id, descripcion):
        query = """
                UPDATE public.pais
                SET  detalle_pais=%s
                WHERE id_pais=%s;
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

    def getPaisById(self, id):
        query = """
                select id_pais, detalle_pais
                from public.pais where id_pais=%s
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (id,))
            pais = cur.fetchone()
            if pais:
                return{'id_pais': pais[0], 'detalle_pais': pais[1]}
            return None
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()