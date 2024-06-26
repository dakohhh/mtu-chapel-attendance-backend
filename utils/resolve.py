from database.choices import Department
import numpy as np
import random

def resolve_dept(value: str):

        if value in [
            "BSc MASS COM",
            "MCM",
            "MCM",
            "MASS COMMUNICATION",
            "BSc MASSCOM",
            "MASS COMMUNICATION NDH-B106",
            "MASS COMMUNICATION    NEH-R104",
            "MASS COMM",
            "MASS COMMUNICATION",
        ]:
            return Department.MASS_COMMUNICATION.value

        elif value in ["PHYSICS"]:
            return Department.PHYSICS.value

        elif value in [
            "BSc BUS ADMIN",
            "BUSINESS ADMINISTRATION",
            "BUSINESS ADMINISTRATION",
            "BSc BUS ADMIN",
            "BUSINESS ADMIN",
            "BUSINESS ADMIN",
            "BUISNESS ADMIN",
        ]:
            return Department.BUSINESS_ADMIN.value

        elif value in ["ECONOMICS", "ECO", "ECO", "ECO "]:
            return Department.ECONOMICS.value

        elif value in [
            "PUBLIC ADMINISTRATION",
            "PUBLIC ADMIN",
            "Bsc Public Admin",
            "PAD",
        ]:
            return Department.PUBLIC_ADMINISTRATION.value

        elif value in [
            "RELIGIOUS",
            "RELIGIOUS STUDIES",
            "RELIGIOUS AND PHIL",
            "RELIGIOS STUDIES",
            "PHILOSOPHY",
        ]:
            return Department.PHILOSOPHY_RELIGION.value

        elif value in ["FINANCE", "BANKING &FINANCE"]:
            return Department.BANKING_FINANCE.value

        elif value in ["CHEMISTRY"]:
            return Department.CHEMISTRY.value

        elif value in ["BSc BIOCHEMISTRY", "BIOCHEMISTRY", "BIO CHEMISTRY"]:
            return Department.BIOCHEMISTRY.value

        elif value in ["MATHEMATICS"]:
            return Department.MATHEMATICS.value

        elif value in ["SOFTWARE ENGINEERING", "BSc SOFTWARE ENG", "BSc SOFTWARE"]:
            return Department.SOFTWARE_ENGINEERING.value
        
        elif value in [
            "ACCOUNTING",
            "BSc ACCOUNTING",
            "Bsc Accounting",
        ]:
            return Department.ACCOUNTING.value

        elif value in ["BIOLOGY"]:
            return Department.BIOLOGICAL_SCIENCES.value

        elif value in ["MICROBIOLOGY", "BSc MCB"]:
            return Department.MICROBIOLOGY.value

        elif value in ["IRPM", "BSc IRPM", "Bsc IRPM"]:
            return Department.IRPM.value

        elif value in ["ENGLISH", "BSc ENGLISH", "ENCLISH"]:
            return Department.LANGUAGES.value

        elif value in [
            "CYBER SECURITY",
            "BSc CYBER SECURITY",
            "BSc CYBERSECURITY",
            "BSc CYBER SECURTIY",
            "BSc CYBER SECURITY",
            "CYBER SECURITY",
        ]:
            return Department.CYBER_SECURITY.value

        elif value in [
            "INDUSTRIAL CHEMISTRY",
        ]:
            return Department.INDUSTRIAL_CHEMISTRY.value

        elif value in ["FOOD SCIENCE &TECHNOLOGY", "BSc FOOD SCI TECH", "FST"]:
            return Department.FOOD_SCIENCE.value

        elif value in [
            "PHYSICS WITH ELECTRONICS",
            "PHYSICS",
            "PHYSICS",
            "PHYSICS ",
            "PHYSICS",
        ]:
            
            return Department.PHYSICS.value

        elif value in [
            "FAA",
            "B.A FINE ARTS",
            "FINE ARTS",
            "BSc FINE ARTS",
            "FINE &APPLIED ART",
        ]:
            return Department.FINE_AND_APPLIED_ART.value

        elif value in ["NURSING SCIENCE"]:
            return Department.NURSING_SCIENCE.value

        elif value in [
            "GEOLOGY",
            "GEOPHYSICS",
            "GEOSCIENCE",
            "GEOPHYSICS",
            "GEOSCIENCXE",
            "GEO PHYSICS"
        ]:
            return Department.GEOSCIENCES.value


        elif value in ["LANGUAGE", "LANGUAGES", "LANGUAGE", ]:
            return Department.LANGUAGES.value

        elif value in ["BIOLOGICAL SCIENCE"]:

            return Department.BIOLOGICAL_SCIENCES.value
                     
        elif value in ["BSc TECHNOLOGY", "BIO TECHNOLOGY", "BIOTECHNOLOGY"]:
            return Department.BIOLOGICAL_SCIENCES.value

        elif value in ["MUSIC", "DIP MUSIC", "BSc MUSIC", "MAA"]:
            return Department.MUSIC.value

        elif value in ["BSc COMPUTER SCI", "CSC", "BSc COMPUER SCI",  "BSc COMPUTER", "COMPUTER SCIENCE",]:
            return Department.COMPUTER_SCI.value

        elif value in ["PEL"]:
            return Department.UNKOWN_DEPARTMENT.value
        
        elif value is np.nan:
            return Department.UNKOWN_DEPARTMENT.value
        
        else:
            print(value)
            return value
        


# [400, 100, 200, 300, 'FOUNDATION', 500, nan, 'DIPLOMA']

def resolve_level(value):
    if value in [100, 200, 300, 400, 500]:
        return value
    
    if value in ['FOUNDATION', "FDN"]:
        return 0
    
    if value in ['DIPLOMA']:
        return 1
    

# ['F', 'M', 'FEMALE', nan, 'MALE']
def resolve_gender(value):

    if value in ["F", "FEMALE"]:
        return 1
    
    elif value in ["M", "MALE"]:
        return 0
    
    else:
        return random.choice([0, 1])
    
    