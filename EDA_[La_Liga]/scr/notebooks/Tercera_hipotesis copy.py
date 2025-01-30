# analisis_goles_tiempos.py
import matplotlib.pyplot as plt
import seaborn as sns

def analizar_goles_tiempos(df):
    """
    Analiza dónde se hacen más goles: en el primer o segundo tiempo.

    :param df: pd.DataFrame con los datos de los partidos.
    """
    if df is None:
        print("El DataFrame no está definido.")
        return

    # Calcular los goles en el segundo tiempo
    df['Goles_2T_Local'] = df['FTHG'] - df['HTHG']
    df['Goles_2T_Visitante'] = df['FTAG'] - df['HTAG']

    # Calcular los totales de goles por tiempo
    goles_1T = df['HTHG'].sum() + df['HTAG'].sum()
    goles_2T = df['Goles_2T_Local'].sum() + df['Goles_2T_Visitante'].sum()

    # Crear el gráfico comparativo
    plt.figure(figsize=(8, 5))
    barras = sns.barplot(
        x=['Primer Tiempo', 'Segundo Tiempo'], 
        y=[goles_1T, goles_2T], 
        palette="coolwarm"
    )

    # Añadir etiquetas con los números de goles en cada barra
    for barra, valor in zip(barras.patches, [goles_1T, goles_2T]):
        # Colocamos el texto justo encima de la barra
        x = barra.get_x() + barra.get_width() / 2  # Posición X
        y = valor  # Altura de la barra (valor Y)
        plt.text(x, y + 5, f'{int(valor)}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Configuración del gráfico
    plt.title("Comparativa de goles entre primer y segundo tiempo")
    plt.ylabel("Cantidad de goles")
    plt.xlabel("Tiempos")
    plt.show()


