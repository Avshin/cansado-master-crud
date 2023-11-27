from conexion.conexion import Conexion
class personasDAO:
    def getPersonas(self):
        sql = """
        SELECT id_persona, cin_persona, nombre_persona, apellido_persona, fechanac_persona, 
        direcc_persona, tel_persona, id_ciudad, detalle_ciudad, id_pais,detalle_pais 
        FROM public.personas
        left join ciudad using (id_ciudad)
        left join pais using (id_pais)
        """
        lista=[]
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sql)
            tuplas_personas = cur.fetchall()
            if len(tuplas_personas)>0:
                for item in tuplas_personas:
                    lista.append({
                        'id_persona': item[0],
                        'cin_persona': item[1],
                        'nombre_persona': item[2],
                        'apellido_persona': item[3],
                        'fechanac_persona': item[4],
                        'direcc_persona': item[5],
                        'tel_persona': item[6],
                        'detalle_ciudad': item[8],
                        'detalle_pais': item[10]
                    })
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return lista
    
    
    def selectById(self):
        sql = """
             
             SELECT id_persona, cin_persona, nombre_persona, apellido_persona, fechanac_persona, 
        direcc_persona, tel_persona, id_ciudad, detalle_ciudad, id_pais,detalle_pais 
        FROM public.personas
        left join ciudad using (id_ciudad)
        left join pais using (id_pais)
        where id_persona = %s
            """
        lista=[]
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sql, (id))
            persona = cur.fetchone()
            if persona:
                return{
                        'id_persona': persona[0],
                        'cin_persona': persona[1],
                        'nombre_persona': persona[2],
                        'apellido_persona': persona[3],
                        'fechanac_persona': persona[4],
                        'direcc_persona': persona[5],
                        'tel_persona': persona[6],
                        'detalle_ciudad': persona[8],
                        'detalle_pais': persona[10]
                    }
            return None
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
            
            
    def insertPersonas(self, cedula, nombre, apellido, fecha, direccion, telefono, ciudad, pais):
        query = """
                INSERT INTO public.personas(
            id_persona, cin_persona, nombre_persona, apellido_persona, fechanac_persona,
            direcc_persona, tel_persona, id_ciudad, id_pais)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        conexion=Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query, (cedula, nombre, apellido, fecha, direccion, telefono, ciudad, pais,))
            con.commit()
            return True
        except con.Error as e:
            print(f"codigo de error: {e.pgcode}, mensaje: {e.pgerror}")
        finally:
            cur.close()
            con.close()
        return False