import pandas as pd

def limpiar_datos(df):
    """
    Limpia y valida un dataframe de productos.
    
    Parámetros:
    -----------
    df : pd.DataFrame
        Dataframe con columnas: producto, categoria, id, costo, stock
    
    Retorna:
    --------
    pd.DataFrame
        Dataframe limpio y filtrado
    """
    # Validar que existan las columnas requeridas
    columnas_requeridas = ["producto", "categoria", "id", "costo", "stock"]
    columnas_faltantes = [col for col in columnas_requeridas if col not in df.columns]
    
    if columnas_faltantes:
        raise ValueError(f"Columnas faltantes: {columnas_faltantes}")
    
    df = df.copy()

    # Limpiar datos de texto
    df["producto"] = df["producto"].str.lower().str.strip()
    df["categoria"] = df["categoria"].str.lower().str.strip()

    # Convertir a numérico y eliminar valores inválidos (NaN)
    df["id"] = pd.to_numeric(df["id"], errors="coerce")
    df["costo"] = pd.to_numeric(df["costo"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")
    
    # Eliminar filas con valores NaN en columnas numéricas
    df = df.dropna(subset=["id", "costo", "stock"])

    # Filtrar por condiciones
    df = df[df["costo"] > 20000]
    df = df[df["stock"] >= 0]

    return df


# Ejemplo de uso
if __name__ == "__main__":
    # Crear datos de prueba
    datos = {
        "producto": ["LAPTOP", "Mouse", "TECLADO", "Monitor"],
        "categoria": ["ELECTRÓNICA", "accesorios", "ACCESORIOS", "electrónica"],
        "id": [1, 2, 3, 4],
        "costo": [50000, 15000, 25000, 35000],
        "stock": [5, -2, 10, 0]
    }
    
    df = pd.DataFrame(datos)
    
    print("=" * 50)
    print("DATOS ORIGINALES:")
    print("=" * 50)
    print(df)
    print("\n" + "=" * 50)
    print("DATOS DESPUÉS DE LIMPIAR:")
    print("=" * 50)
    df_limpio = limpiar_datos(df)
    print(df_limpio)
    print("\n" + "=" * 50)
    print(f"Filas procesadas: {len(df)} → {len(df_limpio)}")
    print("=" * 50)
