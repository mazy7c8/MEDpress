# MEDpress

Open source project for healthcare workers to simplify medical descriptions


## Homepage

[https://mazy7c8.github.io/medpress.docs/](https://mazy7c8.github.io/medpress.docs/)



## Description

Project was inspired by the Emergency Department personel of local hospital. The idea was to make a tool to help doctors or other medical workers boost they workflow with making papers with different parts like epicrisis. The program was needed to be simple just to run it on the different machines with different user situations like unability to install new programs to their machines so it must can be taken on a pendrive for example and run on different machines. The templates must be stored in easy to read files to make them shareable among users and easy to edit if needed. There is manual and more examples on a homepage of a project. The project is looking for recognize among users so the next goal is to make a cloud solution for sharing a templates among users.


Projekt dla poznańskiego SOR szpitala , ma przyspieszać pracę i jednocześnie ustandaryzować wypisy lekarskie głównie ich część specyficzną tzw epikryze. Program ma być połączeniem dwóch przykładowych wzroców użycia, jednak pozbawionym komercyjnej i zbędnej programistycznej nadbudowy. . Projekt jest oparty o idee projektu społecznościowego. Celem aplikacji jest przyjęcie się i upowrzechnienie w środowisku medyków w obrębie jednej lub więcej placówek. Program z założenia ma być prosty i jego celem ma być działanie w trybie portable. Strona projektu ma udostępniać instrukcje na temat działania programu tak aby każdy mógł zacząć korzystać z narzędzia i "dostrajać je" wg swojego zapotrzebowania. W wersji końcowej jest zaplanowane stworzenie systemu bazodanowego online przechowującego tzw. formularze.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip3 install -r requirents.txt
```

use [cxFreeze](https://pypi.org/project/cx-Freeze/) to make executable for Windows, Linux or macOS in located in /build or download already created a zip build from homepage

```bash
python3 setupfreeze.py build
```

## Usage

If you want to run project from the source code just

```python
python3 main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Project is now waiting for test users and feedback to get pushed for new releases

## Support

My active email is rafalinz at gmail dot com

## License

[MIT](https://choosealicense.com/licenses/mit/)
