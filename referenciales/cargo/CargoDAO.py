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


    def getCargosById(self, id):
        query = """
                select id_cargo, detalle_cargo
                from public.cargos where id_cargo=%s
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (id,))
            cargo = cur.fetchone()
            if cargo:
                return{'id_cargo': cargo[0], 'detalle_cargo': cargo[1]}
            return None
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()



    def insertCargos(self, descripcion):
        query = """
                insert into public.cargos (detalle_cargo)
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



    def deleteCargo(self, id):
        query = """
                DELETE FROM public.cargos
                WHERE id_cargo=%s;
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



    def updateCargos(self, id, descripcion):
        query = """
                UPDATE public.cargos
                SET  detalle_cargo=%s
                WHERE id_cargo=%s;
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