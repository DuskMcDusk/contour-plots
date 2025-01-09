import os
import shutil
import unittest

from parser import parseData

testFileFolderPath = "./test_files"
testFileName = "input.xyz"
def setup():

    # create tests file folder
    if not os.path.exists(testFileFolderPath):
        os.mkdir(testFileFolderPath)
    # write a test case file
    dest_path = os.path.join(testFileFolderPath, testFileName)
    f = open(dest_path, "w")
    testData = """# /beamlines/bl04/projects/cycle2024-I/uind-2024028063-nffa/DATA/STF_Ni/STF_Ni_cooling_f00001.xye : mythproc.py merge -s 0.006 -l -999.0 -f /beamlines/bl04/inhouse/ff/FlatField/ff_08May2024rod4mm60s_17keV.raw -b True -c true -o xye /beamlines/bl04/projects/cycle2024-I/uind-2024028063-nffa/DATA/STF_Ni/STF_Ni_cooling_00001.dat
# IsMon = [14510164, 14503967, 14510716]  IsPos = [-0.5004, -1.4881, -2.4989]
# Wave = 0.4139  CalPath /beamlines/bl04/commissioning/2024/May_2024/22May_2024/Si_30keV_f00003.cal
# Date = 2024-05-24_23:08:27 Dt = 10.0000  Bin = 0.0060  <imon> = 14508282 +/- 3060 (Min/Max) 14503967 / 14510716  <blowerT> = 734.5000 +/- 10.7716 (Min/Max) 724.7000 / 749.5000  <blowerC> = 733.4333 +/- 8.5187 (Min/Max) 725.7000 / 745.3000
# icurr 250.5165  mocoIn 1.8373E-05  mocoOut 0.6280  i15 10117554.6667  imon 14508282.3333  i7 6.6667  iEMpd_timer 10.0000  iEMpd_1 1.0903E-09  iEMpd_2 -1.1618E-08  iEMpd_3 -2.1474E-09  iEMpd_4 -1.3818E-09  iEMhp_timer 10.0000  iEMhp_1 6.3237E-07  iEMhp_2 -1.3660E-08  iEMhp_3 -5.5540E-09  iEMhp_4 -5.2629E-09  blowerP 13.8000  blowerSP 741.9667  blowerTar 282.3333
#      9776
5.4960000E-01  1.8058579E+02  1.4175608E+01
5.5560000E-01  1.9094472E+02  1.4489498E+01
5.6160000E-01  1.8488071E+02  1.4245959E+01
"""
    f.write(testData)
    f.close()
    print("setup")

def tearDown():
    if os.path.exists(testFileFolderPath):
        shutil.rmtree(testFileFolderPath)
    print("teardown")


class TestParser(unittest.TestCase):
    
    def test_parse(self):
        setup()
        expected = [
            [5.4960000E-01, 1.8058579E+02],
            [5.5560000E-01, 1.9094472E+02],
            [5.6160000E-01, 1.8488071E+02]
        ]
        path = os.path.join(testFileFolderPath, testFileName)
        actual = parseData(path)
        self.assertEqual(actual, expected)
        # tearDown()

if __name__ == "main":
    unittest.main()