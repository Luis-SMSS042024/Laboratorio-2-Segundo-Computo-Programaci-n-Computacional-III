import pandas as pd

# 1. Cargar dataset (ajusta el nombre al tuyo)
df = pd.read_csv("netflix_titles.csv")

# 2. Resumen estadístico
print("=== DESCRIBE ===")
print(df.describe(include='all'))  # incluye categóricas y numéricas

# 3. Tipos de datos
print("\n=== DTYPES ===")
print(df.dtypes)

# 4. Primeros y últimos registros
print("\n=== HEAD ===")
print(df.head())
print("\n=== TAIL ===")
print(df.tail())

# 5. Ordenar por release_year (películas más recientes primero)
print("\n=== ORDENADO POR release_year ===")
print(df.sort_values("release_year", ascending=False).head(10))

# 6. Medidas estadísticas sobre columna numérica (release_year)
print("\n=== MEDIDAS release_year ===")
print("Media:", df["release_year"].mean())
print("Mediana:", df["release_year"].median())
print("Desviación estándar:", df["release_year"].std())
