import numpy as np
import ROOT
import random

data = np.loadtxt("./Data/data_D0_daughtersPT_Eta_Phi_Mass_dau1_dau2_AND_D0PT_Y_Phi_Mass.txt")
nEvents = 40000

daughters = np.zeros([nEvents, 10]) # Px1 Px2 Py1 Py2 Pz1 Pz2 E1 E2 M1 M2
mother = np.zeros([nEvents, 5]) # Px Py Pz E M
verif = np.zeros([nEvents])

j = 0
while j < nEvents:
    i = random.randint(0, 146690)

    if i not in verif:
        verif[j] = i

        # Within this logic trk1 = pions and trk2 = kaons
        if data[i][6] == 0.13957:
            v_trk1 = ROOT.Math.PtEtaPhiMVector(data[i][0], data[i][2], data[i][4], data[i][6])
            v_trk2 = ROOT.Math.PtEtaPhiMVector(data[i][1], data[i][3], data[i][5], data[i][7])
            daugthers[j][8], daughters[j][9] = data[i][6], data[i][7] # M (9th and 10th columns)
        if data[i][6] == 0.493677:
            v_trk2 = ROOT.Math.PtEtaPhiMVector(data[i][0], data[i][2], data[i][4], data[i][6])
            v_trk1 = ROOT.Math.PtEtaPhiMVector(data[i][1], data[i][3], data[i][5], data[i][7])
            daugthers[j][8], daughters[j][9] = data[i][7], data[i][6] # M (9th and 10th columns)

        daughters[j][0], daughters[j][1] = v_trk1.Px(), v_trk2.Px() # Px (1st and 2nd columns)
        daughters[j][2], daughters[j][3] = v_trk1.Py(), v_trk2.Py() # Py (3rd and 4th columns)
        daughters[j][4], daughters[j][5] = v_trk1.Pz(), v_trk2.Pz() # Pz (5th and 6th columns)
        daughters[j][6], daughters[j][7] = v_trk1.E(), v_trk2.E() # Px (7th and 8th columns)

        D0 = ROOT.Math.PtEtaPhiMVector(data[i][8], data[i][9], data[i][10], data[i][11]) # D0

        mother[j][0] = D0.Px() # Px (1st column)
        mother[j][1] = D0.Py() # Py (2nd column)
        mother[j][2] = D0.Pz() # Pz (3rd column)
        mother[j][3] = D0.E() # E (4th column)
        mother[j][4] = data[i][12] # M (5th column)

        j += 1
    else:
        pass
        
np.savetxt("./Data/data_D0_daughtersPx_Py_Pz_E_M_trk1_trk2.txt", daughters, fmt='%.5f')
np.savetxt("./Data/data_D0_daughtersPx_Py_Pz_E_M_D0.txt", mother, fmt='%.5f')