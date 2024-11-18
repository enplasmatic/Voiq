_PURPLE = {
    "[#]": "def",
    "[*]": "class"
}

_BLUE = {
    "[pair]": "lambda",
    "[get]": "import",
    "[using]": "with",
    "[::]": "pass",
    "[attempt]": "try",
    "[ef]": "elif",
    "[if]": "if",
    "[else]": "else",
    "[but]": "finally",
    "[/]": "for",
    "[while]": "while",
    "[gen]": "yield",
    " [&] ": " and ",
    " [|] ": " or ",
    " [!] ": " not ",
    " [:] ": " as ",
    "[esif]": "assert",
    "[send]": "async",
    "[pause]": "await",
    "[global]": "global",
    "[!local]": "nonlocal",
    "[>]": "return",
    "[error]": "raise",
    "[>>]": "try",
    "[<<]": "except",
    " ++ ": " += "
    
}



_FUNCS = {
    #I/O
    '>>': "print",
    "<<": "input",
    "read": "open",
    "cls": "close",
    "div": "split",
    "@": "int",
    "line": "readline",

    #LOOP OPERATIONS
    "from": "in range",
    "++": "max",
    "--": "min",


    #DATA OPERATIONS
    "get": "zip",
    "[]": "list",
    "apply": "map",


    #MISC
    "|": "abs",
    "|+": "sum",


}

for f in _FUNCS.copy():
    _FUNCS[f+"("] = _FUNCS[f] + "("
    del _FUNCS[f]


Keywords = {**_FUNCS, **_BLUE, **_PURPLE}

KeywordsInversed = {v: k for k, v in Keywords.items()}
