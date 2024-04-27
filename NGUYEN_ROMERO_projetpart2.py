#Fonction pour calculer la quantité d'Ethereum achetée
def calc_quantite_achetee(investissement_usd, prix_ouverture, marge=0.25):
    """
    Calcule la quantité d'ETH achetée en fonction de l'investissement initial, du prix d'ouverture et de la marge.
    """
    quantite_achetee = (investissement_usd / prix_ouverture) / marge
    return quantite_achetee

#Fonction pour calculer la performance du contrat perpétuel
def calc_perf_contrat(prix_ouverture, prix_fermeture, taux_financement_moyen, jours_investis, quantite_eth, investissement_usd):
    """
    Calcule la performance financière d'un investissement dans un contrat perpétuel.
    """
    perf = ((prix_fermeture - prix_ouverture) * quantite_eth) - (taux_financement_moyen * investissement_usd * jours_investis)
    return perf

#Fonction pour calculer la performance sur le marché spot
def calc_perf_spot(prix_ouverture, prix_fermeture, quantite_eth):
    """
    Calcule la performance financière d'un investissement sur le marché spot.
    """
    performance = (prix_fermeture - prix_ouverture) * quantite_eth
    return performance

#Calcul du taux de financement moyen
def calculer_Tx_Fi_moyen(taux_financement):
    """
    Calcule le taux de financement moyen à partir des données historiques.
    """
    taux_financement_float = df_Tx_Fi['Taux de financement'] = pd.to_numeric(df_Tx_Fi['Taux de financement'], errors='coerce')
    taux_financement_moyen = taux_financement_float.mean()
    return taux_financement_moyen


#Déclaration des variables préliminaires
investissement_initial_usd = float(input('Entrez le montant de votre investissement initial en USD: '))
jours_investis = (date_fin - date_debut).days
prix_ouverture_spot = float(df_spot.iloc[0]['Ouverture'])
prix_fermeture_contrat = float(df_contrat.iloc[-1]['Fermeture'])
prix_fermeture_spot = float(df_spot.iloc[-1]['Fermeture'])
taux_financement_moyen = calculer_Tx_Fi_moyen(df_Tx_Fi['Taux de financement'])
quantite_eth_achetee = calc_quantite_achetee(investissement_initial_usd, prix_ouverture_spot)

#Calcul des performances
perf_contrat = calc_perf_contrat(prix_ouverture_spot, prix_fermeture_contrat, taux_financement_moyen, jours_investis, quantite_eth_achetee, investissement_initial_usd)
perf_spot = calc_perf_spot(prix_ouverture_spot, prix_fermeture_spot, quantite_eth_achetee)

#Affichage
print("Performance du contrat perpétuel :", perf_contrat, "USD")
print("Performance sur le marché spot :", perf_spot,"USD")

## Conclusion

### Résultats
#Après une année complète de suivi, le script a calculé la performance des investissements en contrats perpétuels et sur le marché spot pour lEthereum. Les résultats montrent des différences significatives de rendement, influencées par les fluctuations du marché et les taux de financement appliqués aux contrats perpétuels.

### Implications
#Ces analyses permettent aux investisseurs de mieux comprendre le comportement des différents instruments financiers dans le domaine des crypto-monnaies. Selon les conditions de marché prévalentes, le choix entre les contrats perpétuels et lachat direct peut avoir un impact substantiel sur le rendement de linvestissement.

### Étapes futures
#Pour des analyses futures, il serait bénéfique délargir cette étude à dautres crypto-monnaies et dintégrer des modèles prédictifs pour mieux anticiper les mouvements de marché et les ajustements des taux de financement.

#Nous encourageons les utilisateurs à explorer différentes configurations de simulation et à ajuster les paramètres selon leurs besoins spécifiques pour maximiser leur compréhension et leur efficacité dans le trading de crypto-monnaies.