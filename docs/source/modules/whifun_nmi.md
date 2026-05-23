# whifun_nmi

**Source:** `whifun_functions/whifun_nmi.m:1`

## Signature

```matlab
function nmi = whifun_nmi(labels1, labels2)
```

## Summary

WHIFUN_NMI Calculates the Normalized Mutual Information (NMI) between two label vectors.

## Description

Information between two vectors of cluster or classification labels. NMI is a symmetry measure of similarity between two data clusterings, ranging from 0 (no mutual dependence) to 1 (perfect correlation).

This function is commonly used to evaluate the quality of a clustering algorithm by comparing its output (labels1) to known ground truth labels (labels2), or to compare two different clustering solutions.

The calculation involves the following steps:

1.  **Confusion Matrix (C)**: Creates a contingency table showing the
overlap between the two labelings.

2.  **Probabilities (pi, uj)**: Calculates the marginal probabilities
for each set of labels.

3.  **Mutual Information (I)**: Computes the mutual information using
the formula: I = sum(P(i,j) * log2(P(i,j) / (P(i) * P(j)))). A small constant (1e-10) is added to avoid issues with log2(0).

4.  **Entropy (Hpi, Huj)**: Computes the entropy for each set of labels.
5.  **Normalization**: Normalizes the mutual information by the average
entropy of the two labelings: NMI = 2 * I / (H(pi) + H(uj)).

## Input Arguments

### `labels1`
A vector of cluster or class labels (e.g., from a clustering algorithm).

### `labels2`
A vector of ground truth or second cluster labels. Must be the same length as labels1.

## Output Arguments

### `nmi`
The Normalized Mutual Information score (scalar). See also CONFUSIONMAT, LOG2. Modified by Pratik from following code qqffssxx (2025). Normalized Mutual Information (NMI) for Cluster Analysis (https://www.mathworks.com/matlabcentral/fileexchange/130784-normalized-mutual-information-nmi-for-cluster-analysis), MATLAB Central File Exchange. Retrieved September 25, 2025.

## Author

Author: Pratik Jain, qqffssxx

## Examples

```matlab
nmi = WHIFUN_NMI(labels1, labels2) computes the Normalized Mutual
```
