import folium
import tkinter as tk
from tkinter import messagebox
import networkx as nx
from geopy.distance import geodesic

senegal_regions = {
    'Dakar': (14.7167, -17.4677),
    'Guédiawaye': (14.7670, -17.3840),
    'Pikine': (14.7534, -17.3912),
    'Rufisque': (14.7192, -17.2827),
    'Diourbel': (14.6517, -16.2333),
    'Bambey': (14.6833, -16.4667),
    'Mbacké': (14.7917, -15.9097),
    'Saint-Louis': (16.0191, -16.4900),
    'Podor': (16.6667, -14.9667),
    'Dagana': (16.5167, -15.6667),
    'Louga': (15.6053, -16.2347),
    'Kebemer': (15.4167, -16.3667),
    'Linguère': (15.3967, -15.1211),
    'Tambacounda': (13.7815, -13.6677),
    'Goudiry': (13.9833, -13.9167),
    'Bakel': (14.8969, -12.4625),
    'Koumpentoum': (13.9792, -13.9181),
    'Thiès': (14.7833, -16.9667),
    'Mbour': (14.4258, -16.9683),
    'Tivaouane': (14.9500, -16.8333),
    'Kaolack': (14.1488, -16.0779),
    'Guinguinéo': (13.8739, -15.7542),
    'Nioro du Rip': (13.7581, -15.8086),
    'Fatick': (14.3395, -16.4060),
    'Foundiougne': (14.1347, -16.4733),
    'Gossas': (14.3114, -15.9406),
    'Kaffrine': (14.1059, -15.5542),
    'Koungheul': (13.9833, -15.5667),
    'Malem Hodar': (14.1500, -15.9500),
    'Birkilane': (14.2500, -15.9667),
    'Kédougou': (12.5572, -12.1744),
    'Saraya': (12.4803, -12.8231),
    'Salémata': (12.7178, -12.4933),
    'Kolda': (12.8861, -14.9497),
    'Vélingara': (12.8539, -14.9658),
    'Médina Yoro Foulah': (13.1500, -14.9500),
    'Matam': (15.6608, -13.2578),
    'Kanel': (15.1667, -13.1333),
    'Ranérou': (15.1167, -13.5500),
    'Sédhiou': (12.7081, -15.5564),
    'Bounkiling': (12.4925, -16.5461),
    'Goudomp': (12.5547, -16.2875),
    'Ziguinchor': (12.5730, -16.2750),
    'Oussouye': (12.4853, -16.5469),
    'Bignona': (12.8067, -16.2256)
}
senegal_routes = [
('Dakar', 'Pikine'),
('Pikine','Rufisque'),
('Pikine','Guediawaye'),
('Rufisque','Mbour'),
('Rufisque','Thiès'),
('Mbour','Fatick'),
('Fatick','Kaolack'),
('Fatick','Gossas'),
('Fatick','Foundiougne'),
('Kaolack','Foundiougne'),
('Kaolack','Guinguineo'),
('Kaolack','Nioro du Rip'),
('Kaolack','Gossas'),
('Thiès','Bambey'),
('Bambey','Diourbel'),
('Diourbel','Gossas'),
('Thiès','Tivaouane'),
('Thiès','Mbour'),
('Diourbel','Mbacké'),
('Tivaouane','Kebemer'),
('Kebemer','Louga'),
('Louga','Linguère'),
('Linguère','Mbacké'),
('Mbacké','Louga'),
('Mbacké','Kebemer'),
('Louga','Saint-Louis'),
('Saint-Louis','Dagana'),
('Dagana','Podor'),
('Podor','Matam'),
('Matam','Kanel'),
('Matam','Ranerou'),
('Matam','Linguère'),
('Linguère','Kanel'),
('Linguère','Podor'),
('Kaffrine','Kaolack'),
('Kaffrine','Mbacké'),
('Kaffrine','Malem Hodar'),
('Malem Hodar','Koungheul'),
('Koungheul','Linguere'),
('Kaffrine','Birkilane'),
('Koungheul','Koumpentoum'),
('Koumpentoum','Tambacounda'),
('Tambacounda','Goudiry'),
('Goudiry','Bakel'),
('Bakel','Kanel'),
('Tambacounda','Kédougou'),
('Tambacounda','Sédhiou'),
('Tambacounda','Bakel'),
('Kédougou','Saraya'),
('Kédougou','Salémata'),
('Tambacounda','Vélingara'),
('Vélingara','Medina Yoro Foulah'),
('Medina Yoro Foulah','Kolda'),
('Kolda','Sèdhiou'),
('Sèdhiou','Bounkiling'),
('Ziguinchor','Bignona'),
('Ziguinchor','Oussouye'),
('Ziguinchor','Goudomp'),
('Sedhiou','Bignona'),
('Bounkiling','Nioro du Rip'),
('Bounkiling','Bignona'),
('Matam','Bakel'),
('Tamba','Bakel'),
('Velingara','Kolda'),
('Tamba','Kaffrine'),

('Pikine','Dakar'),
('Rufisque','Pikine'),
('Guediawaye','Pikine'),
('Keur Massar','Rufisque'),
('Mbour','Rufisque'),
('Thies','Rufisque'),
('Fatick','Mbour'),
('Kaoloack','Fatick'),
('Gossas','Fatick'),
('Foundiougne','Fatick'),
('Foudiougne','Kaolack'),
('Foundiougne','Kaolack'),
('Guinguineo','Kaolack'),
('Nioro du Rip ','Kaolack'),
('Gossas','Kaolack'),
('Bambey','Thies'),
('Diourbel','Bambey'),
('Gossas','Diourbel'),
('Tivaoune','Thiès'),
('Mbour','Thiès'),
('Mbacke','Diourbel'),
('Kebemer','Tivaoune'),
('Louga','Kebemer'),
('Lingère','Louga'),
('Mbacke','Linguère'),
('Louga','Mbacke'),
('Kebemer','Mbacke'),
('Saint-Louis','Louga'),
('Dagana','Saint-Louis'),
('Podor','Dagana'),
('Matam','Podor'),
('Kanel','Matam'),
('Ranerou','Matam'),
('Linguere','Matam'),
('kanel','Linguere'),
('Podor','Linguere'),
('Kaolack','Kaffrine'),
('Mbacké','Kaffrine'),
('Malem Hodar','Kaffrine'),
('Koungheul','Malem Hodar'),
('Linguere','Koungheul'),
('Linguere','Koungheul'),
('Birkilane','Kaffrine'),
('Koumpentoum','Koungheul'),
('Tamba','Koumpentoum'),
('Guoudiry','Tamba'),
('Bakel','Goudiry'),
('Kanel','Kakel'),
('Kedougou','Tamba'),
('Sedhiou','Tamba'),
('Bakel','Tamba'),
('Saraya','Kedougou'),
('Salemata','Kedougou'),
('Velingara','Tamba'),
('medina Yoro Foulah','Velingara'),
('Kolda','medina Yoro Foulah'),
('Kolda','Sedhiou'),
('Bounkiling','Sedhiou'),
('Bounkiling','Koungheul'),
('Bignona','Ziguinchor'),
('Oussouye','Ziguinchor'),
('Goudomp','Ziguinchor'),
('Bignona','Sedhiou'),
('Nioro du Rip','Bounkiling'),
('Bignona','Bounkiling'),
('Bakel','Matam'),
('Bakel','Tambacounda'),
('Kolda','Velingara'),
('Kaffrine','Tambacounda'),
]

# Création du graphe
G = nx.Graph()
G.add_nodes_from(senegal_regions.keys())
G.add_edges_from(senegal_routes)


# Fonction pour calculer la distance entre deux régions
def calculer_distance(region_depart, region_arrivee):
    coord_depart = senegal_regions[region_depart]
    coord_arrivee = senegal_regions[region_arrivee]
    distance = geodesic(coord_depart, coord_arrivee).kilometers
    return distance, [region_depart, region_arrivee]


# Fonction pour tracer le chemin sur la carte
def tracer_chemin(carte, chemin):
    for i in range(len(chemin) - 1):
        region_depart = chemin[i]
        region_arrivee = chemin[i + 1]
        coord_depart = senegal_regions[region_depart]
        coord_arrivee = senegal_regions[region_arrivee]
        carte.add_child(folium.PolyLine([coord_depart, coord_arrivee], color='blue', weight=2.5))


# Fonction principale
def main():
    # Création de la carte
    carte = folium.Map(location=[14.5, -14], zoom_start=7)

    # Tracé des régions
    for region, coord in senegal_regions.items():
        folium.Marker(coord, popup=region).add_to(carte)

    # Fonction pour gérer le bouton de soumission
    def soumettre():
        # Récupérer les valeurs saisies par l'utilisateur
        region_depart = region_depart_entry.get()
        region_arrivee = region_arrivee_entry.get()

        # Vérification si les régions de départ et d'arrivée existent dans les régions du Sénégal
        if region_depart not in senegal_regions.keys() or region_arrivee not in senegal_regions.keys():
            messagebox.showerror("Erreur", "Région de départ ou d'arrivée invalide.")
            return

        # Calcul du plus court chemin
        chemin = nx.dijkstra_path(G, region_depart, region_arrivee)

        # Calcul de la distance entre les régions et les départements traversés
        distance_totale = 0
        departements_traverses = []
        for i in range(len(chemin) - 1):
            region_depart = chemin[i]
            region_arrivee = chemin[i + 1]
            distance, departements = calculer_distance(region_depart, region_arrivee)
            distance_totale += distance
            departements_traverses.extend(departements[1:])

        # Afficher le plus court chemin et la distance avec les départements traversés
        messagebox.showinfo("Plus court chemin", "Le plus court chemin est : {}\nDistance : {} km\nDépartements traversés : {}".format(chemin, distance_totale, departements_traverses))

        # Tracer le chemin sur la carte
        tracer_chemin(carte, chemin)

        # Afficher la carte
        carte.save("carte_senegal.html")
        messagebox.showinfo("Carte", "La carte a été enregistrée sous le nom 'carte_senegal.html'.")

    # Création de l'interface graphique
    root = tk.Tk()
    root.title("Calculateur de chemin - Sénégal")

    # Calcul des dimensions de la fenêtre
    window_width = 500
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Centrer la fenêtre sur l'écran
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Label de bienvenue
    welcome_label = tk.Label(root, text="Bienvenue ! Cher utilisateur", font=("Helvetica", 18))
    welcome_label.pack(pady=10)

    # Label et champ de saisie pour la région de départ
    region_depart_label = tk.Label(root, text="Région de départ:", font=("Helvetica", 12))
    region_depart_label.pack()
    region_depart_entry = tk.Entry(root, font=("Helvetica", 12))
    region_depart_entry.pack()

    # Label et champ de saisie pour la région d'arrivée
    region_arrivee_label = tk.Label(root, text="Région d'arrivée:", font=("Helvetica", 12))
    region_arrivee_label.pack()
    region_arrivee_entry = tk.Entry(root, font=("Helvetica", 12))
    region_arrivee_entry.pack()

    # Bouton de soumission
    soumettre_button = tk.Button(root, text="Calculer le chemin", command=soumettre, font=("Helvetica", 12))
    soumettre_button.pack(pady=10)

    # Exécution de l'interface graphique
    root.mainloop()


if __name__ == '__main__':
    main()
