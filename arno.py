
#Partie 1 : Johnny Saravouth Marie-Ange
liste = f"""accompagnement_personnes_agees, adil, afpa, anah, apec, apecita, ars, ars_antenne, banque_de_france, bav,
bsn, caa, caf, carsat, ccas, cci, cdas, cddp, cdg, centre_detention, centre_impots_fonciers, centre_penitentiaire, centre_social, cesr, cg, chambre_agriculture, chambre_metier, cicas, cidf, cij, cio, civi, clic, cnfpt, cnra, commissariat_police, commission_conciliation, conciliateur_fiscal, conseil_culture, cour_appel, cpam, cr, crc, crdp, creps, crfpn, crib, crous, csl, dac, dd_femmes, dd_fip, ddcs, ddcspp, ddpjj, ddpp, ddsp, ddt, defenseur_droits, did_routes, dir_mer, dir_meteo, dir_pj, direccte, direccte_ut, dml, dr_femmes, dr_fip, dr_insee, drac, draf, drddi, dreal, dreal_ut, driea, driea_ut, driee, driee_ut, drihl, drihl_ut, drjscs, dronisep, drpjj, drrt, drsp, dz_paf, edas, epci, esm, fdapp, fdc, fongecif, gendarmerie, greta, hypotheque, inspection_academique, maia, mairie, mairie_com, mairie_mobile, maison_arret, maison_centrale, maison_handicapees, mds, mission_locale, mjd, msa, ofii, onac, onf, paris_mairie, paris_mairie_arrondissement, paris_ppp, paris_ppp_antenne, paris_ppp_certificat_immatriculation, paris_ppp_gesvres, paris_ppp_permis_conduire, permanence_juridique, permanence_sociale, pif, pmi, pole_emploi, pp_marseille, prefecture, prefecture_greffe_associations, prefecture_region, prudhommes, rectorat, sdac, sdsei, service_navigation, 
sgami, sie, sip, sous_pref, spip, suio, ta, te, tgi, ti, tresorerie, tribunal_commerce, urssaf"""
liste2= liste.split(",")
liste3=[]
for elem in liste2:
    liste3.append(elem.lstrip())
#Partie 3 : Teklit , Johnny
for elem in liste3:
    print("{key:'"+elem+"', value:'"+elem+"', text: '"+elem+"'},")


