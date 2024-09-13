# Unidades de Medida en CSS

En CSS, existen diferentes unidades de medida que se utilizan para definir el tamaño, espacio y posicionamiento de los elementos. Aquí  una tabla con las más comunes:

| Unidad | Descripción                               | Ejemplo |
|--------|-------------------------------------------|---------|
| px     | Píxeles. Unidad fija que no depende del tamaño de la pantalla o ventana. | `font-size: 16px;` |
| %      | Porcentaje. Basado en el tamaño del elemento padre.                        | `width: 50%;`      |
| em     | Relativa al tamaño de la fuente del elemento padre.                       | `padding: 2em;`    |
| rem    | Relativa al tamaño de la fuente raíz (`html`).                            | `margin: 1.5rem;`  |
| vw     | Viewport Width. 1vw equivale al 1% del ancho de la ventana del navegador.  | `width: 50vw;`     |
| vh     | Viewport Height. 1vh equivale al 1% de la altura de la ventana del navegador. | `height: 100vh;`   |
| vmin   | El menor valor entre el ancho (`vw`) y la altura (`vh`) del viewport.     | `width: 20vmin;`   |
| vmax   | El mayor valor entre el ancho (`vw`) y la altura (`vh`) del viewport.     | `width: 50vmax;`   |
| ch     | El ancho de un carácter "0" en la fuente utilizada.                      | `width: 30ch;`     |
| ex     | La altura de la "x" minúscula en la fuente utilizada.                     | `line-height: 1ex;`|
| fr     | Fracción. Se usa en los **grids** para definir proporciones relativas.    | `grid-template-columns: 1fr 2fr;` |

Estas unidades permiten flexibilidad y control sobre el diseño en distintas resoluciones y dispositivos.
