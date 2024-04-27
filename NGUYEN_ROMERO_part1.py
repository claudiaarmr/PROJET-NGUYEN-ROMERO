# Analyse de Performance des Contrats Perpétuels vs Marché Spot pour Ethereum

## Contexte
#Dans le cadre de lévaluation des investissements en crypto-monnaies, il est crucial de comprendre les différentes options de trading disponibles. Ce projet se concentre sur la comparaison entre les contrats perpétuels et les achats directs sur le marché spot pour lEthereum (ETH). Les contrats perpétuels, une forme populaire de dérivés sur les plateformes de crypto-monnaies, nont pas de date dexpiration et ajustent continuellement leur valeur à travers des taux de financement pour imiter le marché spot.

## Objectif
#Lobjectif de ce projet est de calculer et de comparer la performance financière dune position longue sur un contrat perpétuel avec celle dun achat direct sur le marché spot. Nous utilisons des données historiques pour estimer les coûts et les rendements, en tenant compte des taux de financement et des fluctuations des prix pendant lannée 2023.


import requests
import pandas as pd
  
#Choix de la période
from datetime import datetime

date_debut = datetime(2023, 1, 1)
date_fin = datetime(2023, 12, 31)

    # Conversion en millisecondes
timestamp_debut = int(date_debut.timestamp() * 1000)
timestamp_fin = int(date_fin.timestamp() * 1000)

#Choix de la cryptomonnaie

Crypto = "ETHUSDT" #nous avons choisi la crypto ethereum

#Collecte de données
url_contrat = f"https://api.binance.com/api/v1/klines?symbol=ETHUSDT&interval=1d&startTime={timestamp_debut}&endTime={timestamp_fin}"
url_spot = f"https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1d&startTime={timestamp_debut}&endTime={timestamp_fin}"
url_Tx_Fi = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol=ETHUSDT&interval=1d&startTime={timestamp_debut}&endTime={timestamp_fin}"

response_contrat = requests.get(url_contrat)
response_spot = requests.get(url_spot)
response_Tx_Fi = requests.get(url_Tx_Fi)

data_contrat = response_contrat.json()
data_spot = response_spot.json()
data_Tx_Fi = response_Tx_Fi.json()

#Nom des colonnes pour le DataFrame
colonnes = ['Date ouverture','Ouverture','Plus haut','Plus bas','Fermeture','Volume','Date fermeture','Volume Trades','Nombre Trades','Taker buy base asset volume','Taker buy quote asset volume','Valeur à ignorer']
colonnes2 = ['fundingTime', 'fundingRate']  

#Conversion en DataFrame
df_contrat = pd.DataFrame(data_contrat, columns = colonnes)
df_spot = pd.DataFrame(data_spot, columns = colonnes)
df_Tx_Fi = pd.DataFrame(data_Tx_Fi, columns = colonnes2)


#Reconversion des dates en dates lisibles
df_contrat['Date ouverture'] = pd.to_datetime(df_contrat['Date ouverture'], unit='ms')
df_contrat['Date fermeture'] = pd.to_datetime(df_contrat['Date fermeture'], unit='ms')

df_spot['Date ouverture'] = pd.to_datetime(df_spot['Date ouverture'], unit='ms')
df_spot['Date fermeture'] = pd.to_datetime(df_spot['Date fermeture'], unit='ms')
df_Tx_Fi['fundingTime'] = pd.to_datetime(df_Tx_Fi['fundingTime'], unit='ms')

df_Tx_Fi.rename(columns={'fundingTime': 'Dates', 'fundingRate': 'Taux de financement'}, inplace=True)
