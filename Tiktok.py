import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class TikTokCountryAnalyzer:
    def __init__(self, country_name):
        self.country = country_name
        self.colors = ['#FF0051', '#00F2EA', '#69C9D0', '#EE1D52', '#000000', 
                      '#25F4EE', '#FFFFFF', '#2D2D2D', '#FE2C55', '#5E5E5E']
        
        self.start_year = 2016  # TikTok a été lancé internationalement en 2016
        self.end_year = 2025
        
        # Configuration spécifique à chaque pays
        self.config = self._get_country_config()
        
    def _get_country_config(self):
        """Retourne la configuration spécifique pour chaque pays"""
        configs = {
            "United States": {
                "population_base": 331000000,
                "tiktok_users_base": 100000000,
                "market_type": "mature",
                "specialties": ["entertainment", "influencers", "business", "ads", "music"]
            },
            "China": {
                "population_base": 1400000000,
                "tiktok_users_base": 600000000,  # Douyin, la version chinoise
                "market_type": "domestic",
                "specialties": ["e-commerce", "live-streaming", "education", "government"]
            },
            "India": {
                "population_base": 1380000000,
                "tiktok_users_base": 200000000,  # Avant l'interdiction
                "market_type": "emerging",
                "specialties": ["entertainment", "music", "dance", "regional_content"]
            },
            "Brazil": {
                "population_base": 213000000,
                "tiktok_users_base": 82000000,
                "market_type": "growing",
                "specialties": ["music", "dance", "comedy", "social_causes"]
            },
            "Indonesia": {
                "population_base": 274000000,
                "tiktok_users_base": 99000000,
                "market_type": "growing",
                "specialties": ["islamic_content", "comedy", "local_business", "education"]
            },
            "Russia": {
                "population_base": 144000000,
                "tiktok_users_base": 50000000,
                "market_type": "regulated",
                "specialties": ["politics", "comedy", "challenges", "music"]
            },
            "Mexico": {
                "population_base": 128000000,
                "tiktok_users_base": 57500000,
                "market_type": "growing",
                "specialties": ["music", "comedy", "beauty", "family_content"]
            },
            "Vietnam": {
                "population_base": 97300000,
                "tiktok_users_base": 50000000,
                "market_type": "booming",
                "specialties": ["music", "dance", "comedy", "educational"]
            },
            "Philippines": {
                "population_base": 110000000,
                "tiktok_users_base": 43500000,
                "market_type": "booming",
                "specialties": ["dance", "comedy", "family_content", "challenges"]
            },
            "Thailand": {
                "population_base": 70000000,
                "tiktok_users_base": 40000000,
                "market_type": "mature",
                "specialties": ["beauty", "comedy", "food", "music"]
            },
            "United Kingdom": {
                "population_base": 67000000,
                "tiktok_users_base": 23000000,
                "market_type": "mature",
                "specialties": ["comedy", "politics", "business", "education"]
            },
            "France": {
                "population_base": 68000000,
                "tiktok_users_base": 24000000,
                "market_type": "mature",
                "specialties": ["humor", "politics", "culture", "fashion"]
            },
            "Germany": {
                "population_base": 83000000,
                "tiktok_users_base": 22000000,
                "market_type": "growing",
                "specialties": ["comedy", "education", "politics", "business"]
            },
            "Japan": {
                "population_base": 126000000,
                "tiktok_users_base": 17000000,
                "market_type": "emerging",
                "specialties": ["anime", "music", "beauty", "comedy"]
            },
            "South Korea": {
                "population_base": 52000000,
                "tiktok_users_base": 15000000,
                "market_type": "growing",
                "specialties": ["k-pop", "beauty", "fashion", "dance"]
            },
            # Configuration par défaut pour les autres pays
            "default": {
                "population_base": 50000000,
                "tiktok_users_base": 10000000,
                "market_type": "emerging",
                "specialties": ["entertainment", "music", "comedy"]
            }
        }
        
        return configs.get(self.country, configs["default"])
    
    def generate_tiktok_data(self):
        """Génère des données TikTok pour le pays"""
        print(f"📱 Génération des données TikTok pour {self.country}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Year': [date.year for date in dates]}
        
        # Données démographiques
        data['Population'] = self._simulate_population(dates)
        
        # Données utilisateurs TikTok
        data['TikTok_Users'] = self._simulate_tiktok_users(dates)
        data['Active_Users'] = self._simulate_active_users(dates)
        data['Time_Spent_Per_User'] = self._simulate_time_spent(dates)
        
        # Données de contenu
        data['Videos_Uploaded'] = self._simulate_videos_uploaded(dates)
        data['Likes_Count'] = self._simulate_likes_count(dates)
        data['Shares_Count'] = self._simulate_shares_count(dates)
        data['Comments_Count'] = self._simulate_comments_count(dates)
        
        # Données économiques
        data['Ad_Revenue'] = self._simulate_ad_revenue(dates)
        data['Creator_Earnings'] = self._simulate_creator_earnings(dates)
        data['E_Commerce_Revenue'] = self._simulate_ecommerce_revenue(dates)
        
        # Indicateurs d'engagement
        data['Engagement_Rate'] = self._simulate_engagement_rate(dates)
        data['User_Growth_Rate'] = self._simulate_user_growth_rate(dates)
        data['Virality_Score'] = self._simulate_virality_score(dates)
        
        # Données démographiques des utilisateurs
        data['Users_Under_25'] = self._simulate_young_users(dates)
        data['Users_25_34'] = self._simulate_adult_users(dates)
        data['Users_Over_35'] = self._simulate_older_users(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques au pays
        self._add_country_trends(df)
        
        return df
    
    def _simulate_population(self, dates):
        """Simule la population du pays"""
        base_population = self.config["population_base"]
        
        population = []
        for i, date in enumerate(dates):
            # Croissance démographique variable selon le pays
            if self.config["market_type"] == "mature":
                growth_rate = 0.004  # Croissance faible pour les pays développés
            elif self.config["market_type"] == "booming":
                growth_rate = 0.012  # Croissance forte pour les pays émergents
            else:
                growth_rate = 0.008  # Croissance moyenne
                
            growth = 1 + growth_rate * i
            population.append(base_population * growth)
        
        return population
    
    def _simulate_tiktok_users(self, dates):
        """Simule le nombre d'utilisateurs TikTok"""
        base_users = self.config["tiktok_users_base"]
        
        users = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Croissance différente selon le type de marché
            if self.config["market_type"] == "mature":
                if year < 2020:
                    growth_rate = 0.35  # Croissance rapide avant maturité
                else:
                    growth_rate = 0.08  # Ralentissement après maturité
            elif self.config["market_type"] == "booming":
                growth_rate = 0.25  # Croissance soutenue
            elif self.config["market_type"] == "emerging":
                growth_rate = 0.40  # Croissance très forte
            else:  # regulated ou autres
                growth_rate = 0.15  # Croissance modérée
                
            growth = 1 + growth_rate * i
            # Limite maximale en pourcentage de la population
            max_percentage = 0.65 if self.config["market_type"] != "domestic" else 0.45
            max_users = self.config["population_base"] * max_percentage
            
            users.append(min(base_users * growth, max_users))
        
        return users
    
    def _simulate_active_users(self, dates):
        """Simule le nombre d'utilisateurs actifs"""
        active_users = []
        for i, date in enumerate(dates):
            # Pourcentage d'utilisateurs actifs (varie selon le pays)
            if self.config["market_type"] == "mature":
                active_rate = 0.75  # Taux d'activité élevé dans les marchés matures
            elif self.config["market_type"] == "booming":
                active_rate = 0.85  # Très haut taux d'activité dans les marchés en croissance
            else:
                active_rate = 0.70  # Taux moyen
            
            active_users.append(self._simulate_tiktok_users([date])[0] * active_rate)
        
        return active_users
    
    def _simulate_time_spent(self, dates):
        """Simule le temps passé par utilisateur (en minutes par jour)"""
        time_spent = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Augmentation générale du temps passé sur TikTok
            base_time = 45  # minutes par jour
            
            if year < 2018:
                time = base_time * 0.7
            elif year < 2020:
                time = base_time * 0.9
            elif year < 2022:
                time = base_time * 1.1
            else:
                time = base_time * 1.2
            
            # Ajustements selon le pays
            if self.config["market_type"] == "booming":
                time *= 1.15  # Plus de temps dans les marchés en croissance
            elif self.config["market_type"] == "emerging":
                time *= 1.25  # Encore plus dans les marchés émergents
            
            time_spent.append(time)
        
        return time_spent
    
    def _simulate_videos_uploaded(self, dates):
        """Simule le nombre de vidéos uploadées"""
        videos = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Base de calcul : nombre de vidéos par utilisateur actif
            if year < 2018:
                videos_per_user = 0.8  # Faible au début
            elif year < 2020:
                videos_per_user = 1.2  # Augmentation
            elif year < 2022:
                videos_per_user = 1.5  # Continue d'augmenter
            else:
                videos_per_user = 1.8  # Stabilisation
            
            # Ajustements selon le pays
            if self.config["market_type"] == "booming":
                videos_per_user *= 1.3  # Plus de création de contenu
            elif "comedy" in self.config["specialties"]:
                videos_per_user *= 1.2  # Plus de contenu humoristique
            
            videos.append(self._simulate_active_users([date])[0] * videos_per_user * 365)
        
        return videos
    
    def _simulate_likes_count(self, dates):
        """Simule le nombre de likes"""
        likes = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Base de calcul : likes par vidéo
            if year < 2018:
                likes_per_video = 150
            elif year < 2020:
                likes_per_video = 250
            elif year < 2022:
                likes_per_video = 350
            else:
                likes_per_video = 400
            
            likes.append(self._simulate_videos_uploaded([date])[0] * likes_per_video)
        
        return likes
    
    def _simulate_shares_count(self, dates):
        """Simule le nombre de partages"""
        shares = []
        for i, date in enumerate(dates):
            # Partages en proportion des likes
            share_ratio = 0.08  # 8% des likes sont partagés
            
            shares.append(self._simulate_likes_count([date])[0] * share_ratio)
        
        return shares
    
    def _simulate_comments_count(self, dates):
        """Simule le nombre de commentaires"""
        comments = []
        for i, date in enumerate(dates):
            # Commentaires en proportion des likes
            comment_ratio = 0.05  # 5% des likes ont des commentaires
            
            comments.append(self._simulate_likes_count([date])[0] * comment_ratio)
        
        return comments
    
    def _simulate_ad_revenue(self, dates):
        """Simule les revenus publicitaires"""
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Revenus par utilisateur
            if year < 2018:
                revenue_per_user = 2.5  # Faible au début
            elif year < 2020:
                revenue_per_user = 5.0  # Augmentation
            elif year < 2022:
                revenue_per_user = 8.0  # Continue d'augmenter
            else:
                revenue_per_user = 12.0  # Stabilisation à un niveau élevé
            
            # Ajustements selon le pays
            if self.config["market_type"] == "mature":
                revenue_per_user *= 1.5  # Revenus plus élevés dans les marchés matures
            elif self.config["market_type"] == "regulated":
                revenue_per_user *= 0.7  # Revenus réduits dans les marchés régulés
            
            revenue.append(self._simulate_active_users([date])[0] * revenue_per_user)
        
        return revenue
    
    def _simulate_creator_earnings(self, dates):
        """Simule les revenus des créateurs"""
        earnings = []
        for i, date in enumerate(dates):
            # Revenus des créateurs en proportion des revenus publicitaires
            creator_ratio = 0.25  # 25% des revenus publicitaires vont aux créateurs
            
            earnings.append(self._simulate_ad_revenue([date])[0] * creator_ratio)
        
        return earnings
    
    def _simulate_ecommerce_revenue(self, dates):
        """Simule les revenus du commerce électronique"""
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Développement progressif du e-commerce
            if year < 2019:
                ecommerce_revenue = 0  # Presque inexistant au début
            elif year < 2021:
                ecommerce_revenue = self._simulate_ad_revenue([date])[0] * 0.1  # 10% des revenus pub
            elif year < 2023:
                ecommerce_revenue = self._simulate_ad_revenue([date])[0] * 0.2  # 20% des revenus pub
            else:
                ecommerce_revenue = self._simulate_ad_revenue([date])[0] * 0.3  # 30% des revenus pub
            
            # Ajustements selon le pays
            if "e-commerce" in self.config["specialties"]:
                ecommerce_revenue *= 1.5  # Revenus e-commerce plus élevés
            
            revenue.append(ecommerce_revenue)
        
        return revenue
    
    def _simulate_engagement_rate(self, dates):
        """Simule le taux d'engagement"""
        engagement = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year < 2018:
                rate = 0.12  # Faible au début
            elif year < 2020:
                rate = 0.16  # Augmentation
            elif year < 2022:
                rate = 0.18  # Continue d'augmenter
            else:
                rate = 0.20  # Stabilisation
            
            # Ajustements selon le pays
            if self.config["market_type"] == "booming":
                rate *= 1.15  # Engagement plus élevé
            
            engagement.append(rate)
        
        return engagement
    
    def _simulate_user_growth_rate(self, dates):
        """Simule le taux de croissance des utilisateurs"""
        growth_rates = []
        previous_users = self.config["tiktok_users_base"]
        
        for i, date in enumerate(dates):
            current_users = self._simulate_tiktok_users([date])[0]
            growth_rate = (current_users - previous_users) / previous_users if previous_users > 0 else 0
            growth_rates.append(growth_rate)
            previous_users = current_users
        
        return growth_rates
    
    def _simulate_virality_score(self, dates):
        """Simule un score de viralité"""
        virality = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year < 2018:
                score = 1.2  # Faible au début
            elif year < 2020:
                score = 1.5  # Augmentation
            elif year < 2022:
                score = 1.8  # Continue d'augmenter
            else:
                score = 2.0  # Stabilisation
            
            # Ajustements selon le pays
            if "music" in self.config["specialties"] or "dance" in self.config["specialties"]:
                score *= 1.2  # Contenu plus viral
            
            virality.append(score)
        
        return virality
    
    def _simulate_young_users(self, dates):
        """Simule le nombre d'utilisateurs de moins de 25 ans"""
        young_users = []
        for i, date in enumerate(dates):
            # Pourcentage d'utilisateurs jeunes
            if self.config["market_type"] == "mature":
                young_ratio = 0.45  # Moins de jeunes dans les marchés matures
            else:
                young_ratio = 0.60  # Plus de jeunes ailleurs
            
            young_users.append(self._simulate_tiktok_users([date])[0] * young_ratio)
        
        return young_users
    
    def _simulate_adult_users(self, dates):
        """Simule le nombre d'utilisateurs de 25 à 34 ans"""
        adult_users = []
        for i, date in enumerate(dates):
            adult_ratio = 0.30  # Proportion stable
            
            adult_users.append(self._simulate_tiktok_users([date])[0] * adult_ratio)
        
        return adult_users
    
    def _simulate_older_users(self, dates):
        """Simule le nombre d'utilisateurs de plus de 35 ans"""
        older_users = []
        for i, date in enumerate(dates):
            # Le reste des utilisateurs
            young_ratio = 0.45 if self.config["market_type"] == "mature" else 0.60
            adult_ratio = 0.30
            older_ratio = 1 - young_ratio - adult_ratio
            
            older_users.append(self._simulate_tiktok_users([date])[0] * older_ratio)
        
        return older_users
    
    def _add_country_trends(self, df):
        """Ajoute des tendances spécifiques au pays"""
        for i, row in df.iterrows():
            year = row['Year']
            
            # Développement initial (2016-2018)
            if 2016 <= year <= 2018:
                df.loc[i, 'User_Growth_Rate'] *= 1.2  # Croissance très forte au début
            
            # Expansion internationale (2019-2020)
            if 2019 <= year <= 2020:
                df.loc[i, 'Ad_Revenue'] *= 1.3  # Forte croissance des revenus
            
            # Période COVID-19 (2020-2021) - augmentation de l'usage
            if 2020 <= year <= 2021:
                df.loc[i, 'Time_Spent_Per_User'] *= 1.25
                df.loc[i, 'Active_Users'] *= 1.15
            
            # Développement du e-commerce (2021-2023)
            if 2021 <= year <= 2023:
                if "e-commerce" in self.config["specialties"]:
                    df.loc[i, 'E_Commerce_Revenue'] *= 1.4
            
            # Maturité du marché (2023-2025)
            if year >= 2023:
                if self.config["market_type"] == "mature":
                    df.loc[i, 'User_Growth_Rate'] *= 0.7  # Ralentissement de la croissance
    
    def create_tiktok_analysis(self, df):
        """Crée une analyse complète de TikTok pour le pays"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des utilisateurs
        ax1 = plt.subplot(4, 2, 1)
        self._plot_user_evolution(df, ax1)
        
        # 2. Revenus de TikTok
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_evolution(df, ax2)
        
        # 3. Engagement des utilisateurs
        ax3 = plt.subplot(4, 2, 3)
        self._plot_engagement_metrics(df, ax3)
        
        # 4. Démographie des utilisateurs
        ax4 = plt.subplot(4, 2, 4)
        self._plot_user_demographics(df, ax4)
        
        # 5. Contenu généré
        ax5 = plt.subplot(4, 2, 5)
        self._plot_content_metrics(df, ax5)
        
        # 6. Croissance
        ax6 = plt.subplot(4, 2, 6)
        self._plot_growth_metrics(df, ax6)
        
        # 7. Répartition des revenus
        ax7 = plt.subplot(4, 2, 7)
        self._plot_revenue_breakdown(df, ax7)
        
        # 8. Comparaison internationale
        ax8 = plt.subplot(4, 2, 8)
        self._plot_international_comparison(df, ax8)
        
        plt.suptitle(f'Analyse de TikTok en {self.country} ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.country}_tiktok_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_tiktok_insights(df)
    
    def _plot_user_evolution(self, df, ax):
        """Plot de l'évolution des utilisateurs"""
        ax.plot(df['Year'], df['TikTok_Users'], label='Utilisateurs Totaux', 
               linewidth=2, color='#FF0051', alpha=0.8)
        ax.plot(df['Year'], df['Active_Users'], label='Utilisateurs Actifs', 
               linewidth=2, color='#00F2EA', alpha=0.8)
        
        ax.set_title('Évolution des Utilisateurs de TikTok', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Nombre d\'utilisateurs')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_revenue_evolution(self, df, ax):
        """Plot de l'évolution des revenus"""
        ax.plot(df['Year'], df['Ad_Revenue'], label='Revenus Publicitaires', 
               linewidth=2, color='#FF0051', alpha=0.8)
        ax.plot(df['Year'], df['E_Commerce_Revenue'], label='Revenus E-Commerce', 
               linewidth=2, color='#25F4EE', alpha=0.8)
        ax.plot(df['Year'], df['Creator_Earnings'], label='Revenus Créateurs', 
               linewidth=2, color='#69C9D0', alpha=0.8)
        
        ax.set_title('Évolution des Revenus (M$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Revenus (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_engagement_metrics(self, df, ax):
        """Plot des métriques d'engagement"""
        ax.plot(df['Year'], df['Engagement_Rate'], label='Taux d\'Engagement', 
               linewidth=2, color='#FF0051', alpha=0.8)
        ax.plot(df['Year'], df['Time_Spent_Per_User'], label='Temps passé/jour (min)', 
               linewidth=2, color='#25F4EE', alpha=0.8)
        
        ax.set_title('Métriques d\'Engagement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux / Minutes')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_user_demographics(self, df, ax):
        """Plot de la démographie des utilisateurs"""
        years = df['Year']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Users_Under_25', 'Users_25_34', 'Users_Over_35']
        colors = ['#FF0051', '#25F4EE', '#69C9D0']
        labels = ['Moins de 25 ans', '25-34 ans', '35 ans et plus']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition par Âge des Utilisateurs', fontsize=12, fontweight='bold')
        ax.set_ylabel('Nombre d\'utilisateurs')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_content_metrics(self, df, ax):
        """Plot des métriques de contenu"""
        ax.plot(df['Year'], df['Videos_Uploaded'], label='Vidéo Uploadées', 
               linewidth=2, color='#FF0051', alpha=0.8)
        ax.plot(df['Year'], df['Likes_Count'], label='Likes', 
               linewidth=2, color='#25F4EE', alpha=0.8)
        ax.plot(df['Year'], df['Shares_Count'], label='Partages', 
               linewidth=2, color='#69C9D0', alpha=0.8)
        
        ax.set_title('Métriques de Contenu', fontsize=12, fontweight='bold')
        ax.set_ylabel('Nombre')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_growth_metrics(self, df, ax):
        """Plot des métriques de croissance"""
        ax.bar(df['Year'], df['User_Growth_Rate'], label='Taux de Croissance', 
              color='#FF0051', alpha=0.7)
        
        ax.set_title('Taux de Croissance des Utilisateurs', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux de Croissance', color='#FF0051')
        ax.tick_params(axis='y', labelcolor='#FF0051')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Score de viralité en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Year'], df['Virality_Score'], label='Score de Viralité', 
                linewidth=3, color='#25F4EE')
        ax2.set_ylabel('Score de Viralité', color='#25F4EE')
        ax2.tick_params(axis='y', labelcolor='#25F4EE')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_revenue_breakdown(self, df, ax):
        """Plot de la répartition des revenus"""
        years = df['Year']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Ad_Revenue', 'E_Commerce_Revenue', 'Creator_Earnings']
        colors = ['#FF0051', '#25F4EE', '#69C9D0']
        labels = ['Publicité', 'E-Commerce', 'Créateurs']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition des Revenus (M$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Revenus (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_international_comparison(self, df, ax):
        """Plot de comparaison internationale"""
        # Cette méthode serait normalement plus complexe avec des données réelles
        # Pour cette démonstration, nous utilisons des données simulées
        
        # Simuler des données pour les principaux pays
        major_countries = ["United States", "China", "India", "Brazil", "Indonesia"]
        years = df['Year']
        
        for country in major_countries:
            if country == self.country:
                continue  # Ne pas comparer le pays avec lui-même
            
            # Simuler des données pour ce pays (simplifié)
            country_config = self._get_country_config_for_country(country)
            country_users = [country_config["tiktok_users_base"] * (1 + 0.2 * i) for i, year in enumerate(years)]
            
            ax.plot(years, country_users, label=country, alpha=0.7)
        
        # Ajouter le pays actuel
        ax.plot(years, df['TikTok_Users'], label=self.country, linewidth=3, color='#FF0051')
        
        ax.set_title('Comparaison Internationale des Utilisateurs', fontsize=12, fontweight='bold')
        ax.set_ylabel('Nombre d\'utilisateurs')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _get_country_config_for_country(self, country):
        """Helper method to get config for any country"""
        configs = {
            "United States": {"tiktok_users_base": 100000000},
            "China": {"tiktok_users_base": 600000000},
            "India": {"tiktok_users_base": 200000000},
            "Brazil": {"tiktok_users_base": 82000000},
            "Indonesia": {"tiktok_users_base": 99000000},
        }
        return configs.get(country, {"tiktok_users_base": 50000000})
    
    def _generate_tiktok_insights(self, df):
        """Génère des insights analytiques sur TikTok"""
        print(f"📱 INSIGHTS ANALYTIQUES - TikTok en {self.country}")
        print("=" * 60)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_users = df['TikTok_Users'].mean()
        avg_active_users = df['Active_Users'].mean()
        avg_time_spent = df['Time_Spent_Per_User'].mean()
        
        print(f"Utilisateurs moyens annuels: {avg_users:,.0f}")
        print(f"Utilisateurs actifs moyens: {avg_active_users:,.0f}")
        print(f"Temps moyen passé par utilisateur: {avg_time_spent:.1f} min/jour")
        
        # 2. Croissance
        print("\n2. 📊 TAUX DE CROISSANCE:")
        user_growth = ((df['TikTok_Users'].iloc[-1] / 
                       df['TikTok_Users'].iloc[0]) - 1) * 100
        revenue_growth = ((df['Ad_Revenue'].iloc[-1] / 
                          df['Ad_Revenue'].iloc[0]) - 1) * 100
        
        print(f"Croissance des utilisateurs ({self.start_year}-{self.end_year}): {user_growth:.1f}%")
        print(f"Croissance des revenus ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        
        # 3. Structure des utilisateurs
        print("\n3. 📋 DÉMOGRAPHIE DES UTILISATEURS:")
        last_year = df.iloc[-1]
        under_25_share = (last_year['Users_Under_25'] / last_year['TikTok_Users']) * 100
        over_35_share = (last_year['Users_Over_35'] / last_year['TikTok_Users']) * 100
        
        print(f"Part des moins de 25 ans: {under_25_share:.1f}%")
        print(f"Part des 35 ans et plus: {over_35_share:.1f}%")
        
        # 4. Revenus et économie
        print("\n4. 💰 ÉCONOMIE DE TIKTOK:")
        avg_ad_revenue = df['Ad_Revenue'].mean()
        avg_creator_earnings = df['Creator_Earnings'].mean()
        ad_revenue_per_user = avg_ad_revenue / avg_active_users if avg_active_users > 0 else 0
        
        print(f"Revenus publicitaires moyens: ${avg_ad_revenue:,.2f} M")
        print(f"Revenus moyens des créateurs: ${avg_creator_earnings:,.2f} M")
        print(f"Revenus publicitaires par utilisateur: ${ad_revenue_per_user:.2f}")
        
        # 5. Spécificités du pays
        print(f"\n5. 🌟 SPÉCIFICITÉS DE {self.country.upper()}:")
        print(f"Type de marché: {self.config['market_type']}")
        print(f"Spécialités: {', '.join(self.config['specialties'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 2016: Lancement international de TikTok")
        print("• 2018: Fusion avec Musical.ly et expansion rapide")
        print("• 2020: Pic d'utilisation pendant la pandémie COVID-19")
        print("• 2020: Menaces d'interdiction aux États-Unis et ailleurs")
        print("• 2021: Développement accéléré des fonctionnalités e-commerce")
        print("• 2022-2025: Maturation du marché et diversification des revenus")
        
        # 7. Recommandations
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        if self.config["market_type"] == "mature":
            print("• Se concentrer sur la monétisation et la rétention des utilisateurs")
            print("• Développer de nouvelles sources de revenus (e-commerce, abonnements)")
        elif self.config["market_type"] == "booming":
            print("• Capitaliser sur la croissance rapide pour accroître la part de marché")
            print("• Adapter le contenu aux spécificités culturelles locales")
        elif self.config["market_type"] == "emerging":
            print("• Investir dans le marketing pour accélérer l'adoption")
            print("• Développer des partenariats avec des créateurs locaux")
        
        if "e-commerce" in self.config["specialties"]:
            print("• Développer les intégrations e-commerce et les boutiques en ligne")
        if "music" in self.config["specialties"]:
            print("• Renforcer les partenariats avec l'industrie musicale")
        if "education" in self.config["specialties"]:
            print("• Développer du contenu éducatif et informatif")

def main():
    """Fonction principale pour l'analyse de TikTok"""
    # Liste des pays les plus concernés par TikTok
    countries = [
        "United States", "China", "India", "Brazil", "Indonesia",
        "Russia", "Mexico", "Vietnam", "Philippines", "Thailand",
        "United Kingdom", "France", "Germany", "Japan", "South Korea"
    ]
    
    print("📱 ANALYSE DE TIKTOK PAR PAYS (2016-2025)")
    print("=" * 60)
    
    # Demander à l'utilisateur de choisir un pays
    print("Liste des pays disponibles:")
    for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")
    
    try:
        choix = int(input("\nChoisissez le numéro du pays à analyser: "))
        if choix < 1 or choix > len(countries):
            raise ValueError
        pays_selectionne = countries[choix-1]
    except (ValueError, IndexError):
        print("Choix invalide. Sélection des États-Unis par défaut.")
        pays_selectionne = "United States"
    
    # Initialiser l'analyseur
    analyzer = TikTokCountryAnalyzer(pays_selectionne)
    
    # Générer les données
    tiktok_data = analyzer.generate_tiktok_data()
    
    # Sauvegarder les données
    output_file = f'{pays_selectionne}_tiktok_data_2016_2025.csv'
    tiktok_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(tiktok_data[['Year', 'TikTok_Users', 'Active_Users', 'Ad_Revenue', 'Engagement_Rate']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse TikTok...")
    analyzer.create_tiktok_analysis(tiktok_data)
    
    print(f"\n✅ Analyse de TikTok en {pays_selectionne} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Utilisateurs, engagement, revenus, contenu")

if __name__ == "__main__":
    main()