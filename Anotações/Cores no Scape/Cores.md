# Cores no Terminal:
## Código ANSI
- Escape sequence
- São opcionais os valores.
- Sintaxe:
```
\033[_Estilo_Texto_Background_m
```

````puthon
print('\033[1:31:43mPokémon\033[m')
```
### Style(São quatro estilos):
- 0 -> Nada.
- 1 -> Negrito.
- 4 -> Sublinhar.
- 7 -> inversão.

### Text(Cores para o texto):
- Cor (Branco) -> 30 
- Cor (Rosa) -> 31 
- Cor (Verde) -> 32
- Cor (Amarelo) -> 33
- Cor (Azul) -> 34 
- Cor (Roxo) -> 35 
- Cor (Azul claro) -> 36
- Cor (Cinza) -> 37
- Cor (Vemelho) -> 91
### Back(Fundo):
- Cor (Branco) -> 40 
- Cor (Vermelho) -> 41 
- Cor (Verde) -> 42
- Cor (Amarelo) -> 43
- Cor (Azul) -> 44 
- Cor (Roxo) -> 45 
- Cor (Azul claro) -> 46
- Cor (Cinza) -> 47