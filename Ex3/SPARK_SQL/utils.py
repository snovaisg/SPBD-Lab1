def fillaffected(inj,death,affected):
    if float(affected)<float(inj)+float(death):
        affected=float(inj)+float(death)
    return affected

def fillnan(x):
    if x=="":
        return 0
    else:
        return x