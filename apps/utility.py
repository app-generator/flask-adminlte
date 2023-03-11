import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)



def clean_VDMataReferencementBrut(form): 

    form["key"] = form["KEY"]
    form.pop("KEY")

    form["EstimationProduction_last_1"] = form["EstimationProduction_n-1_1"]
    form.pop("EstimationProduction_n-1_1")

    form["xsaison_last_1"] = form["xsaison_n-1_1"]
    form.pop("xsaison_n-1_1")

    form["xsaison_last_but_one_1"] = form["xsaison_n-2_1"]
    form.pop("xsaison_n-2_1")

    form["xsaison_last_but_two_1"] = form["xsaison_n-3_1"]
    form.pop("xsaison_n-3_1")

    if "groupement" in form: 
        form["pgroupement"] = form["groupement"]
        form.pop("groupement")

    if "IdParcelle_1" in form: 
        form["idParcelle_1"] = form["IdParcelle_1"]
        form.pop("IdParcelle_1")

    if "IdParcelle_2" in form: 
        form["idParcelle_2"] = form["IdParcelle_2"]
        form.pop("IdParcelle_2")

    if "IdParcelle_3" in form: 
        form["idParcelle_3"] = form["IdParcelle_3"]
        form.pop("IdParcelle_3")

    if "Nom" in form: 
        form["pNom"] = form["Nom"]
        form.pop("Nom")

    if "Prenom" in form: 
        form["pPrenom"] = form["Prenom"]
        form.pop("Prenom")

    if "Photo" in form: 
        form["pPhoto"] = form["Photo"]
        form.pop("Photo")

    if "Poincon" in form: 
        form["pPoincon"] = form["Poincon"]
        form.pop("Poincon")

    if "Genre" in form: 
        form["pGenre"] = form["Genre"]
        form.pop("Genre")

    if "Cin" in form: 
        form["pCin"] = form["Cin"]
        form.pop("Cin")

    if "PhotoCin" in form: 
        form["pPhotoCin"] = form["PhotoCin"]
        form.pop("PhotoCin")

    if "DateNaissance" in form: 
        form["pDateNaissance"] = form["DateNaissance"]
        form.pop("DateNaissance")

    if "District" in form: 
        form["pDistrict"] = form["District"]
        form.pop("District")

    if "Commune" in form: 
        form["pCommune"] = form["Commune"]
        form.pop("Commune")

    if "Fokontany" in form: 
        form["pFokontany"] = form["Fokontany"]
        form.pop("Fokontany")

    if "Village" in form: 
        form["pVillage"] = form["Village"]
        form.pop("Village")

    if "EstimationProduction_n-1_2" in form: 
        form["EstimationProduction_last_1"] = form["EstimationProduction_n-1_2"]
        form.pop("EstimationProduction_n-1_2")

    if "xsaison_n-1_2" in form: 
        form["xsaison_last_2"] = form["xsaison_n-1_2"]
        form.pop("xsaison_n-1_2")

    if "xsaison_n-2_2" in form: 
        form["xsaison_last_but_one_2"] = form["xsaison_n-2_2"]
        form.pop("xsaison_n-2_2")

    if "xsaison_n-3_2" in form: 
        form["xsaison_last_but_two_2"] = form["xsaison_n-3_2"]
        form.pop("xsaison_n-3_2")

    if "cammpagne" in form: 
        form["campagne"] = form["cammpagne"]
        form.pop("cammpagne")


    # Handle multiple plots dynamically
    if "idParcelle_3" in form: form.pop("idParcelle_3")

    if "NomParcelle_3" in form: form.pop("NomParcelle_3")

    if "DescriptionParcelle_3" in form: form.pop("DescriptionParcelle_3")

    if "ConsigneGarmin_3" in form: form.pop("ConsigneGarmin_3")

    if "StatutParcelle_3" in form: form.pop("StatutParcelle_3")
    
    if "Surface_3" in form: form.pop("Surface_3")

    if "TotalPlants_3" in form: form.pop("TotalPlants_3")

    if "PlantsProductives_3" in form: form.pop("PlantsProductives_3")

    if "AgeMoyenPlants_3" in form: form.pop("AgeMoyenPlants_3")

    if "PhotoParcelle_3" in form: form.pop("PhotoParcelle_3")

    if "EstimationProduction_3" in form: form.pop("EstimationProduction_3")

    if "EstimationProduction_n-1_3" in form: form.pop("EstimationProduction_n-1_3")

    if "Estimation_VRAC_3" in form: form.pop("Estimation_VRAC_3")

    if "EstimationProduction_n-2_3" in form: form.pop("EstimationProduction_n-2_3")

    if "GPS_3" in form: form.pop("GPS_3")

    if "xsaison_n-1_3" in form: form.pop("xsaison_n-1_3")

    if "xsaison_n-2_3" in form: form.pop("xsaison_n-2_3")

    if "xsaison_n-3_3" in form: form.pop("xsaison_n-3_3")

    if "otherstatus_1" in form: form.pop("otherstatus_1")
    

    return form