from pandas.io.formats.style import Styler


ALICE_HUMAN, BOB_HUMAN, ALICE_BOT, BOB_BOT = ("#4F3130", "#753742", "#AA5042", "#A08C66") #D8D78F


def magnify():
    return [dict(selector="table",
                props=[("border-color", "black"),
                       ("text-align","left"),
                       ("border","1"),
                       ("width", "750px")
                      ]),
            dict(selector="span.speaker.alice.human",
                 props=[("color", ALICE_HUMAN)]
            ),
            dict(selector="span.speaker.alice.bot",
                 props=[("color", ALICE_BOT)]
            ),
            dict(selector="span.speaker.bob.human",
                 props=[("color", BOB_HUMAN)]
            ),
            dict(selector="span.speaker.bob.bot",
                 props=[("color", BOB_BOT)]
            ),
            dict(selector=".dialog td.speaker",
                 props=[("width", "5em"),
                        ("text-align", "right")]
            ),
            dict(selector=".dialog td.text",
                 props=[("text-align", "left")]
            ),
            dict(selector="tr.dialoghead",
                 props=[("background-color", "#D8D78F")]
            ),
            dict(selector="th", \
                 props=[("font-size", "12pt")]),
            dict(selector="table.dialog td", \
                 props=[
                     ('padding', "0em 1em"),
                 ]),
            dict(selector="td", \
                 props=[
                     ('padding', "1em"),
                     ('background-color', "white")
                 ]),
            dict(selector="td.context", \
                 props=[
                     ('max-width', "0"),
                     ('overflow', "hidden"),
                     ('text-overflow', "ellipsis"),
                     ('white-space', "nowrap")
                 ]),
            dict(selector="td.context:hover", \
                 props=[
                     #('max-width', "100%"),
                     ('text-align', "justify"),
                     ('white-space', "normal")
                 ]),
]

DialogStyler = Styler.from_custom_template("templates", "myhtml.tpl")
