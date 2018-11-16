# Factorial-Dataset
> Factorial data to make your applications more fast with pre-calculated factorials

> Attention: The 5º term is not rounded in the factorials above 170.

[![NPM Version][npm-image]][npm-url]


## Use example
```
fatorialData = {
1:1,
2:2,
3:6,
4:24,
5:120,
6:720,
7:5040,
8:40320,
9:362880,
.
.
.
168:2.52608E+302,
169:4.26907E+304,
170:7.25742E+306,
}
```
```
def fatorial(n):
    if n >= 171:
        print("[!] Valor de Fatorial muito grande.")
        print("[!] Abortando o programa.")
        sys.exit("Ate logo!")
    return(fatorialData[n])
```

## Histórico

* 0.1.1
    * Adicionado data-set contendo o fatorial como string.
* 0.1.0
    * Alteração de `[E]([\d]+) para E+$1 (regex)`
* 0.0.1
    * Trabalho em andamento

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/seunome/seuprojeto/wiki
