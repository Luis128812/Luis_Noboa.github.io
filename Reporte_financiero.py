
# Programa que analice un diccionario que contenga gastos y presupuestos

gastos = [{ "categoria" : "comida" ,"monto" :520},
          {"categoria" : "transporte" ,"monto" :180},
          {"categoria" : "ocio" ,"monto" :240} ,
          {"categoria" : "internet" ,"monto" :60} ,
          {"categoria" : "ropa" ,"monto" :160}]
ingreso = 1800
presupuesto = {
"comida" :600,
"transporte" :250,
"ocio" :200,
"internet" :80,
"ropa" :150
}
def analisis_completo(gastos,ingreso):
    gasto_tot=0
    for gasto in gastos:
        gasto_tot += gasto["monto"]
    dinero_rest=ingreso - gasto_tot
    cat_mayor= gastos[0]["categoria"]
    valor_mayor=gastos[0]["monto"]
    for a in gastos:
        if a["monto"]>valor_mayor:
            cat_mayor=a["categoria"]
            valor_mayor=a["monto"]
    d=[]
    for b in gastos:
        d.append((b["categoria"],round((b["monto"]/ingreso)*100,2)))
    cat_consume_mas=gastos[0]["categoria"]
    porcentaje=(gastos[0]["monto"]/ingreso)*100
    for c in gastos:
        porcent=(c["monto"]/ingreso)*100
        if porcent>porcentaje:
            cat_consume_mas=c["categoria"]
            porcentaje=porcent  
    return {"Ingreso":ingreso,"Gasto_total": gasto_tot, "Dinero_restante":dinero_rest,"Cat_mayor":cat_mayor, "Valor_mayor":valor_mayor, "porcentajes": d,"porcentaje_alto": cat_consume_mas}
resultado=analisis_completo(gastos,ingreso)
print("========== REPORTE FINANCIERO ==========")
print()
print("Ingreso:            $", resultado["Ingreso"])
print("Gasto total:        $", resultado["Gasto_total"])
print("Dinero restante:    $", resultado["Dinero_restante"])
print()
print("Mayor gasto")
print(f"{resultado['Cat_mayor'].capitalize()} --> ${resultado['Valor_mayor']}")
print()
print("Porcentajes")     
for categoria, porcentaje in resultado["porcentajes"]:
    print(categoria.capitalize(), "-->", porcentaje, "%")
print()
# Generdor de aletras de presupuesto
print("==========ALERTAS DE PRESUPUESTO==========")
print()
for gasto in gastos:
    if gasto["monto"]> presupuesto[gasto["categoria"]]:
        print(f"{gasto['categoria'].capitalize()} supera el presupuesto")
    elif gasto["monto"]<= presupuesto[gasto["categoria"]]:
        print(f"{gasto['categoria'].capitalize()} está dentro del presupuesto")

