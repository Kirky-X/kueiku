"""Utility functions — CSV I/O, formatting, matrix operations, statistical helpers."""

import csv
import io
import math
import sys
from pathlib import Path


# ───────────────────────── I/O Tool ─────────────────────────

def read_csv(source):
    """Read CSV from file path or stdin, return list[dict].

    Exits with a friendly error if the CSV is empty or has no data rows.
    """
    if source == "-" or source is None:
        text = sys.stdin.read()
    else:
        text = Path(source).read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text))
    rows = [row for row in reader]
    if not rows:
        where = "stdin" if (source == "-" or source is None) else f"'{source}'"
        print(f"Error: CSV input {where} is empty (no header or no data rows).", file=sys.stderr)
        sys.exit(1)
    return rows


def fnum(value, field, row_no):
    """Parse a float from a CSV cell; exit with a friendly error on bad values."""
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"Error: row {row_no}: invalid number for field '{field}': {value!r} (expected a number)", file=sys.stderr)
        sys.exit(1)


def inum(value, field, row_no):
    """Parse an int from a CSV cell; exit with a friendly error on bad values."""
    try:
        return int(value)
    except (TypeError, ValueError):
        print(f"Error: row {row_no}: invalid integer for field '{field}': {value!r} (expected an integer)", file=sys.stderr)
        sys.exit(1)


def write_output(content, output_path=None):
    """Output to file or stdout."""
    if output_path:
        Path(output_path).write_text(content, encoding="utf-8")
        print(f"Report written: {output_path}", file=sys.stderr)
    else:
        print(content)


# ───────────────────────── FormatTool ─────────────────────────

def md_table(headers, rows):
    """Generate Markdown table string."""
    if not rows:
        return "(empty table)\n"
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    sep = "-|-".join("-" * w for w in col_widths)
    lines = [fmt.format(*headers), sep]
    for row in rows:
        lines.append(fmt.format(*[str(c) for c in row]))
    return "\n".join(lines) + "\n"


def fmt_num(n, decimals=2):
    """Format number with thousands separator and decimal places."""
    if isinstance(n, int):
        return f"{n:,}"
    if abs(n) >= 1000:
        return f"{n:,.{decimals}f}"
    return f"{n:.{decimals}f}"


def pct(n, decimals=1):
    return f"{n:.{decimals}f}%"


# ───────────────────────── Matrix Tools (for quantitative investment) ─────────────────────────

def mat_mult(A, B):
    """Matrix multiplication A(m×n) × B(n×p)."""
    n = len(A)
    m = len(B[0])
    k = len(B)
    return [[sum(A[i][x] * B[x][j] for x in range(k)) for j in range(m)] for i in range(n)]


def mat_inv(M):
    """Gauss-Jordan elimination matrix inverse (partial pivoting)."""
    n = len(M)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        mx = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[mx] = aug[mx], aug[col]
        if abs(aug[col][col]) < 1e-12:
            return None
        pivot = aug[col][col]
        aug[col] = [x / pivot for x in aug[col]]
        for row in range(n):
            if row != col:
                f = aug[row][col]
                aug[row] = [aug[row][j] - f * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def mat_transpose(M):
    """Matrix transpose."""
    return [list(row) for row in zip(*M)]


def quad_form(w, M):
    """Quadratic form w'Mw."""
    n = len(w)
    return sum(w[i] * M[i][j] * w[j] for i in range(n) for j in range(n))


# ───────────────────────── Statistical Tools ─────────────────────────

def rank_data(values):
    """Rank data (1-based, average tie-breaking)."""
    indexed = sorted(enumerate(values), key=lambda x: x[1])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(indexed):
        j = i
        while j < len(indexed) and indexed[j][1] == indexed[i][1]:
            j += 1
        avg_rank = (i + j + 1) / 2.0
        for k in range(i, j):
            ranks[indexed[k][0]] = avg_rank
        i = j
    return ranks


def spearman_ic(x, y):
    """Spearman rank correlation (IC)."""
    rx = rank_data(x)
    ry = rank_data(y)
    n = len(x)
    if n < 3:
        return 0.0
    mx = sum(rx) / n
    my = sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n)) / n
    sx = math.sqrt(sum((r - mx) ** 2 for r in rx) / n)
    sy = math.sqrt(sum((r - my) ** 2 for r in ry) / n)
    if sx == 0 or sy == 0:
        return 0.0
    return cov / (sx * sy)


def norm_cdf(x):
    """Standard normal CDF approximation (Abramowitz & Stegun)."""
    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
    p = 0.3275911
    sign = 1 if x >= 0 else -1
    x = abs(x) / math.sqrt(2)
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)
    return 0.5 * (1.0 + sign * y)


def z_test(p1, n1, p2, n2):
    """Two-proportion z-test, return (z_stat, p_value_approx)."""
    p_pool = (n1 * p1 + n2 * p2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return 0, 1.0
    z = (p2 - p1) / se
    p_val = 2 * (1 - norm_cdf(abs(z)))
    return z, p_val


def quintile_score(values, reverse=False):
    """Map values to 1-5 quintile scores. reverse=True means lower value gets higher score (e.g. recency)."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    scores = {}
    for i, v in enumerate(sorted_vals):
        q = min(4, int(i / n * 5))
        scores[v] = (5 - q) if reverse else (q + 1)
    return [scores[v] for v in values]
