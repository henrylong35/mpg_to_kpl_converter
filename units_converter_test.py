"""
Unit test for the MPG to KPL units converter
"""

# import the code to be tested

from units_converter import mpg2kpl, kpl2mpg

def describe_a_units_converter():

        def that_can_convert_mpg_to_kpl():

            assert mpg2kpl(30) == 12.7543
            assert mpg2kpl(60) == 25.5086

        def that_can_convert_kpl_to_mpg():

             assert kpl2mpg(30) == 70.5643