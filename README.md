# L'Aigle Noir - Journal Automatique 🗞️

Ce site est un agrégateur d'actualités mis à jour automatiquement chaque jour à 6h du matin.

## Structure
- **Pages** : Accueil, Monde, Technologie, Économie, France
- **Sources** : Flux RSS publics (Le Monde, Numerama, Les Échos, France Info)
- **Mise à jour** : Via GitHub Actions et un script Python

## Comment ça marche ?
1. Le script `scripts/update_news.py` récupère les dernières actualités depuis les flux RSS.
2. Il génère des résumés originaux et met à jour les pages HTML.
3. GitHub Actions exécute ce script tous les jours à 6h.

## Lien du site
👉 [https://epigone15.github.io/aigle-noir/](https://epigone15.github.io/aigle-noir/)

## Configuration
- **GitHub Pages** : Activé sur la branche `main`
- **Workflow** : `.github/workflows/update.yml`

## Contribuer
- Fork le repo
- Modifie le script ou le design
- Ouvre une Pull Request

© 2026 L'Aigle Noir