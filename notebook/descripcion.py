import pandas as pd
from utils.simulacion import generar_simulacion
from notebook.limpieza import limpiar_datos

def main():
    print("GENERANDO DATOS...")
    data = generar_simulacion(10)
    df = pd.DataFrame(data)

    print("\n=== DATOS ORIGINALES ===")
    print(df)

    print("\nLIMPIANDO DATOS...")
    df_limpio = limpiar_datos(df)

    print("\n=== DATOS LIMPIOS ===")
    print(df_limpio)

if __name__ == "__main__":
    main()