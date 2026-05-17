# 🌍 Análisis Exploratorio de Datos — Sismicidad Global 2000-2025

## Descripción 

Análisis exploratorio (EDA) de la actividad sísmica global registrada entre 2000 y 2025,
realizado como proyecto final del módulo de Análisis de Datos.

El objetivo es identificar patrones en la frecuencia, intensidad y distribución geográfica
de los terremotos de magnitud ≥ 5.0 en la escala Richter.

---

## Hipótesis planteadas

| # | Hipótesis | Resultado |
|---|-----------|-----------|
| H1 | Los terremotos profundos (>300 km) tienen menor magnitud que los superficiales (<70 km) | ❌ Refutada |
| H2 | La frecuencia anual de terremotos no muestra tendencia creciente entre 2000 y 2025 | ✅ Confirmada |
| H3 | Más del 70% de los terremotos ≥6.0 ocurren en el Cinturón de Fuego del Pacífico | ✅ Confirmada |
| H4 | La distribución mensual de terremotos ≥6.0 es uniforme a lo largo del año | ⚠️ Refutada formalmente (diferencias débiles) |

---

## Tecnologías utilizadas

- Python 
- pandas · numpy
- matplotlib · seaborn
- scipy

---

## Estructura del repositorio
EDA-SISMICIDAD-GLOBAL/
├── src/
│   ├── data/
│   │   └── global_natural_disasters_2000_2025.csv
│   ├── img/
│   ├── notebooks/
│   │   ├── Notebook-Análisis univariante.ipynb
│   │   ├── Notebook-Análisis finales.ipynb
│   │   └── Notebook-tratamiento-datos.ipynb
│   └── utils/
├── main.ipynb
├── Memoria.pdf
├── Presentacion.pdf
└── README.md

---

## Instrucciones de reproducción

1. Clona el repositorio:
```bash
   git clone https://github.com/usuario/EDA-SISMICIDAD-GLOBAL.git
```

2. Instala las dependencias:
```bash
   pip install pandas numpy matplotlib seaborn scipy
```

3. Abre el notebook principal:
```bash
   jupyter notebook main.ipynb
```

> El CSV ya está incluido en `src/data/`. No es necesario descargarlo por separado.

---

## Principales conclusiones

- **La magnitud no depende de la profundidad.** La correlación entre ambas variables es prácticamente nula (r=−0.054).
- **La frecuencia sísmica es estable.** No existe tendencia creciente en el período analizado. La media anual es de ~1.785 terremotos.
- **El Cinturón de Fuego domina la sismicidad global.** El 82.3% de los terremotos ≥6.0 ocurren en esta región, superando el umbral planteado en +12.3 puntos porcentuales.
- **La estacionalidad existe, pero es débil.** El test Chi² detecta diferencias significativas (p=0.0017), pero el coeficiente de variación mensual es de solo el 9.2%.

---

## Autores

| Nombre | GitHub | LinkedIn |
|--------|--------|----------|
| Pablo Morán | [@pablo](https://github.com/pmoranmacho-hue) | [LinkedIn](https://linkedin.com/in/pablo-morán-macho-75727a9b/) |
| Ana Belén Escobar | [@anabelen](https://github.com/Abem-ds) | [LinkedIn](www.linkedin.com/in/ana-belén-escobar-b9831a3a2) |

Mayo 2026
