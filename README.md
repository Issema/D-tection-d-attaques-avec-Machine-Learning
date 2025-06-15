# 🔐 Détection d’Intrusions Réseau avec Machine Learning

## 📌 Contexte

Dans un contexte de cybersécurité, notamment pour les institutions financières et les grandes entreprises, la détection des intrusions réseau est cruciale.  
Ce projet a pour but de créer un modèle de machine learning capable de **détecter automatiquement les attaques réseau**, en s'appuyant sur le célèbre dataset **NSL-KDD**, dérivé de KDD'99.

---

## ⚙️ Description du Projet

Ce projet s'appuie sur un modèle de **Random Forest** entraîné pour distinguer le trafic réseau normal des comportements malveillants.  
L’objectif est de **prédire si une connexion est une attaque ou non** à partir de ses caractéristiques réseau (protocole, service, taille de paquets, etc.).

---

## 📁 Fichiers du Projet

- `intrusion_detection.py` : script principal (prétraitement, entraînement, évaluation)
- `README.md` : ce fichier
- `NSL-KDD.csv` : jeu de données à télécharger manuellement (voir lien ci-dessous)

---

## 📊 Données

Le dataset utilisé est disponible sur Kaggle :  
👉 [NSL-KDD Dataset (Kaggle)](https://www.kaggle.com/datasets/yopx5s/nslkdd)

**⚠️ Remarque :** le fichier CSV doit être téléchargé manuellement et placé dans le même dossier que le script `intrusion_detection.py`.

- Nombre total de connexions : **125 973**
- Nombre de caractéristiques : **42**
- Données équilibrées entre classes normales et attaques

---

## ✅ Résultats du Modèle

- **Accuracy (précision globale)** : 100 %
- **F1-score (normal & attaque)** : 1.00
- **Matrice de confusion :**

```
[[20078     5]
 [   13 17696]]
```

Le modèle détecte presque toutes les attaques sans presque aucun faux positif.

---

## 🔧 Librairies Utilisées

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

---

## 📸 Visualisation

- Matrice de confusion
- Graphique de distribution des classes (`normal` vs `attaque`)
- Option : courbe ROC ou graphique d’importance des features

---

## 💡 Idées d’Amélioration

- Tester d’autres modèles (XGBoost, SVM, etc.)
- Ajuster le modèle pour détecter les **types d’attaques spécifiques** (DoS, R2L, U2R…)
- Déploiement dans un environnement réel avec détection en **temps réel**
