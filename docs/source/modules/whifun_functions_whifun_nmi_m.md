- **Key Features:**
  - WHIFUN_NMI Calculates the Normalized Mutual Information (NMI) between two label vectors. nmi = WHIFUN_NMI(labels1, labels2) computes the Normalized Mutual Information between two vectors of cluster or classification labels. NMI is a symmetry measure of similarity between two data clusterings, ranging from 0 (no mutual dependence) to 1 (perfect correlation). This function is commonly used to evaluate the quality of a clustering algorithm by comparing its output (labels1) to known ground truth labels (labels2), or to compare two different clustering solutions. The calculation involves the follow
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: Statistics and Machine Learning Toolbox

## Function: `whifun_nmi()`
- **Functional Purpose:** WHIFUN_NMI Calculates the Normalized Mutual Information (NMI) between two label vectors. nmi = WHIFUN_NMI(labels1, labels2) computes the Normalized Mutual Information between two vectors of cluster or classification labels. NMI is a symmetry measure of similarity between two data clusterings, ranging from 0 (no mutual dependence) to 1 (perfect correlation). This function is commonly used to evaluate the quality of a clustering algorithm by comparing its output (labels1) to known ground truth labels (labels2), or to compare two different clustering solutions. The calculation involves the following steps: 1. **Confusion Matrix (C)**: Creates a contingency table showing the overlap between the
- **Arguments:**
  - `labels1` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `labels2` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
