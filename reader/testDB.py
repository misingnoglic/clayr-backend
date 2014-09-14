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

    AVGCOLOR = '00BCD1'
    GOODCOLOR = '379F7A'
    MEHCOLOR = 'F2B657'
    BADCOLOR = 'CE3D48'

    WBCdesc = 'When a person has a bacterial infection, the number of white cells rises very quickly. ' \
              'The number of white blood cells is sometimes used to find an infection or to see how the ' \
              'body is dealing with cancer treatment.'
    testDB['wbc'] = Test(['WBC', 'leukocyte'], 'White Blood Cell count', WBCdesc,[('AVG', AVGCOLOR, (4.5, 10.5))],'10^3 cells/uL')

    RBCdesc = 'RBCs contain hemoglobin, which carries oxygen. How much oxygen your body tissues ' \
              'get depends on how many RBCs you have and how well they work.'
    testDB['rbc'] = Test(['RBC', 'red blood cell count'], 'Red Blood Cell count', RBCdesc, [('AVG', AVGCOLOR, (4.32, 5.72))], '10^6 cells/uL')

    Hemodesc = 'Hemoglobin is a protein in red blood cells that carries oxygen.'
    testDB['hemo'] = Test(['Hemoglobin', 'Hemo', 'HGB','hb'], 'Oxygen capacity of RBCs', Hemodesc, [('AVG', AVGCOLOR, (13.5, 17.5))], 'g/dL')

    Hemocritdesc = 'Hematocrit is a blood test that measures the percentage of the volume of whole ' \
                   'blood that is made up of red blood cells. This measurement depends on the number ' \
                   'of red blood cells and the size of red blood cells.'
    testDB['hematocrit'] = Test(['Hematocrit', 'HCT', 'PCV'], 'pct space RBCs take up', Hemocritdesc, [('AVG', AVGCOLOR, (38.8, 50.0))], '%')

    MCVdesc = 'Average red blood cell size'
    testDB['mcv'] = Test(['MCV', 'mean corpuscular volume'], 'Average volume of a RBC', MCVdesc, [('AVG', AVGCOLOR, (84, 96))], 'fL')

    MCHdesc = 'Hemoglobin amount per red blood cell'
    testDB['mch'] = Test(['MCH', 'mean corpuscular hemoglobin'], 'Average mass of a hemoglobin per RBC', MCHdesc, [('AVG', AVGCOLOR, (28, 34))], 'pg')

    MCHCdesc = 'The amount of hemoglobin relative to the size of the cell (hemoglobin concentration) per red blood cell'
    testDB['mchc'] = Test(['MCHC', 'mean corpuscular hemoglobin concentration'], 'concentration of hemoglobin in volume of RBCs', MCHCdesc, [('AVG', AVGCOLOR, (32, 36))], 'g/dL')

    RDWdesc = 'Red cell distribution width'
    testDB['rdw'] = Test(['RDW', 'RDW-SD', 'RDW-CV','red blood cell distribution width'], 'measures variation in RBC size', RDWdesc, [('AVG', AVGCOLOR, (39, 46))], 'fL')

    return testDB

def testValueDictionary():
    d = {}
    d['cbc'] = ['wbc','rbc', 'hemo', 'hematocrit', 'mcv', 'mch', 'mchc', 'rdw']
    return d
