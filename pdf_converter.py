import tabula
from global_vars import *
from pandas import DataFrame

#inspections = tabula.read_pdf(LOCAL_LOCUS_PATH+"/data/whole/dca_files/source/FOIL-2020-866-00276_Inspections_from_2010_to_2017_Dataset_Redacted.pdf", encoding='utf-8', lattice=True ,pages='all')
applications = tabula.read_pdf(LOCAL_LOCUS_PATH+"/data/whole/dca_files/source/Historical_License_Applications_Data_Dataset.pdf", encoding='utf-8', lattice=True ,pages='all')
charges = tabula.read_pdf(LOCAL_LOCUS_PATH+"/data/whole/dca_files/source/FOIL-2020-866-00282_Charges_Dataset (1).pdf", encoding='utf-8', lattice=True ,pages='all')

#inspections=pd.concat(inspections, ignore_index=True)
applications=pd.concat(applications, ignore_index=True)
charges=pd.concat(charges, ignore_index=True)

print([
#inspections,
applications, charges])

#inspections.to_pkl(LOCAL_LOCUS_PATH+"/data/whole/dca_files/inspections_base.pkl")
applications.to_pkl(LOCAL_LOCUS_PATH+"/data/whole/dca_files/applications_base.csv")
charges.to_pkl(LOCAL_LOCUS_PATH+"/data/whole/dca_files/charges_base.csv")
