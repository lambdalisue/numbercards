#!/usr/bin/env python
# coding=utf-8
"""
Create bunches of simple number cards.
Useful for creating number cards for posters in conferences.

(C) 2013 hashnote.net, Alisue
"""
__author__  = 'Alisue (lambdalisue@hashnote.net)'
__version__ = '0.1.0'
__date__    = '2013-11-20'

from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.lib.units import mm


PAGESIZES = {
    'A0': pagesizes.A0,
    'A1': pagesizes.A1,
    'A2': pagesizes.A2,
    'A3': pagesizes.A3,
    'A4': pagesizes.A4,
    'A5': pagesizes.A5,
    'A6': pagesizes.A6,
    'B0': pagesizes.B0,
    'B1': pagesizes.B1,
    'B2': pagesizes.B2,
    'B3': pagesizes.B3,
    'B4': pagesizes.B4,
    'B5': pagesizes.B5,
    'B6': pagesizes.B6,
    'LETTER': pagesizes.LETTER,
    'LEGAL': pagesizes.LEGAL,
    'ELEVENSEVENTEEN': pagesizes.ELEVENSEVENTEEN,
}

TRIMMARK_WIDTH = 5.0 * mm
TRIMMARK_HEIGHT = 5.0 * mm
TRIMMARK_MINOR_WIDTH = 3.0 * mm
TRIMMARK_MINOR_HEIGHT = 3.0 * mm
TRIMMARK_COLOR = (0.6, 0.6, 0.6)

def draw_numbercards(c, n, ncol, nrow, prefix='', suffix='',
                     pagesize=pagesizes.A4,
                     orientation=pagesizes.landscape,
                     margin=(8.4*mm, 8.4*mm),
                     font_family='Arimo-Regular',
                     font_size=20,
                     face_color=(0.1,0.1,0.1),
                     stroke_color=(0.6,0.6,0.6),
                     trimmark=True):
    """
    Draw number cards on the specified reportlab canvas

    Args:
        c: An instance of reportlab Canvas
        n: The minimum number of cards you need
        ncol: The number of columns in the page
        nrow: The number of rows in the page
        prefix: A prefix of the text in each card
        suffix: A suffix of the text in each card
        pagesize: A page size (reportlab.lib.pagesizes.XXXX)
        orientation: A orientation of the page (reportlab.lib.pagesize.landscape
            or portrait)
        margin: A two item list. The 1st and 2nd items indicate xmargin and
            ymargin respectively
        font_family: A name of font family
        font_size: A size of font
        trimmark: Draw trim mark if it is true

    Returns:
        An instance of reportlab Canvas
    """
    # calculate size
    xmargin, ymargin = margin
    pwidth, pheight = orientation(pagesize)
    width = pwidth - xmargin*2
    height = pheight - ymargin*2
    swidth = width / ncol
    sheight = height / nrow

    def draw_trimmark(col, row):
        x = xmargin + swidth * col
        y = ymargin + sheight * row

        if row == 0:
            c.line(x, ymargin-TRIMMARK_HEIGHT,
                   x, ymargin)
            c.line(x-TRIMMARK_MINOR_WIDTH/2, ymargin,
                   x+TRIMMARK_MINOR_WIDTH/2, ymargin)
        elif row == nrow-1:
            c.line(x, pheight-(ymargin-TRIMMARK_HEIGHT),
                   x, pheight-ymargin)
            c.line(x-TRIMMARK_MINOR_WIDTH/2, pheight-ymargin,
                   x+TRIMMARK_MINOR_WIDTH/2, pheight-ymargin)

        if col == 0:
            c.line(xmargin-TRIMMARK_WIDTH, y,
                   xmargin, y)
            c.line(xmargin, y-TRIMMARK_MINOR_HEIGHT/2,
                   xmargin, y+TRIMMARK_MINOR_HEIGHT/2)
        elif col == ncol-1:
            c.line(pwidth-(xmargin-TRIMMARK_WIDTH), y,
                   pwidth-xmargin, y)
            c.line(pwidth-xmargin, y-TRIMMARK_MINOR_HEIGHT/2,
                   pwidth-xmargin, y+TRIMMARK_MINOR_HEIGHT/2)



    index = 1
    while index <= n:
        c.setPageSize(orientation(pagesize))
        c.setFont(font_family, font_size)
        c.setFillColorRGB(*face_color)
        c.setStrokeColorRGB(*stroke_color)
        for row in range(nrow):
            for col in range(ncol):
                # calculate center
                x = xmargin + swidth * col + swidth / 2
                y = ymargin + sheight * (nrow-row-1) + sheight / 2
                # draw number with prefix, suffix
                c.drawCentredString(x, y, prefix+str(index)+suffix)
                # increate the number
                index += 1
                # draw trimmark
                if trimmark:
                    draw_trimmark(col, row)
        if trimmark:
            draw_trimmark(ncol, 0)
            draw_trimmark(ncol, nrow-1)
            draw_trimmark(0, nrow)
            draw_trimmark(ncol-1, nrow)
        # newpage
        c.showPage()
    return c


def main(args=None):
    import os
    import argparse
    from reportlab.pdfbase.pdfmetrics import registerFont
    from reportlab.pdfbase.ttfonts import TTFont

    usage  = None
    description = __doc__
    epilog = None
    parser = argparse.ArgumentParser('numbercards',
                                     usage=usage,
                                     description=description,
                                     epilog=epilog,
                                     version=__version__)
    parser.add_argument('numbers', type=int,
                        help='minimum number of cards you need')
    parser.add_argument('outfile',
                        help='output filename (PDF file)')
    parser.add_argument('-c', '--ncol', default=2, type=int,
                        help='the number of columns (Default: 2)')
    parser.add_argument('-r', '--nrow', default=2, type=int,
                        help='the number of rows (Default: 2)')
    parser.add_argument('-p', '--prefix', default='',
                        help='prefix of the number text')
    parser.add_argument('-s', '--suffix', default='',
                        help='suffix of the number text')
    parser.add_argument('--no-trimmark', dest='trimmark',
                        default=True, action='store_false',
                        help='do not draw trim marks')
    parser.add_argument('--xmargin', default=8.4, type=float,
                        help='horizontal page margin in mm '
                             '(Default: 8.4)')
    parser.add_argument('--ymargin', default=8.4, type=float,
                        help='vertical page margin in mm '
                             '(Default: 8.4)')
    parser.add_argument('--pagesize', default='A4',
                        choices=PAGESIZES.keys(),
                        help='page size of the output (Default: A4)')
    parser.add_argument('--orientation', default='landscape',
                        choices=('landscape', 'portrait'),
                        help='orientation of the paper (Default: landscape)')
    parser.add_argument('--font-family', default='Arimo-Regular',
                        help='name of the font family. '
                             'see the help of `--font-file` option. '
                             '(Default: Arimo-Regular)')
    parser.add_argument('--font-size', default=120, type=float,
                        help='font size (Default: 120)')
    parser.add_argument('--face-color', default='0.1,0.1,0.1',
                        help='comma separated RGB color (0-1) for font face '
                             '(Default: 0.1,0.1,0.1)')
    parser.add_argument('--stroke-color', default='0.6,0.6,0.6',
                        help='comma separated RGB color (0-1) for trimmark '
                             '(Default: 0.6,0.6,0.6)')
    parser.add_argument('--font-file', default=None,
                        help='file name of external ttf font. '
                             'It is strongly suggested to specify this '
                             'when you want to use different font family '
                             'while reportlab font searching system is a '
                             'little bit buggy')
    args = parser.parse_args(args)

    # modify the parsed arguments
    args.margin = (args.xmargin * mm, args.ymargin * mm)
    args.pagesize = PAGESIZES[args.pagesize]
    if args.orientation == 'landscape':
        args.orientation = pagesizes.landscape
    else:
        args.orientation = pagesizes.portrait
    args.face_color = map(float, args.face_color.split(','))
    args.stroke_color = map(float, args.stroke_color.split(','))

    # reportlab cannot really find font so I use Arimo for default
    if args.font_file is None:
        resdir = os.path.dirname(__file__)
        resdir = os.path.dirname(resdir)
        resdir = os.path.dirname(resdir)
        resdir = os.path.join(resdir, 'res')
        font_families = (
            'Arimo-Bold',
            'Arimo-BoldItalic',
            'Arimo-Italic',
            'Arimo-Regular')
        for font_family in font_families:
            filename = os.path.join(resdir, font_family+".ttf")
            registerFont(TTFont(font_family, filename))
    else:
        registerFont(TTFont(args.font_family, args.font_file))

    # draw numbercards
    c = canvas.Canvas(args.outfile)
    c = draw_numbercards(c, args.numbers, args.ncol, args.nrow,
                         prefix=args.prefix,
                         suffix=args.suffix,
                         pagesize=args.pagesize,
                         orientation=args.orientation,
                         margin=args.margin,
                         font_family=args.font_family,
                         font_size=args.font_size,
                         trimmark=args.trimmark)
    # save
    c.save()

if __name__ == '__main__':
    main()
