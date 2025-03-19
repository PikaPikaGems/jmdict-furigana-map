# JMdict Furigana Map

Generates a JSON file that maps Japanese words from JMdict to furigana.

## Usage

### Requirements

Python 3.x:

```bash
python --version
# Python 3.13.2
```

Input file:

Download the latest `JmdictFurigana.json` from the [JmdictFurigana project][jmdictfurigana]
and save it in the `input` directory.

```bash
curl --output-dir input -OL https://github.com/Doublevil/JmdictFurigana/releases/latest/download/JmdictFurigana.json
```

### Running the program

In your terminal, run:

```bash
./src/main.py
```

A new `jmdict-furigana-map.json` should be generated in the `output` directory, and its
compressed archive file in the `releases` directory.

## License

The software is distributed under the [MIT License][mit-license].

The releases which contain the jmdict-furigana-map.json file by Michael Galero is licensed
under [CC BY-SA 4.0][cc-by-sa-4].

## Credits

This project uses the JmdictFurigana.json from the [JmdictFurigana project][jmdictfurigana]
by [@Doublevil](https://github.com/Doublevil) that is licensed under [CC BY-SA 4.0][cc-by-sa-4].

Doublevil's JmdictFurigana project uses the [JMdict/EDICT][jmdict-edict] file, which is the
property of the Electronic Dictionary Research and Development Group (https://www.edrdg.org/),
and used in conformance with the Group's [license](https://www.edrdg.org/edrdg/licence.html).

[jmdictfurigana]: https://github.com/Doublevil/JmdictFurigana
[mit-license]: https://github.com/PikaPikaGems/jmdict-furigana-map/blob/main/LICENSE
[cc-by-sa-4]: https://creativecommons.org/licenses/by-sa/4.0
[jmdict-edict]: https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project
