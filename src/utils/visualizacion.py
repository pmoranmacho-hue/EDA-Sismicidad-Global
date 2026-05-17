import matplotlib.pyplot as plt
import seaborn as sns


def pinta_distribucion_categoricas(df, columnas_categoricas, relativa=False, mostrar_valores=False):
    """
    Pinta barplots para una lista de variables categóricas.

    Parámetros:
    - df: DataFrame de pandas
    - columnas_categoricas: lista de nombres de columnas a visualizar
    - relativa: si True, muestra frecuencia relativa (porcentaje); si False, frecuencia absoluta
    - mostrar_valores: si True, anota el valor numérico encima de cada barra
    """
    num_columnas = len(columnas_categoricas)
    num_filas = (num_columnas // 2) + (num_columnas % 2)

    fig, axes = plt.subplots(num_filas, 2, figsize=(15, 5 * num_filas))
    axes = axes.flatten()

    for i, col in enumerate(columnas_categoricas):
        ax = axes[i]
        if relativa:
            total = df[col].value_counts().sum()
            serie = df[col].value_counts().apply(lambda x: x / total)
            sns.barplot(x=serie.index, y=serie, ax=ax, palette='viridis',
                        hue=serie.index, legend=False)
            ax.set_ylabel('Frecuencia Relativa')
        else:
            serie = df[col].value_counts()
            sns.barplot(x=serie.index, y=serie, ax=ax, palette='viridis',
                        hue=serie.index, legend=False)
            ax.set_ylabel('Frecuencia')

        ax.set_title(f'Distribución de {col}')
        ax.set_xlabel('')
        ax.tick_params(axis='x', rotation=45)

        if mostrar_valores:
            for p in ax.patches:
                height = p.get_height()
                ax.annotate(f'{height:.2f}',
                            (p.get_x() + p.get_width() / 2., height),
                            ha='center', va='center',
                            xytext=(0, 9), textcoords='offset points')

    for j in range(i + 1, num_filas * 2):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


def plot_multiple_boxplots(df, columns, dim_matriz_visual=2):
    """
    Pinta boxplots individuales para una lista de columnas numéricas.

    Parámetros:
    - df: DataFrame de pandas
    - columns: lista de nombres de columnas numéricas
    - dim_matriz_visual: número de columnas en la cuadrícula de gráficos (por defecto 2)
    """
    num_cols = len(columns)
    num_rows = num_cols // dim_matriz_visual + num_cols % dim_matriz_visual
    fig, axes = plt.subplots(num_rows, dim_matriz_visual, figsize=(12, 6 * num_rows))
    axes = axes.flatten()

    for i, column in enumerate(columns):
        if df[column].dtype in ['int64', 'float64']:
            sns.boxplot(data=df, x=column, ax=axes[i])
            axes[i].set_title(column)

    for j in range(i + 1, num_rows * 2):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


def plot_boxplot_grouped(df, column_to_plot, group_column):
    """
    Pinta un boxplot de una variable numérica agrupada por una variable categórica.

    Parámetros:
    - df: DataFrame de pandas
    - column_to_plot: nombre de la columna numérica (eje Y)
    - group_column: nombre de la columna categórica para agrupar (eje X)
    """
    if (df[column_to_plot].dtype in ['int64', 'float64'] and
            df[group_column].dtype in ['object', 'category']):
        sns.boxplot(data=df, x=group_column, y=column_to_plot)
        plt.show()
