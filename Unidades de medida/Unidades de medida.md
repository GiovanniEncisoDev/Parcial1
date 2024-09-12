# Unidades de Medida en CSS

En CSS, se utilizan diferentes unidades para definir el tamaño, la longitud, el espacio y otros aspectos relacionados con el diseño. Estas unidades pueden dividirse en dos categorías principales: **unidades absolutas** y **unidades relativas**.

## 1. Unidades Absolutas

Las unidades absolutas tienen valores fijos que no dependen del contexto, lo que significa que no varían según el tamaño de la pantalla o el contenedor. Se utilizan cuando se desea tener un control preciso sobre las dimensiones de los elementos.

| Unidad | Descripción                       | Equivalencia     |
|--------|-----------------------------------|------------------|
| `cm`   | Centímetros                       | 1cm = 37.8px     |
| `mm`   | Milímetros                        | 1mm = 0.1cm      |
| `in`   | Pulgadas                          | 1in = 96px       |
| `px`   | Píxeles                           | 1px = 1/96 pulgadas |
| `pt`   | Puntos                            | 1pt = 1/72 pulgadas |
| `pc`   | Picas                             | 1pc = 12pt       |

> **Nota:** Las unidades absolutas son útiles para medios impresos, pero pueden no ser adecuadas para pantallas debido a la variabilidad de tamaños y resoluciones.

## 2. Unidades Relativas

Las unidades relativas se basan en el tamaño de otros elementos o el contenedor, y se ajustan automáticamente dependiendo del entorno en el que se utilicen. Son más flexibles y comunes en el diseño web responsivo.

### 2.1 Unidades Relativas a la Fuente
Estas unidades dependen del tamaño de la fuente.

| Unidad | Descripción                                    |
|--------|------------------------------------------------|
| `em`   | Relativa al tamaño de la fuente del elemento padre. 1em equivale al tamaño de la fuente actual. |
| `rem`  | Relativa al tamaño de la fuente raíz (`html`). 1rem equivale al tamaño de la fuente del elemento raíz. |

> **Ejemplo:** Si la fuente raíz es de 16px, entonces `1rem = 16px`.

### 2.2 Unidades Relativas a la Vista
Estas unidades dependen del tamaño de la ventana o el área visible del navegador.

| Unidad  | Descripción                                              |
|---------|----------------------------------------------------------|
| `vw`    | Relativa al 1% del ancho de la ventana.                  |
| `vh`    | Relativa al 1% de la altura de la ventana.               |
| `vmin`  | Relativa al 1% de la dimensión menor (ancho o altura).   |
| `vmax`  | Relativa al 1% de la dimensión mayor (ancho o altura).   |

> **Ejemplo:** Si la altura de la ventana es 1000px, entonces `1vh = 10px`.

### 2.3 Otras Unidades Relativas

| Unidad  | Descripción                                                     |
|---------|-----------------------------------------------------------------|
| `%`     | Porcentaje relativo al tamaño del elemento contenedor.          |
| `ex`    | Relativa a la altura de la letra "x" de la fuente.              |
| `ch`    | Relativa al ancho del carácter "0" en la fuente actual.         |

## 3. Uso de Unidades en CSS

A continuación, se muestra un ejemplo de cómo se utilizan algunas de estas unidades en CSS:

```css
body {
    font-size: 16px; /* Tamaño de fuente base */
}

h1 {
    font-size: 2rem; /* 2 veces el tamaño de la fuente raíz */
}

.container {
    width: 80vw; /* 80% del ancho de la ventana */
    height: 50vh; /* 50% de la altura de la ventana */
}

.box {
    padding: 1em; /* Igual al tamaño de la fuente del contenedor padre */
}
