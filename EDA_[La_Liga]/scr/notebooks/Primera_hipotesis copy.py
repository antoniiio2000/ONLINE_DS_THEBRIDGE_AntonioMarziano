import matplotlib.pyplot as plt
import seaborn as sns

def analizar_casa_vs_fuera(df):
    """
    Analiza la influencia de jugar en casa o fuera en los resultados.

    :param df: pd.DataFrame con los datos de los partidos.
    """
    if df is None:
        print("El DataFrame no está definido.")
        return

    resultados = df['FTR'].value_counts()
    total_partidos = len(df)
    porcentajes = (resultados / total_partidos) * 100

    # Gráfico de barras
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=porcentajes.index, y=porcentajes.values, palette="viridis")
    plt.title("Influencia de jugar en casa (FTR)")
    plt.xlabel("Resultado (H = Local, D = Empate, A = Visitante)")
    plt.ylabel("Porcentaje (%)")

    # Añadir los porcentajes en cada barra
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2., height + 1,  # Añadir el texto un poco por encima de la barra
                f'{height:.2f}%', 
                ha='center', va='bottom',  # Alineación horizontal y vertical
                fontsize=12, color='black', fontweight='bold')

    plt.show()

    # Promedio de goles
    promedio_local = df['FTHG'].mean()
    promedio_visitante = df['FTAG'].mean()

    print(f"Promedio de goles Local: {promedio_local:.2f}")
    print(f"Promedio de goles Visitante: {promedio_visitante:.2f}")
