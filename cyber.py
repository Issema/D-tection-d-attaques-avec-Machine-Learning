import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Charge le fichier (remplace le nom si besoin)
df = pd.read_csv('KDDTrain.csv', header=None)

print("Taille du jeu de données :", df.shape)  # Exemple attendu : (125973, 43)
print("Aperçu des 5 premières lignes :")
print(df.head())

print("\nNombre de connexions par étiquette :")
print(df[41].value_counts())  # la colonne 41 contient "normal" et le type d’attaque
# Noms des colonnes
columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root',
    'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
    'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

df.columns = columns

# On affiche pour vérification
print(df.head())

# Encodage de protocol_type, service, flag
for col in ['protocol_type', 'service', 'flag']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Option : encoder le label (normal vs attaque)
df['label_binary'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

print(df[['label', 'label_binary']].value_counts().head(10))

# Features = tout sauf les colonnes inutiles
X = df.drop(columns=['label', 'label_binary'])  
y = df['label_binary']

# Séparation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Taille de l'entraînement :", X_train.shape)
print("Taille du test :", X_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Créer le modèle
model = RandomForestClassifier(random_state=42)

# Entraîner le modèle
model.fit(X_train, y_train)

# Prédire sur le test
y_pred = model.predict(X_test)

# Évaluation
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
