# analisis_mantener_victoria.py
import matplotlib.pyplot as plt
import seaborn as sns

def analizar_mantener_victoria(df):
    """
    Analiza los equipos que más mantienen la victoria.

    :param df: pd.DataFrame con los datos de los partidos.
    """
    if df is None:
        print("El DataFrame no está definido.")
        return

    # Filtrar partidos donde el equipo mantiene la victoria
    locales_que_mantienen = df[(df['HTR'] == 'H') & (df['FTR'] == 'H')]['HomeTeam'].value_counts()
    visitantes_que_mantienen = df[(df['HTR'] == 'A') & (df['FTR'] == 'A')]['AwayTeam'].value_counts()

    # Sumar los resultados de locales y visitantes
    total_que_mantienen = (locales_que_mantienen + visitantes_que_mantienen).fillna(0).sort_values(ascending=False)
    top_3_equipos = total_que_mantienen.head(3)

    # Crear el gráfico
    plt.figure(figsize=(8, 5))
    barras = sns.barplot(x=top_3_equipos.index, y=top_3_equipos.values, palette="magma")

    # Añadir etiquetas dentro de las barras, en la parte superior
    for barra, valor in zip(barras.patches, top_3_equipos.values):
        # Coordenadas para colocar el texto
        x = barra.get_x() + barra.get_width() / 2  # Centro de la barra
        y = barra.get_height()  # Altura de la barra
        plt.text(x, y - 20, f'{int(valor)}', ha='center', va='bottom', fontsize=12, color='white', fontweight='bold')

    # Configuración del eje Y y del gráfico
    plt.title("Top 3 equipos que más mantienen la victoria", fontsize=14)
    plt.ylabel("Partidos sin remontada", fontsize=12)
    plt.xlabel("Equipos", fontsize=12)
    plt.yticks(range(0, 501, 100))  # Escala del eje Y de 0 a 500 en pasos de 100
    plt.ylim(0, 500)  # Límite superior del eje Y
    plt.show()

    # Imprimir los resultados en la consola
    print("Top 3 equipos que más mantienen la victoria:")
    print(top_3_equipos)


