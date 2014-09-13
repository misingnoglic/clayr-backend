def testDatabaseGenerator():
    #Values from http://www.webmd.com/a-to-z-guides/complete-blood-count-cbc
    # and http://www.mayoclinic.org/tests-procedures/complete-blood-count/basics/results/prc-20014088
    testDB = {}
    #ranges = [("name", hex, (lower, upper))]
    class Test:
      def __init__(self,aliases,brief_desc,desc,ranges,unit):
        self.aliases = aliases #Synonym names/codes within tests
        self.brief_desc = brief_desc #1/2 line description
        self.desc = desc #Don't worry about these for now
        self.ranges = ranges
        self.unit = unit

    AVGCOLOR = '379F7A'

    WBCdesc = 'When a person has a bacterial infection, the number of white cells rises very quickly. The number of white blood cells is sometimes used to find an infection or to see how the body is dealing with cancer treatment.'
    testDB['wbc'] = Test(['WBC', 'leukocyte'], 'White Blood Cell count', WBCdesc,[('AVG', AVGCOLOR, (3.5, 10.5))],'10^3 cells/uL')

    RBCdesc = ''
    testDB['rbc'] = Test(['RBC', 'red blood cell count'], 'Red Blood Cell count', RBCdesc, [('AVG', AVGCOLOR, (4.32, 5.72))], '10^6 cells/uL')

    Hemodesc = ''
    testDB['hemo'] = Test(['Hemoglobin', 'Hemo', 'HGB'], 'Oxygen capacity of RBCs', Hemodesc, [('AVG', AVGCOLOR, (13.5, 17.5))], 'g/dL')

    Hemocritdesc = ''
    testDB['hematocrit'] = Test(['Hematocrit', 'HCT', 'PCV'], 'pct space RBCs take up', Hemocritdesc, [('AVG', AVGCOLOR, (38.8, 50.0))], '%')

    MCVdesc = ''
    testDB['mcv'] = Test(['MCV', 'mean corpuscular volume'], 'Average volume of a RBC', MCVdesc, [('AVG', AVGCOLOR, (84, 96))], 'fL')

    MCHdesc = ''
    testDB['mch'] = Test(['MCH', 'mean corpuscular hemoglobin'], 'Average mass of a hemoglobin per RBC', MCHdesc, [('AVG', AVGCOLOR, (28, 34))], 'pg')

    MCHCdesc = ''
    testDB['mchc'] = Test(['MCHC', 'mean corpuscular hemoglobin concentration'], 'concentration of hemoglobin in volume of RBCs', MCHCdesc, [('AVG', AVGCOLOR, (32, 36))], 'g/dL')

    RDWdesc = ''
    testDB['rdw'] = Test(['RDW', 'RDW-SD', 'red blood cell distribution width'], 'measures variation in RBC size', RDWdesc, [('AVG', AVGCOLOR, (39, 46))], 'fL')

    return testDB