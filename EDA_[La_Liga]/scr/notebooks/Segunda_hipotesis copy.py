# analisis_cambio_resultado.py
import matplotlib.pyplot as plt

def analizar_cambio_resultado(df):
    """
    Analiza los cambios de resultado entre el primer y segundo tiempo.

    :param df: pd.DataFrame con los datos de los partidos.
    """
    if df is None:
        print("El DataFrame no está definido.")
        return

    # Creamos la columna para detectar cambios
    df['CambioResultado'] = df.apply(lambda row: row['HTR'] != row['FTR'], axis=1)
    
    # Contamos los cambios
    cambios = df['CambioResultado'].value_counts()

    # Extraemos los valores para análisis
    total_partidos = len(df)
    cambia = cambios.get(True, 0)  # Número de partidos donde cambia el resultado
    no_cambia = cambios.get(False, 0)  # Número de partidos donde no cambia el resultado

    # Calculamos porcentajes
    porcentaje_cambia = (cambia / total_partidos) * 100
    porcentaje_no_cambia = (no_cambia / total_partidos) * 100

    # Mostramos los porcentajes
    print(f"Total de partidos analizados: {total_partidos}")
    print(f"Porcentaje de partidos que cambian de resultado: {porcentaje_cambia:.2f}%")
    print(f"Porcentaje de partidos que no cambian de resultado: {porcentaje_no_cambia:.2f}%")
    
    # Interpretamos el resultado
    if porcentaje_cambia > 50:
        print("Conclusión: Más de la mitad de los partidos cambian de resultado entre el primer y segundo tiempo.")
    elif porcentaje_cambia > 30:
        print("Conclusión: Una cantidad significativa de partidos (más del 30%) cambian de resultado.")
    else:
        print("Conclusión: La mayoría de los partidos no cambian de resultado entre el primer y segundo tiempo.")

    # Gráfico de pastel
    plt.figure(figsize=(6, 6))
    plt.pie(
        cambios, 
        labels=['No Cambia', 'Cambia'], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=["#66c2a5", "#fc8d62"]
    )
    plt.title("Cambios de resultado entre la primera y segunda parte")
    plt.show()

