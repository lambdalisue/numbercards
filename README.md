numbercards
=============================================================================

numbercards is a simple program.
It just create simple number cards which you might see often on posters found
in some scientific conference.

Requirements
-----------------------------------------------------------------------------

-   [Python][]
-   [reportlab][]

[Python]: http://www.python.org/
[reportlab]: http://www.reportlab.com/software/opensource/


Install
-----------------------------------------------------------------------------

1.  You have to install [Python][]. Follow the instruction at
    http://www.python.org/getit/

2.  Now, you can install numbercards with [pip][] or [easy_install][].
    [reportlab][] will be installed automatically when you install

    1.  Install [pip][] or [easy_install][], follow the instrcutions below

        -   pip: http://www.pip-installer.org/en/latest/installing.html
        -   easy_install: http://pypi.python.org/pypi/setuptools

    2.  Install numbercards with the following command in Terminal (Command
        Prompt)

        ~~~
        pip install numbercards
        ~~~

        or

        ~~~
        easy_install numbercards
        ~~~

[pip]: http://www.pip-installer.org/
[easy_install]: http://pypi.python.org/pypi/setuptools


Usage
-----------------------------------------------------------------------------

    usage: numbercards [-h] [-v] [-c NCOL] [-r NROW] [-p PREFIX] [-s SUFFIX]
                      [--no-trimmark] [--xmargin XMARGIN] [--ymargin YMARGIN]
                      [--pagesize {B4,LETTER,B5,B3,B6,LEGAL,A1,A0,A3,A2,A5,A4,B2,A6,B0,ELEVENSEVENTEEN,B1}]
                      [--orientation {landscape,portrait}]
                      [--font-family FONT_FAMILY] [--font-size FONT_SIZE]
                      [--face-color FACE_COLOR] [--stroke-color STROKE_COLOR]
                      [--font-file FONT_FILE]
                      numbers outfile

    Create bunches of simple number cards. Useful for creating number cards for
    posters in conferences. (C) 2013 hashnote.net, Alisue

    positional arguments:
      numbers               minimum number of cards you need
      outfile               output filename (PDF file)

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -c NCOL, --ncol NCOL  the number of columns (Default: 2)
      -r NROW, --nrow NROW  the number of rows (Default: 2)
      -p PREFIX, --prefix PREFIX
                            prefix of the number text
      -s SUFFIX, --suffix SUFFIX
                            suffix of the number text
      --no-trimmark         do not draw trim marks
      --xmargin XMARGIN     horizontal page margin in mm (Default: 8.4)
      --ymargin YMARGIN     vertical page margin in mm (Default: 8.4)
      --pagesize {B4,LETTER,B5,B3,B6,LEGAL,A1,A0,A3,A2,A5,A4,B2,A6,B0,ELEVENSEVENTEEN,B1}
                            page size of the output (Default: A4)
      --orientation {landscape,portrait}
                            orientation of the paper (Default: landscape)
      --font-family FONT_FAMILY
                            name of the font family. see the help of `--font-file`
                            option. (Default: Arimo-Regular)
      --font-size FONT_SIZE
                            font size (Default: 120)
      --face-color FACE_COLOR
                            comma separated RGB color (0-1) for font face
                            (Default: 0.1,0.1,0.1)
      --stroke-color STROKE_COLOR
                            comma separated RGB color (0-1) for trimmark (Default:
                            0.6,0.6,0.6)
      --font-file FONT_FILE
                            file name of external ttf font. It is strongly
                            suggested to specify this when you want to use
                            different font family while reportlab font searching
                            system is a little bit buggy
