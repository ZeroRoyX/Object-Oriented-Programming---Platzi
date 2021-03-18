# from bokeh.plotting import figure, output_file, show
# from datetime import date, timedelta

# # if __name__ == '__main__':
# #     output_file('graficado_simple.html')
# #     fig = figure()
# #     # type(fig)
# #     # help(fig)

# #     # total_values = int(input('¿Cuántos valores quieres graficar?: '))
# #     x_values = [i for i in range(-3, 4)]
# #     y_values = [i**3 for i in x_values]

# #     # y_values = [int(input(f'Valor "Y" para {i}: ')) for i in x_values]
    
# #     fig.line(x_values, y_values, line_width = 2)
# #     show(fig)


# if __name__ == '__main__':
#     output_file('graficado_simple.html')
#     fig = figure()
#     # print(type(fig))
#     # help(fig)

#     # total_values = int(input('¿Cuántos valores quieres graficar?: '))
#     x_values = [i for i in range(11, 18)]
#     y_values = [20.7133, 20.7637, 20.7637, 20.7637, 20.7637, 20.5753, 20.6828]

#     # y_values = [int(input(f'Valor "Y" para {i}: ')) for i in x_values]
    
#     fig.line(x_values, y_values, line_width = 2)
#     # show(fig)

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':

    output_file('graficado2.html')
    fig = figure()

    total_values = int(input('¿Cuántos valores quieres graficar?: '))
    x_values = [i for i in range(total_values)]
    y_values = [int(input(f'Valor de "Y" para {i}: ')) for i in x_values]

    fig.line(x_values, y_values, line_width = 3)
    show(fig)