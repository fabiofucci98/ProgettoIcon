# ProgettoIcon

Per installare libreria arcade:

pip3 install arcade

cambiare variabili d'ambiente (warning: import [module] could not be resolved)

main.py contiene il codice base, tutte le immagini sono in resources

create_scene.py deve contenere tutte le funzioni per la creazione dei muri, stanza, oggetti, ecc

la funzione create_wall in create_scene deve aggiungere alla wall_list ogni muro creato dalle funzioni che creano le stanze

Creata la funzione create_texture in create_scene.py per aggiungere texture di scale e ascensore

Modificato in main.py l'ordine di creazione di player, wall e texture in modo da non far mai scomparire il player sotto le texture, per il futuro, lasciare self.player_list.draw() come ultima funzione

Aggiunto self.physics_engine2 per le collisioni tra player e texture
