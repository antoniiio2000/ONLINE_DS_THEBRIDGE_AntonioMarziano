# main.py
from proyecto_eda.Cargar_datos import cargar_datos
from proyecto_eda.Primera_hipotesis import analizar_casa_vs_fuera
from proyecto_eda.Segunda_hipotesis import analizar_cambio_resultado
from proyecto_eda.Tercera_hipotesis import analizar_goles_tiempos
from proyecto_eda.Cuarta_hipotesis import analizar_mantener_victoria

# Ruta al archivo CSV
ruta_csv = "/Users/dayanapetrova/Desktop/myenv2/proyecto_eda/LaLiga_Matches.csv"

# Cargar los datos
df = cargar_datos(ruta_csv)

# Ejecutar los análisis
analizar_casa_vs_fuera(df)
analizar_cambio_resultado(df)
analizar_goles_tiempos(df)
analizar_mantener_victoria(df)
