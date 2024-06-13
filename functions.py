# On importe toutes les bibliothèques utile pour les fonctions
import matplotlib.pyplot as plt
import numpy as np

# Affichage de l'éboulis des valeurs propres
def display_scree_plot(pca):
    scree = pca.explained_variance_ratio_*100
    plt.bar(np.arange(len(scree)) + 1, scree)
    plt.plot(np.arange(len(scree)) + 1, scree.cumsum(), c="red", marker='o')
    plt.xlabel("Nombre de composantes principales")
    plt.ylabel("Variance expliquée (%)")
    plt.title("Eboulis des valeurs propres")
    plt.show()