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
    testDB['wbc'] = Test(['WBC', 'leukocyte'], 'White Blood Cell count', WBCdesc,[('LOW', BADCOLOR, (2.0, 4.5))], ('AVG', AVGCOLOR, (4.5, 11.0)),('HIGH', BADCOLOR, (11.1, 30.0))],'10^3 cells/uL')

    RBCdesc = 'RBCs contain hemoglobin, which carries oxygen. How much oxygen your body tissues ' \
              'get depends on how many RBCs you have and how well they work.'
    testDB['rbc'] = Test(['RBC', 'red blood cell count'], 'Red Blood Cell count', RBCdesc, [('LOW', BADCOLOR, (1.0, 4.1)), ('AVG', AVGCOLOR, (4.2, 5.4)), ('HIGH', BADCOLOR, (5.5, 10.0))], '10^6 cells/uL')

    Hemodesc = 'Hemoglobin is a protein in red blood cells that carries oxygen.'
    testDB['hemo'] = Test(['Hemoglobin', 'Hemo', 'HGB','hb'], 'Oxygen capacity of RBCs', Hemodesc, [('LOW', BADCOLOR, (6.0, 13.5)), ('AVG', AVGCOLOR, (13.6, 17.5)), ('HIGH', BADCOLOR, (17.6, 20.0))], 'g/dL')

    Hemocritdesc = 'Hematocrit is a blood test that measures the percentage of the volume of whole ' \
                   'blood that is made up of red blood cells. This measurement depends on the number ' \
                   'of red blood cells and the size of red blood cells.'
    testDB['hematocrit'] = Test(['Hematocrit', 'HCT', 'PCV'], 'pct space RBCs take up', Hemocritdesc, [('LOW', BADCOLOR, (18.0, 40.0)), ('AVG', AVGCOLOR, (40.1, 54.0)), ('HIGH', BADCOLOR, (54.1, 60.0))], '%')

    MCVdesc = 'The MCV is a measure of the average size of a red blood cell. The MCV is used to determine' \
              'the type and cause of anemia.'
    testDB['mcv'] = Test(['MCV', 'mean corpuscular volume'], 'Average volume of a RBC', MCVdesc, [('LOW', BADCOLOR, (60.0, 80.0)), ('AVG', AVGCOLOR, (80.1, 96.0)), ('HIGH', BADCOLOR, (96.1, 120.0))], 'fL')

    MCHdesc = 'The average mass of hemoglobin per red cell. The MCH is used to determine the type,' \
              'cause and severity of anemia.'
    testDB['mch'] = Test(['MCH', 'mean corpuscular hemoglobin'], 'Average mass of a hemoglobin per RBC', MCHdesc, [('LOW', BADCOLOR, (15.4, 25.3)), ('AVG', AVGCOLOR, (25.4, 34.6)), ('HIGH', BADCOLOR, (34.7, 45.6))], 'pg')

    MCHCdesc = 'The amount of hemoglobin relative to the size of the cell (hemoglobin concentration) per red blood cell'
    testDB['mchc'] = Test(['MCHC', 'mean corpuscular hemoglobin concentration'], 'concentration of hemoglobin in volume of RBCs', MCHCdesc, [('LOW', BADCOLOR, (25.0, 30.9)), ('AVG', AVGCOLOR, (31.0, 36.0)), ('HIGH', BADCOLOR, (36.1, 41.0))], 'g/dL')

    RDWdesc = 'Red cell distribution width is a measure of the variation in the size of red blood cells.'
    testDB['rdw'] = Test(['RDW', 'RDW-SD', 'RDW-CV','red blood cell distribution width'], 'measures variation in RBC size', RDWdesc, [('LOW', BADCOLOR, (7.0, 11.4)), ('AVG', AVGCOLOR, (11.5, 14.5)), ('HIGH', BADCOLOR, (14.6, 17.0))], 'fL')

    return testDB

def testValueDictionary():
    d = {}
    d['cbc'] = ['wbc','rbc', 'hemo', 'hematocrit', 'mcv', 'mch', 'mchc', 'rdw']
    return d
