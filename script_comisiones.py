import pandas as pd
import psycopg2
import os

# Leer CSV
df = pd.read_csv("data/ComisionEmpleados_V1_202605.csv", sep=";")

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host="mgg.vps.webdock.cloud",
    port=5432,
    database="dmc",
    user="usr_ro_dmc_rrhh_estudiantes",
    password="fZp!jHt0j6%89^B4I*L*29bz4b^"
)

# Traer datos empleados
empleados = pd.read_sql(
    "SELECT empleado_id, nom_empleado, ape_empleado, cod_cargo, cod_departamento FROM rrhh.Empleado;",
    conn
)

# Merge con comisiones
resultado = df.merge(empleados, on="empleado_id", how="left")

output_path = "/app/output/resultado_comisiones.xlsx"
resultado.to_excel(output_path, index=False)
os.chmod(output_path, 0o644)
