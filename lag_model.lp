\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6]
Subject To
 vincolo_{i}: x[0] + x[1] + x[2] + x[3] >= 1
 vincolo_{i}: x[1] + x[4] + x[5] >= 1
 vincolo_{i}: x[3] + x[6] >= 1
 vincolo_{i}: x[0] + x[4] + x[6] >= 1
 vincolo_{i}: x[2] + x[5] >= 1
Bounds
End
