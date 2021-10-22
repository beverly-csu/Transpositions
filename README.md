<br/>
<p align="center">
  <h3 align="center">Transpositions</h3>

  <p align="center">
    Перемножение и возведение в степень подстановок.
    <br/>
    <br/>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/beverly-csu/Transpositions/total) ![Contributors](https://img.shields.io/github/contributors/beverly-csu/Transpositions?color=dark-green) ![Issues](https://img.shields.io/github/issues/beverly-csu/Transpositions) ![License](https://img.shields.io/github/license/beverly-csu/Transpositions) 

## About The Project

Существует два режима работы программы:
1. multi - перемножение двух заданных циклов
2. exp - возведение в степень n заданного цикла

## Getting Started

Для успешной работы программы необходимо наличие рядом с transpositions.py файла ex.txt, в котором в правильном формате будут указаны данные.

## Usage

Файл ex.txt должен выглядеть по разному для разных режимов.
Если необходимо перемножить два цикла, то в первую строчку файла ex.txt должен быть написан режим multi, во второй и третьей строках должны быть написаны циклы.
<b>Пример:</b><br>
multi<br>
( 1 12 20 19 18 ) ( 2 ) ( 3 15 13 10 16 9 17 5 6 14 7 ) ( 4 ) ( 8 ) ( 11 )<br>
( 1 11 8 14 18 7 5 2 17 3 20 19 13 9 ) ( 4 16 6 ) ( 10 15 ) ( 12 )<br>
Если необходимо возвести в n-ую степень цикл то необходимо записать в файле режим exp, во второй строке цикл, а в третьей строке любую цифру.
<b>Пример:</b><br>
exp<br>
( 1 12 20 19 18 ) ( 2 ) ( 3 15 13 10 16 9 17 5 6 14 7 ) ( 4 ) ( 8 ) ( 11 )<br>
10<br>

## Authors

* **beverly-csu** - ** - [beverly-csu]() - **
