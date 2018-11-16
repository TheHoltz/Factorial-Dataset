# Factorial-Dataset
> Factorial data to make your applications more fast with pre-calculated factorials
> Attention: The 5º term is not rounded in the factorials above 170.

[![NPM Version][npm-image]][npm-url]


## Exemplo de uso

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
   10:3628800,
   11:39916800,
   12:479001600,
   13:6227020800,
   14:87178291200,
   15:1307674368000,
   16:20922789888000,
   17:355687428096000,
   .
   .
   .
   }

   def fatorial(n):
       if n >= 171:
           print("[!] Valor de Fatorial muito grande.")
           print("[!] Abortando o programa.")
           sys.exit("Ate logo!")
       return(fatorialData[n])

## Histórico de lançamentos

* 0.1.0
    * Alteração de E^[\d] para e^[+\d]
* 0.0.1
    * Trabalho em andamento

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/seunome/seuprojeto/wiki
