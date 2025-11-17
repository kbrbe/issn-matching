import pandas as pd
import unicodedata
import ast
import os
import re

# -----------------------------------------------------------------------------
def jsonParser(data):
    return ast.literal_eval(data) if data != "" else np.nan

# -----------------------------------------------------------------------------
def createInputDataframe(prefix, path, columns):

  # create dataframes for each 1:n file
  colDfs = {}
  for c in columns:
    colFile = os.path.join(path, f'{prefix}-{c}.csv')
    colDfs[c] = pd.read_csv(colFile)

  # read main csv
  mainDf = pd.read_csv(os.path.join(path,f'{prefix}.csv'))

  
  return mainDf, colDfs

# -----------------------------------------------------------------------------
def normalize(s):
    if pd.isna(s):
        return s
    s = s.strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = " ".join(s.split())  # collapse whitespace
    return s


# -----------------------------------------------------------------------------
def split_classification_for_explode(s):
    """
    Given a MARC-style classification string like '654.165 (05) (493.2 B.)',
    return a list of elements to explode for linkage:
    - main class
    - each auxiliary facet individually
    - optional progressive combinations
    """
    if pd.isna(s):
        return []
    
    s = s.strip()
    
    # Extract main numeric class
    main_match = re.match(r"^([\d\.]+)", s)
    main_class = main_match.group(1) if main_match else ""
    
    # Extract all parentheses content
    parens = re.findall(r"\((.*?)\)", s)
    
    # Normalize: strip whitespace, remove trailing dots
    parens = [p.strip().rstrip('.') for p in parens if p.strip()]
    
    # Initialize list of codes
    codes = []
    
    # 1. Main class alone
    if main_class:
        codes.append(main_class)
    
    # 2. Each auxiliary separately
    codes.extend(parens)
    
    # 3. Progressive combinations (optional)
    if parens:
        combined = main_class
        for p in parens:
            combined += " " + p
            codes.append(combined)
    
    # Deduplicate and return
    codes = list(dict.fromkeys(codes))
    return codes

