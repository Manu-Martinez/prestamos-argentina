import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset con codificación UTF-8
df = pd.read_csv('clientes_ficticios_abril2025.csv', encoding='utf-8')

# Preprocesamiento
# Codificar la variable categórica 'Tipo_Empleo', sin eliminar la primera categoría
df_encoded = pd.get_dummies(df, columns=['Tipo_Empleo'], drop_first=False)

# Imprimir las columnas generadas para depuración
print("Columnas después de pd.get_dummies():", df_encoded.columns.tolist())

# Definir variables predictoras (excluir ID_Cliente y las columnas objetivo)
# Ajustamos los nombres de las columnas dummy según los valores de Tipo_Empleo
features = ['Edad', 'Ingresos_Mensuales', 'Años_Empleo', 'Puntuacion_Crediticia', 
            'Deuda_Actual', 'Monto_Prestamo_Solicitado', 'Ratio_Deuda_Ingresos',
            'Tipo_Empleo_Formal', 'Tipo_Empleo_Informal', 'Tipo_Empleo_Autónomo', 'Tipo_Empleo_Desempleado']
X = df_encoded[features]

# Escalar las variables numéricas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Definir las columnas objetivo
targets = ['Apto_Prestamo_Pequeño', 'Apto_Prestamo_Mediano', 'Apto_Prestamo_Elevado']

# Lista para almacenar los datos de importancia de características
feature_importance_data = []

# Diccionario para almacenar resultados
results = {}

# Iterar sobre cada tipo de préstamo
for target in targets:
    print(f"\nModelando para: {target}")
    y = df_encoded[target]
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Entrenar el modelo Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Predecir en el conjunto de prueba
    y_pred = rf_model.predict(X_test)
    
    # Evaluar el modelo
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    # Guardar resultados
    results[target] = {
        'accuracy': accuracy,
        'f1_score': f1,
        'confusion_matrix': cm,
        'model': rf_model
    }
    
    # Imprimir métricas
    print(f"Precisión: {accuracy:.2f}")
    print(f"F1-Score: {f1:.2f}")
    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred, target_names=['No Apto', 'Apto']))
    
	# Reemplazar guiones bajos por espacios en el nombre del target para títulos y archivos
    target_clean = target.replace('_', ' ')
    
    # Graficar la matriz de confusión
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Apto', 'Apto'], yticklabels=['No Apto', 'Apto'])
    plt.title(f'Matriz de Confusión {target_clean}')
    plt.xlabel('Predicción')
    plt.ylabel('Real')
    plt.savefig(f'confusion_matrix {target.lower().replace("_", " ")}.png')
    plt.show()
    
    # Importancia de las características
    feature_importance = pd.DataFrame({
        'Feature': features,
        'Importance': rf_model.feature_importances_
    }).sort_values(by='Importance', ascending=False)
    
	# Abreviar etiquetas largas, traducir a español y reemplazar guiones bajos por espacios
    feature_importance['Feature'] = feature_importance['Feature'].replace({
        'Ingresos_Mensuales': 'Ingresos Mensuales',
        'Monto_Prestamo_Solicitado': 'Monto Prestamo Solicitado',
        'Puntuacion_Crediticia': 'Puntuación Crediticia',
        'Ratio_Deuda_Ingresos': 'Ratio Deuda Ingresos',
        'Tipo_Empleo_Formal': 'Empleo Formal',
        'Tipo_Empleo_Informal': 'Empleo Informal',
        'Tipo_Empleo_Autónomo': 'Empleo Autónomo',
        'Tipo_Empleo_Desempleado': 'Empleo Desempleado',
        'Edad': 'Edad',
        'Años_Empleo': 'Años Empleo',
        'Deuda_Actual': 'Deuda Actual'
    })
    
	# Renombrar columnas del DataFrame a español
    feature_importance = feature_importance.rename(columns={
        'Feature': 'Característica',
        'Importance': 'Importancia'
    })
    
	# Añadir los datos de importancia a la lista con el tipo de préstamo
    for _, row in feature_importance.iterrows():
        feature_importance_data.append({
            'Tipo_Prestamo': target_clean.split(' ')[-1],  # Extraer "Pequeño", "Mediano", "Elevado"
            'Caracteristica': row['Característica'],
            'Importancia': row['Importancia']
        })
    
    # Graficar la importancia de las características con etiquetas en español
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Importancia', y='Característica', data=feature_importance)
    plt.title(f'Importancia de las Características {target_clean}')
    plt.xlabel('Importancia')
    plt.ylabel('Características')
    plt.yticks(fontsize=8)
    plt.subplots_adjust(left=0.25)
    plt.savefig(f'feature_importance {target.lower().replace("_", " ")}.png', bbox_inches='tight')
    plt.show()

# Resumen de métricas
print("\nResumen de métricas:")
for target, metrics in results.items():
    print(f"{target}: Precisión = {metrics['accuracy']:.2f}, F1-Score = {metrics['f1_score']:.2f}")
    
# Exportar los datos de importancia a un CSV
feature_importance_df = pd.DataFrame(feature_importance_data)
feature_importance_df.to_csv('feature_importance.csv', index=False, encoding='utf-8')
print("\nDatos de importancia exportados a 'feature_importance.csv'")