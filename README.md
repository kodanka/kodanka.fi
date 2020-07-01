
# kodanka

![](https://github.com/kodanka/kodanka.fi/workflows/Deploy%20site/badge.svg)
[![CC BY-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

<img src="_static/logo.png" width="100">

## Licens

Materialet delas under [Creative Commons 4.0 BY-NC-SA][cc-by-nc-sa]

[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Utveckla

### Installera paket

```
conda install -c conda-forge jupyterlab
conda install -c anaconda beautifulsoup4
conda install -c conda-forge nbsphinx
conda install sphinx_rtd_theme
```

### Producera material

```
jupyter lab
```

### Testa sidan

```
make build
```

## Logo

Vi valde en anka som symbol av tre orsaker

- Ankor är lustiga
- [Ankor kan hjälpa med kodning](https://sv.wikipedia.org/wiki/Fels%C3%B6kning_i_kod_med_hj%C3%A4lp_av_gummianka)
- Finlandssvenskarna utgör en ankdam

Källa: [pngimg.com](https://pngimg.com/download/45750) under licensen [Creative Commons 4.0 BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)

## Stoppord

[stoppord.txt](_static/stoppord.txt) från [stopwords-iso](https://github.com/stopwords-iso/stopwords-sv) under [MIT Licens](https://opensource.org/licenses/MIT)