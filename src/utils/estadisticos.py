def resumen_estadisticos(df, columnas):
    """
    Devuelve una tabla de estadísticos descriptivos con nombres en castellano.

    Incluye: Registros, Media, Mediana, Desv. Típica, Mínimo, Q1, Q3 y Máximo.

    Parámetros:
    - df: DataFrame de pandas
    - columnas: lista de nombres de columnas numéricas a resumir

    Retorna:
    - DataFrame con los estadísticos como filas y las columnas como columnas
    """
    return df[columnas].agg([
        'count',
        'mean',
        'median',
        'std',
        'min',
        lambda x: x.quantile(0.25),
        lambda x: x.quantile(0.75),
        'max'
    ]).rename(index={
        'count':       'Registros',
        'mean':        'Media',
        'median':      'Mediana',
        'std':         'Desv. Típica',
        'min':         'Mínimo',
        '<lambda_0>':  'Q1 (25%)',
        '<lambda_1>':  'Q3 (75%)',
        'max':         'Máximo'
    }).round(3)
