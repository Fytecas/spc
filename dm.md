***Le Hy Dario***

**DM de Physique-Chimie**

# A la quête des diodes de toutes les couleurs

## Questions

1. D'après dans le document 2, les matériaux phosphorescents / fluorescents, après avoir absorbé un photon (en l'occurence un photon bleu), s'excitent puis se désexcitent (instanément pour les matériaux fluorescents, cela peut prendre plus ou moins de temps pour les matériaux phosphorescents ). Cette désexitation se fait en passant par plusieurs niveaux d'énergie intermédiaires, chacun emettant un photon propre à son niveau d'énergie. Cela permet d'émettre des photons de longueurs d'ondes différentes de ceux absorbés. Cette désexitation en plusieurs "étages" est donc appelée désexitation en cascade, car le matériaux passe par plusieurs niveaux d'énergie consecutifs lors de la désexitation.

2. Selon le document 2, les led "blanches" ici représentées sont composées d'une led bleue recouverte d'un matériaux fluorescent qui absorbe une partie des photons bleus et ré-émet des photons jaunes. Par lecture graphique sur le document 3, le premier pic, d'une valeur d'environ $440nm$, correspond à la lumière émise par la led bleu et le second, d'une valeur d'environ $595nm$ correspond à la lumière jaune émise par le matériaux phosphorescent.

3. On cherche les valeurs des niveaux d'énergie $E_1$ et $E_1'$ du matériaux fluorescent.

On Pose:

- $h = 6,63\cdot10^{-34}J\cdot s$ étant la constante de Planck

- $c = 3,00\cdot10^{8} m\cdot s^{-1}$ étant la vitesse de la lumière dans le vide

- $1eV = 1,60\cdot10^{-19}J$

Par lecture graphique du document 3:

 - $\lambda_{bleu} = 440nm = 4,40\cdot10^{-7}m$ (correspond à la longueur d'onde du premier pic)

 - $\lambda_{jaune} = 595nm = 5,95\cdot10^{-7}m$ (correspond à la longueur d'onde du second pic)


On peut associer les valeurs de ces deux pics d'émissions aux niveaux d'énergie du matériaux fluorescent. Comme dit dans la question deux, sur le doc. 3 le pic d'émission à 440 nm (bleu) correspond, selon le doc. 2, à l'énergie absorbée par le matériau pour la transition $E_0 \rightarrow E_1$. Le pic à 595 nm (jaune) correspond à l'énergie libérée lors de la désexcitation $E_1' \rightarrow E_0$ (selon le doc. 4).

On sait que $\nu = {c\over\lambda}$

On calcule la fréquence des photons émis par le pic jaune et le pic bleu:

$\nu_{bleu}=\frac{c}{\lambda_{bleu}} =\frac{3,00\cdot10^8m\cdot s^{-1}}{4,40\cdot10^{-7}m}\approx6,82\cdot10^{14}Hz$

$\nu_{jaune}=\frac{c}{\lambda_{jaune}} =\frac{3,00\cdot10^8m\cdot s^{-1}}{5,95\cdot10^{-7}m}\approx5,04\cdot10^{14}Hz$

On sait que $E = h\nu$

On pose $E_0 = 0eV$

On calcule les valeurs des niveaux d'énergie $E_1$ et $E_1'$ en fonction du niveau fondamental $E_0$, en sachant que $E_1$ est lié à l'absorbtion d'un photon de fréquence $\nu_{bleu}$ et que $E_1'$ est lié à l'émission d'un photon de fréquence $\nu_{jaune}$:

$E_1 = \nu_{bleu} \cdot h - E_0= 6,82\cdot10^{14} \cdot 6,63\cdot10^{-34} - 0\approx 4,52\cdot10^{-19} J = \frac{4,52\cdot10^{-19}}{1,60\cdot10^{-19}} eV \approx 2,83eV$

$E_1' = \nu_{jaune} \cdot h - E_0= 5,04\cdot10^{14} \cdot 6,63\cdot10^{-34} - 0\approx 3,34\cdot10^{-19} J = \frac{3,34\cdot10^{-19}}{1,60\cdot10^{-19}} eV \approx 2,09eV$

Donc le niveau d'énergie $E_1$ a une valeur d'environ $2,83eV$ et le niveau d'énergie $E_1'$ une valeur d'environ $2,09eV$.

4. On cherche à calculer la longueur d’onde du photon I-R émis lors de la désexcitation $E_1 \rightarrow E_1'$ :

On calcule la différence entre les valeurs d'énergie $E_1$ et $E_1'$ : $\Delta_{E_1E_1'} = E_1 - E_1' = 4,52\cdot10^{-19} J - 3,34\cdot10^{-19} J= 1,18\cdot10^{-19} J$

A partir de $\Delta_{E_1E_1'}$, on peut donc calculer la fréquence du photon émis lors de la désexitation de $E_1$ à $E_1'$:

On a: $E = h\nu \iff \nu = \frac{E}{h}$

Donc $\nu_{emis} = \frac{\Delta_{E_1E_1'}J}{h} = \frac{1,18\cdot10^{-19}}{6,63\cdot10^{-34}J\cdot s} \approx 1,78\cdot10^{14}Hz$

On convertit cette fréquence en longueur d'onde:

On a: $\nu = \frac{c}{\lambda} \iff \lambda = \frac{c}{\nu}$

Donc $\lambda_{emis} = \frac{c}{\nu_{emis}} = \frac{3,00\cdot10^{8}}{1,78\cdot10^{14}} \approx 1.69 \cdot 10^{-6} m \approx 1690 nm$

Donc la longueur d’onde du photon I-R émis lors de la désexcitation $E_1 \rightarrow E_1'$ est d'environ 1690 nm.

5.

Sur le document 4 on voit que les spectres d'émissions des lampes à filament chauffé (halogène et classique) s'étendent largement au-delà du visible, dans le domaine de l'infrarouge. Ces lampes sont donc très peu efficientes car la majorité de l'énergie y est transformée en rayonnement infrarouge.

Sur le document 3 on voit le spectre d'émission d'une LED blanche. Ici l'émission se concentre dans le visible (bien que, comme vu dans les questions précédentes, de l'infrarouge soit émis, cette émission est minime par rapport à celle d'une lampe à incandescence). Une plus grande partie de l'énergie y est donc transformé en lumière visible. Les LEDs sont donc plus efficientes, et donc plus économes que les lampes à filament chauffé.

## Conclusion

Pour percevoir les couleurs, l'homme dispose dans son œil de cônes de reception du rouge, de cônes de réception du vert et de cônes de réception du bleu.
Il est donc possible de produire une lumière de n'importe quelle couleur avec une lampe rouge, une lampe bleue et une lampe verte. Il suffit ensuite de modifier leur intensité à chacune pour obtenir la couleur recherchée.

Pour la création d'un écran couleur il faut pouvoir mettre ces trois lampes dans chaque pixel. Le but est donc de trouver des dispositifs capables d'émettre une longueur d'onde (couleur) précise, qui puisse être miniaturisé et qui soit assez efficient pour pouvoir en mettre beaucoup sur un espace restreint.
Les lampes à incandescence sont donc exclues, car difficilement "miniaturisable" et très peu économe en énergie (dû à leur spectre d'émission très étendu dans les infrarouges).
Les LEDs, plus économes en énergie et très "miniaturisables", sont plus adaptées à cet usage. Les LEDs rouges et verte furent très vite développées, mais il fallût plus de temps pour développer les LEDs bleues.

La technique de l’émission en cascade ne permet pas non plus de créer de la lumière bleue à partir de rouge ou de vert. En effet celle-ci ne permet que la désexitation par paliers de valeur d'énergie inférieurs au niveau d'énergie atteint lors de l'excitation. La lumière émise a donc fréquence inférieure (et donc un longueur d'onde supérieure) à celle de la lumière absorbée. Or le bleu a une longueur d'onde inférieure au rouge ou au vert. Cette technique n'est donc pas une option pour la création de leds bleues.

Avant le développement des LEDs bleues, la création des écrans couleurs ne pouvait donc être envisagée car le bleu est une couleur nécessaire à la reproduction des autres couleurs selon le modèle trichromatique.
