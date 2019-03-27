def process_file(fname):
    """Given a TeX file name, return a list of \items."""
    with open(fname, "r") as fp:
        contents = fp.read()

    # FIXME: this is brittle, and will produce bogus if e.g. \begin{enumerate}
    # is followed by a TeX comment: \begin{enumerate} % [resume]

    # extract the \enumerate, discard the rest
    try:
        items = contents.split("\\begin{enumerate}[resume]")[1]
    except IndexError:
        # no {enumerate}[resume]?
        items = contents.split("\\begin{enumerate}")[1]

    items = items.split("\\end{enumerate}")[0]

    # extract individual items, discard empty lines
    questions = [q for q in items.split("\\item") if q.strip()]
    return questions


if __name__ == "__main__":
    print(process_file("matan.tex"))
