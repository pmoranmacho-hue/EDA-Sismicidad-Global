import pandas as pd


def tipificar_variables(df):
    """
    Clasifica automáticamente las columnas de un DataFrame según su cardinalidad.

    Criterios:
    - Binaria:           exactamente 2 valores únicos
    - Numérica Continua: más del 30% de valores únicos respecto al total
    - Numérica Discreta: más de 10 valores únicos (sin llegar al 30%)
    - Categórica:        10 o menos valores únicos

    Parámetros:
    - df: DataFrame de pandas

    Retorna:
    - DataFrame con columnas: Card, %_Card, Tipo, Clasificada_como
    """
    df_tip = pd.DataFrame([
        df.nunique(),
        df.nunique() / len(df) * 100,
        df.dtypes
    ]).T.rename(columns={0: "Card", 1: "%_Card", 2: "Tipo"})

    df_tip["Clasificada_como"] = "Categorica"
    df_tip.loc[df_tip["Card"] == 2,      "Clasificada_como"] = "Binaria"
    df_tip.loc[df_tip["Card"] > 10,      "Clasificada_como"] = "Numerica Discreta"
    df_tip.loc[df_tip["%_Card"] > 30,    "Clasificada_como"] = "Numerica Continua"

    return df_tip
