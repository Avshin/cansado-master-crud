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
    
    
    def insertGrado(self, descripcion):
        query = """
                insert into public.grados_academicos (detalle_gacademico)
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
    
    
    
    def deleteGrado(self, id):
        query = """
                DELETE FROM public.grados_academicos
                WHERE id_gacademico=%s;
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
    
    def getGradoById(self, id):
        query = """
                select id_gacademico, detalle_gacademico
                from public.grados_academicos where id_gacademico=%s
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (id,))
            grado = cur.fetchone()
            if grado:
                return{'id_gacademico': grado[0], 'detalle_gacademico': grado[1]}
            return None
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
            
            
            
            
    def updateGrado(self, id, descripcion):
        query = """
                UPDATE public.grados_academicos
                SET  detalle_gacademico=%s
                WHERE id_gacademico=%s;
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