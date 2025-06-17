## locale
- A biblioteca locale do Python é utilizada para internacionalização, permitindo adaptar programas para diferentes configurações regionais, como formatação de números, moedas, datas e textos. 
- ```import locale```

> locale.setlocale(category, locale): Define a localidade para uma categoria específica (como números, datas, etc.). Exemplo: locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8').
- Pode-se omitir, pois irá incluir os dados segundo ao SO.

>locale.getlocale(category): Retorna a localidade atual para uma categoria. Exemplo: locale.getlocale(locale.LC_MONETARY).



>locale.localeconv(): Retorna um dicionário com as convenções de formatação numérica e monetária da localidade atual.


>locale.format_string(format, val, grouping=False): Formata números de acordo com a localidade. Exemplo: locale.format_string('%.2f', 12345.678, grouping=True).


>locale.strxfrm(string): Transforma uma string para comparação de acordo com as regras da localidade, útil para ordenação correta de textos.