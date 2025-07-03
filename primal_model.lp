\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  x[0] + x[1] + x[2] + x[3] + x[4]
Subject To
 vincolo_0: x[0] + x[3] <= 1
 vincolo_1: x[0] + x[1] <= 1
 vincolo_2: x[0] + x[4] <= 1
 vincolo_3: x[0] + x[2] <= 1
 vincolo_4: x[1] + x[3] <= 1
 vincolo_5: x[1] + x[4] <= 1
 vincolo_6: x[2] + x[3] <= 1
Bounds
Binaries
 x[0] x[1] x[2] x[3] x[4]
End
