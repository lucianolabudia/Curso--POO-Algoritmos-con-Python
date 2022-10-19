from bokeh.plotting import figure, output_file, show
# figure: Ventana donde se grafica
#  output_file: Cual es el nombre del archivo que se genera como output
# show: genera un servidor que se prende y muestra el archivo

if __name__ == '__main__':

    output_file('graficado_simple.html') #nombre archivo de salida
    fig = figure() #genera figura

    total_valores = int(input('Cuantos valores quieres graficar? '))
    x_valores = list(range(total_valores)) #generamos automaticamente una secuencia de numeros empezando en 0
    y_valores = [] #generamos una lista vacia de las Y

    for x in x_valores:
        valor = int(input(f'Valor Y para {x}: ')) #generamos una Y por cada valor de X
        y_valores.append(valor)

    fig.line(x_valores, y_valores, line_width=2) #los datos se pasan a la figura
    show(fig) #muestra la figura