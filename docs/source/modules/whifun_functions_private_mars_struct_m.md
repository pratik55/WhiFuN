- **Key Features:**
  - Multifunction function for manipulating structures To help the exposition a bit: 'fill' in a name, means that values empty or missing in one structure are fetched from another 'merge' means simply that missing fields are added, with values, from a second structure (but not filled if empty) Each function needs to deal with the case of empty arguments FORMAT c = mars_struct('fillafromb', a, b, fieldns, flags) fills structure fields empty or missing in a from those present in b a, b are structures fieldns (optional) is cell array of field names to fill from in b c is returned structure Is recursi
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `mars_struct()`
- **Functional Purpose:** Multifunction function for manipulating structures To help the exposition a bit: 'fill' in a name, means that values empty or missing in one structure are fetched from another 'merge' means simply that missing fields are added, with values, from a second structure (but not filled if empty) Each function needs to deal with the case of empty arguments FORMAT c = mars_struct('fillafromb', a, b, fieldns, flags) fills structure fields empty or missing in a from those present in b a, b are structures fieldns (optional) is cell array of field names to fill from in b c is returned structure Is recursive, will fill struct fields from struct fields flags may contain 'f', which Force fills a from b (al
- **Arguments:**
  - `action` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
