# Import Module 
import tabula
  
# Read PDF File
# this contain a list
tabula.convert_into("NORTHERN JUPITER LOAD SEQ SHEET.pdf", "AlternativeMethod.csv", output_format="csv", pages="all")
  
# Convert into Excel File
#df.to_excel('AlternativeMethod.xlsx')