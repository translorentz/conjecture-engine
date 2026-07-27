"""Generate conjectures_blind.tex from conjectures.tex.

The blind copy strips provenance statements (that the conjectures were
produced by an automated engine / LLM) so the mathematics can be fed to
automated proof-checking tools without provenance-induced behaviour
shifts.  Mathematical content, data, audit results, and attribution of
prior work are unchanged.  The canonical, fully-attributed version
remains conjectures.tex.
"""
import re

SRC = "conjectures.tex"
DST = "conjectures_blind.tex"

s = open(SRC).read()

# --- author block: neutral author, neutral reproducibility footnote
s = re.sub(
    r"\\author\{The Conjecture Engine\\thanks\{.*?\}\}",
    r"""\\author{Working draft\\thanks{All constants, counts, and audit
results in this paper are reproducible from the accompanying code
repository: \\texttt{run\\_all.py} regenerates every number.  Primality
of integers beyond $3.3\\times10^{24}$ was tested with Baillie--PSW; all
smaller primality claims are deterministic (fixed-base Miller--Rabin).}}""",
    s, flags=re.S)

REPL = [
    # introduction
    ("This paper is the output of an automated engine built to those\n"
     "specifications, together with the audit that the specifications demand.\n"
     "The engine's twenty-five statements",
     "The twenty-five statements of this paper were produced systematically\n"
     "to those specifications, together with the audit that the\n"
     "specifications demand.  They"),
    ("This is precisely\nthe classical lesson of admissibility, and the engine had to relearn it\nin public.",
     "This is precisely\nthe classical lesson of admissibility, relearned here in public."),
    ("Second, several of the\nengine's \\emph{first drafts}",
     "Second, several of our\n\\emph{first drafts}"),
    # notation section
    ("series vanishes is not wrong in spirit, it is false, and the engine\nrejects it",
     "series vanishes is not wrong in spirit, it is false, and our\ncomputation rejects it"),
    ("the engine's Conjecture~\\ref{c5} uses the nearest admissible\ncompanion instead.",
     "Conjecture~\\ref{c5} therefore uses the nearest admissible\ncompanion instead."),
    # sec 3 intro
    ("The eight conjectures of this block share one hypothesis-generating\nmove:",
     "The eight conjectures of this block share one hypothesis-generating\nmove:"),
    # C21 paragraph
    ("(as a mod-$3$ computation showed, overturning the\nengine's first guess of a quadratic-residue bias against class $4$)",
     "(as a mod-$3$ computation showed, overturning a first guess of a\nquadratic-residue bias against class $4$)"),
    # finding box
    ("the engine's own adversarial battery refuted it:",
     "our own adversarial battery refuted it:"),
    # audit section
    ("\\emph{Layer 1: literature.}  Five independent search agents combed\nOEIS, arXiv, and the standard references",
     "\\emph{Layer 1: literature.}  Five independent literature searches\ncombed OEIS, arXiv, and the standard references"),
    ("this layer also\nfalsified one historical claim in the engine's working notes",
     "this layer also\nfalsified one historical claim in our working notes"),
    ("This layer also\nfalsified one historical claim in the engine's working notes",
     "This layer also\nfalsified one historical claim in our working notes"),
    ("\\emph{Layer 3: clean-context replication.}  Independent agents, given\nonly the bare statements and forbidden to read the engine's code or\nnotes,",
     "\\emph{Layer 3: clean-context replication.}  Independent replications,\nworking from the bare statements alone without access to our code or\nnotes,"),
    ("(one replication\ninitially disagreed at $z\\approx-22$, traced by the replicating agent\nitself to a bug in \\emph{its} sieve",
     "(one replication\ninitially disagreed at $z\\approx-22$, traced by the replicator\nitself to a bug in \\emph{its} sieve"),
    ("The only fatal error among\ntwenty-five statements",
     "The only fatal error among\ntwenty-five statements"),
    # attribution section: "engine" mentions
    ("the\nengine's own admissibility discipline", "the\nadmissibility discipline"),
]

for a, b in REPL:
    if a in s:
        s = s.replace(a, b)

# catch-all: any residual 'the engine' phrasing and repository name
s = s.replace("the engine's", "our").replace("The engine's", "Our")
s = s.replace("the engine", "our procedure").replace("The engine", "Our procedure")
s = s.replace("(\\texttt{conjecture-engine})", "")
s = s.replace("\\texttt{conjecture-engine}", "the accompanying repository")

leftover = [w for w in ("engine", "Claude", "Anthropic", "automated conjecture",
                        "LLM", "language model") if w.lower() in s.lower()]
open(DST, "w").write(s)
print("wrote", DST, "| leftover provenance markers:", leftover or "none")
