#Calculadora de ahorro
datos = {
"ingresos": 2500,
"comida": 500,
"transporte": 250,
"entretenimiento": 300,
"otros": 150,
"ahorro": 600
}
#Debe devolver: gasto total, ahorro, dinero restante, porcentaje gastado, categoría mas cara, numero de categorias de gasto

def reporte_financiero(datos):
    gasto_tot = 0    
    for a,z in datos.items():
        if a != "ahorro" and a != "ingresos":
            gasto_tot += z  
    ahorro = datos["ahorro"]
    dinero_rest = datos["ingresos"] - gasto_tot - ahorro
    porc_gast = ((gasto_tot)/datos["ingresos"])*100
    mayor= 0
    cat_cara = "comida"
    for b,c in datos.items():
        if b != "ingresos" and b != "ahorro":
            if c > mayor:
                mayor = c
                cat_cara = b
    lista = [ ]
    for d in datos.keys():
        if d != "ingresos" and d!= "ahorro":
            lista.append(d)
    num_cats = len(lista)
    return {
        "Gasto_total": gasto_tot,
        "Ahorro" : ahorro,
        "Dinero_restante": dinero_rest,
        "Porcentaje_gastado": porc_gast,
        "Categoría_más_cara": cat_cara,
        "Número_de_categórias_de_gasto": num_cats
    }    
resultado = reporte_financiero(datos)
print(resultado)

def valor_real_ahorro(ahorro,inflación,años):
    ahorro_i = ahorro
    ahorro_f = ahorro
    for a in range(años):
        ahorro_f = ahorro_f - ahorro_f*inflación
    pérdida = ahorro_i - ahorro_f
    porcent = (pérdida/ahorro_i)*100
    return {
        "Ahorro_inicial": ahorro_i,
        "Valor_real_final": ahorro_f,
        "Pérdida_de_poder_adquisitivo": pérdida,
        "Porcentaje_perdido": porcent
    }
resultado1 = valor_real_ahorro(datos["ahorro"], 0.04, 5 )
print(resultado1)