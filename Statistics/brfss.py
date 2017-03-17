import pandas as pd
import numpy as np

class FixedWidthVariables(object):
    """Represents a set of variables in a fixed width file."""

    def __init__(self, variables, index_base=0):
        """Initializes.

        variables: DataFrame
        index_base: are the indices 0 or 1 based?

        Attributes:
        colspecs: list of (start, end) index tuples
        names: list of string variable names
        """
        self.variables = variables

        # note: by default, subtract 1 from colspecs
        self.colspecs = variables[['start', 'end']] - index_base

        # convert colspecs to a list of pair of int
        self.colspecs = self.colspecs.astype(np.int).values.tolist()
        self.names = variables['name']

    def ReadFixedWidth(self, filename, **options):
        """Reads a fixed width ASCII file.

        filename: string filename

        returns: DataFrame
        """
        df = pd.read_fwf(filename,
                             colspecs=self.colspecs, 
                             names=self.names,
                             **options)
        return df


    
def ReadBrfss(filename='LLCP2015ASC.zip', compression='zip', nrows=None):
    """Reads the BRFSS data.

    filename: string
    compression: string
    nrows: int number of rows to read, or None for all

    returns: DataFrame
    """
    var_info = [
        ('sex', 120, 120, int),
        ('age', 1974, 1975, int),
        ('edu', 158, 158, int),
        ('marital', 157, 157, int),
        ('employ', 172, 172, int),
        ('income', 175, 176, int),        
        ('health', 90, 90, int),             
        ('bmi', 1988, 1991, int),
        ('height', 1980, 1982, int),
        ('weight', 1983, 1987, int),    
        ('exercise', 227, 227, int),
        ('workhour', 608, 609, int),
        ('exemin', 2119, 2123, int),
        ('fruit', 2050, 2050, int),
        ('vegetable', 2051, 2051,int),
    ]
    columns = ['name', 'start', 'end', 'type']
    variables = pd.DataFrame(var_info, columns=columns)
    variables.end += 1
    dct = FixedWidthVariables(variables, index_base=1)

    df = dct.ReadFixedWidth(filename, compression=compression, nrows=nrows)
    CleanBrfssFrame(df)
    return df


def CleanBrfssFrame(df):
    """Recodes BRFSS variables.

    df: DataFrame
    """
    # sex
    df.sex = df.sex.replace({1:'M', 2:'F'})
    
    # income
    df.income = df.income.replace({77:np.nan, 99:np.nan})
    
    # health
    df.health = df.health.replace({7:np.nan, 9:np.nan})
    
    # bmi
    df.bmi /= 100

    # height
    df.height /= 100
    
    # weight
    df.weight /= 100
    
    # exercise
    df.exercise = df.exercise.replace({1:True, 2:False, 7:np.nan, 9:np.nan})
    
    # workhour
    df.workhour = df.workhour.replace({97:np.nan, 98:0, 99:np.nan})
     
    # fruit
    df.fruit = df.fruit.replace({1:True, 2:False, 9:np.nan})
    
    # vegetable
    df.vegetable = df.vegetable.replace({1:True, 2:False, 9:np.nan})

    