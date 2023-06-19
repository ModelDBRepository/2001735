from neuron import h, gui
import CaPIC

# templates that define cell classes..............................
h.load_file("Amandola_MN3.hoc")
h.load_file("slicedCell.hoc")


myCell = h.Amandola_MN3_sliced()
# myCell = h.Amandola_MN3()

## add the PIC channels
CaPIC.setDendriticdistance(myCell)
CaPIC.placePunctaCaPIC(myCell, 0.0003/9, proximalLimit=300,
                       distalLimit=600, theta=-43)
