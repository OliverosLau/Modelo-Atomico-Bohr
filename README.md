# Modelo Atómico de Bohr

## Cálculo de los Niveles de Energía del Electrón en el Átomo de Hidrógeno

### Introducción

El átomo de hidrógeno es el más simple de todos los átomos, compuesto por un protón en el núcleo y un electrón que lo orbita. La descripción clásica de este átomo fue dada por el modelo de Bohr, pero en la mecánica cuántica, la descripción correcta se obtiene a través de la **ecuación de Schrödinger**. Esta ecuación permite calcular los **niveles de energía** permitidos para el electrón y da lugar a la estructura cuántica del átomo.

### 1. Ecuación de Schrödinger

La **ecuación de Schrödinger** independiente del tiempo para un electrón en un potencial es:

$$
\hat{H} \psi = E \psi
$$

donde:
- \( \hat{H} \) es el **Hamiltoniano**, que representa la energía total del sistema.
- \( \psi \) es la **función de onda**, que contiene toda la información sobre el estado cuántico del sistema.
- \( E \) es la **energía** asociada al estado cuántico.

Para el átomo de hidrógeno, el Hamiltoniano consta de dos partes:
1. **Energía cinética** del electrón:
   \[
   \hat{T} = - \frac{\hbar^2}{2m} \nabla^2
   \]
2. **Energía potencial** debido a la interacción electrostática entre el electrón y el protón (potencial de Coulomb):
   \[
   V(r) = - \frac{e^2}{4 \pi \epsilon_0 r}
   \]

Sustituyendo ambas en la ecuación de Schrödinger, obtenemos:

$$
\left( - \frac{\hbar^2}{2m} \nabla^2 - \frac{e^2}{4 \pi \epsilon_0 r} \right) \psi = E \psi
$$

### 2. Coordenadas esféricas y separación de variables

Dado que el potencial solo depende de la distancia radial \( r \), es conveniente resolver la ecuación en **coordenadas esféricas** \((r, \theta, \phi)\). El operador Laplaciano en estas coordenadas es:

$$
\nabla^2 = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right) + \frac{1}{r^2 \sin \theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial}{\partial \theta} \right) + \frac{1}{r^2 \sin^2 \theta} \frac{\partial^2}{\partial \phi^2}
$$

Para resolver la ecuación de Schrödinger en estas coordenadas, aplicamos el método de **separación de variables**, suponiendo que la función de onda puede escribirse como el producto de una función radial \( R(r) \) y una función angular \( Y(\theta, \phi) \):

$$
\psi(r, \theta, \phi) = R(r) Y(\theta, \phi)
$$

#### 2.1. Parte angular

La parte angular se resuelve usando los **armónicos esféricos** \( Y(\theta, \phi) \), que son funciones bien conocidas y dependen de los números cuánticos \( l \) (momento angular) y \( m_l \) (proyección del momento angular). La solución angular no afecta a la cuantización de la energía.

#### 2.2. Parte radial

La parte radial de la ecuación de Schrödinger toma la forma:

$$
\frac{d}{dr} \left( r^2 \frac{dR(r)}{dr} \right) - \frac{2mr^2}{\hbar^2} \left( \frac{e^2}{4\pi \epsilon_0 r} + E \right) R(r) + l(l+1) R(r) = 0
$$

donde \( l \) es el número cuántico asociado al momento angular. Esta ecuación se resuelve imponiendo que \( R(r) \) sea finita y normalizable, lo que lleva a la **cuantización de la energía**.

### 3. Cuantización de la energía

La solución de la ecuación radial nos da los **niveles de energía** permitidos para el electrón. Estos niveles están cuantizados y dados por:

\[
E_n = - \frac{13.6 \, \text{eV}}{n^2}
\]

donde:
- \( n \) es el **número cuántico principal**, que puede tomar valores enteros \( n = 1, 2, 3, \dots \).
- \( 13.6 \, \text{eV} \) es la energía del estado fundamental (cuando \( n = 1 \)).

#### 3.1. Interpretación física

- Para \( n = 1 \), el electrón está en el **estado fundamental** con una energía de \( -13.6 \, \text{eV} \).
- Para \( n = 2 \), la energía es \( -3.4 \, \text{eV} \) (primer estado excitado).
- Para \( n = 3 \), la energía es \( -1.51 \, \text{eV} \), y así sucesivamente.

El valor negativo de la energía refleja que el electrón está **ligado** al núcleo; se requiere energía para ionizarlo (liberarlo del átomo).

### 4. Números cuánticos

Además del número cuántico principal \( n \), existen otros números cuánticos que describen completamente el estado del electrón:

- **Número cuántico principal** \( n \): Determina el nivel de energía y el tamaño del orbital.
- **Número cuántico del momento angular** \( l \): Determina la forma del orbital y puede tomar valores \( l = 0, 1, 2, \dots, n-1 \).
- **Número cuántico magnético** \( m_l \): Describe la orientación del orbital en el espacio, con valores \( m_l = -l, -(l-1), \dots, l \).
- **Número cuántico de espín** \( m_s \): Asociado al espín del electrón, puede ser \( +\frac{1}{2} \) o \( -\frac{1}{2} \).

### 5. Transiciones entre niveles de energía

Cuando un electrón pasa de un nivel de energía a otro, emite o absorbe un **fotón** cuya energía corresponde a la diferencia entre los niveles:

\[
E_\text{fotón} = E_{n_2} - E_{n_1}
\]

Esto explica las **líneas espectrales** del hidrógeno observadas en experimentos, donde las frecuencias de la luz emitida o absorbida corresponden a las transiciones entre niveles de energía cuantizados.
