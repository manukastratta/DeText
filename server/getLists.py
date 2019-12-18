import xlrd 

# Parses through excel sheet and extracts data
# Returns list of words and phrases
def getList(fileName):
    raw_list = []
    wb = xlrd.open_workbook(fileName) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
    
    for i in range(sheet.nrows): 
        raw_list.append(str(sheet.cell_value(i, 0)))
    return raw_list
     
def getImplicitList():
    implicit_list = getList("./trainingSets/implicit.xlsx")
    implicit_list = list(set(implicit_list))  # remove duplicates
    return implicit_list

def getExplicitList():
    explicit_list = getList("./trainingSets/explicit.xlsx")
    explicit_list = list(set(explicit_list))  # remove duplicates
    return explicit_list