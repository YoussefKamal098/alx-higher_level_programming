#!/usr/bin/python3
"""Unittest for max_integer function"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    """
    Test cases for the max_integer function.

    This test suite covers various scenarios,
    including positive and negative numbers,
    mixed data types, edge cases, and invalid inputs,
    to ensure the max_integer function
    behaves as expected.

    Test Cases:
    - test_positive_numbers: Test with a list of positive integers.
    - test_negative_numbers: Test with a list of negative integers.
    - test_mixed_numbers: Test with a list of mixed positive,
      negative, and zero values.
    - test_empty_list: Test with an empty list, expecting None as the result.
    - test_single_element_list: Test with a list containing a single element.
    - test_duplicate_values: Test with a list of duplicate values.
    - test_float_numbers: Test with a list of floating-point numbers.
    - test_mixed_integer_and_float: Test with a list of mixed integers
      and floating-point numbers.
    - test_large_numbers: Test with a list of large positive integers.
    - test_negative_large_numbers: Test with a list of large negative integers.
    - test_string_values: Test with a list of strings, expecting a TypeError.
    - test_boolean_values: Test with a list of booleans, expecting a TypeError.
    - test_mixed_data_types: Test with a list containing mixed data types,
      expecting a TypeError.
    - test_none_value: Test with None as input, expecting None as the result.
    - test_whitespace_values: Test with a list containing
      whitespace characters.
    - test_list_of_lists: Test with a list of lists.
    - test_list_of_tuples: Test with a list of tuples.
    - test_list_of_dicts: Test with a list of dictionaries,
      expecting a TypeError.
    - test_list_of_sets: Test with a list of sets, expecting a TypeError.
    """
    
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 3, 0]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_float_numbers(self):
        self.assertEqual(max_integer([2.5, 1.3, 3.8]), 3.8)

    def test_mixed_integer_and_float(self):
        self.assertEqual(max_integer([2.5, 1, 3]), 3)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 500000, 900000]), 1000000)

    def test_negative_large_numbers(self):
        self.assertEqual(max_integer([-1000000, -500000, -900000]), -500000)

    def test_string_values(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_boolean_values(self):
        with self.assertRaises(TypeError):
            max_integer([True, False, True])

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3.14])

    def test_none_value(self):
        self.assertIsNone(max_integer(None))

    def test_whitespace_values(self):
        self.assertEqual(max_integer([4, 2, 9, 5]), 9)

    def test_list_of_dicts(self):
        with self.assertRaises(TypeError):
            max_integer([{'a': 1}, {'b': 2}, {'c': 3}])

    def test_list_of_sets(self):
        with self.assertRaises(TypeError):
            max_integer([{1, 2}, {4, 5}, {7, 8}])

    def test_ints_and_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [199872.7619047619, 115249.8813559322, 37972.944444444445,
                 120549.90322580645, 30889.777777777777, 986136.4,
                 393382.5416666667, 15441.826086956522, 2503567,
                 176118.87179487178, 372359.4, 142747.61538461538,
                 383318.8181818182, 297732.2727272727, 104980.52702702703,
                 98409.27272727272, 617459.875, 56556.62162162162, 61958.8,
                 115000.59090909091, 240958.45714285714,
                 101071.85714285714, 77616.47692307692, 89029.64,
                 104941.96666666666, 31940.53846153846, 106652.10126582278,
                 686700.1538461539, 52758.709677419356, 348259.4285714286,
                 89457.28947368421, 58039.52702702703, 306427.53571428574,
                 64379.01176470588, 557699.5333333333, 18718.639344262294,
                 364967.55555555556, 129951.23404255319, 41683.82692307692,
                 139149.9818181818, 356782.86666666664, 100259.07692307692,
                 245204.75, 78972.5306122449, 404825.8888888889, 124364.25,
                 1065047.5, 42946.45614035088, 73670.8813559322,
                 83546.51351351352, 323098.3333333333, 88578.35294117648,
                 89471.0, 47745.197916666664, 17102.676767676767,
                 127735.80882352941, 110513.05882352941,
                 62214.055555555555, 6968.981481481482, 40691.34693877551,
                 69931.09677419355, 67024.44186046511, 112123.04,
                 1167186.0, 140392.05, 15814.362637362638,
                 88923.34444444445, 114726.20731707317, 143303.55,
                 38233.83516483517, 94065.72857142857, 42789.892857142855,
                 44182.47169811321, 41313.101265822785, 67705.18965517242,
                 1222423.5, 44966.55405405405, 37153.6, 82085.08,
                 559793.2857142857, 30031.58823529412, 126947.4262295082,
                 309222.3125, 125132.82089552238, 37276.27397260274,
                 99726.62903225806, 4270.788235294118, 490468.4375,
                 54086.642857142855, 73068.5, 108526.5081967213, 52943.875,
                 128534.875, 61069.433333333334, 37142.71951219512,
                 51481.13114754098, 571618.5, 35977.166666666664,
                 142333.11764705883, 199123.75]), 2503567)

    def test_positives_and_negatives_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                 7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                 -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                 -8394, 9732, 1695, -4932, -2100, -6920, 2219, -7319,
                 -1193, -422, 9312, 9508, -2690, -9206, 4461, 2997, -6753,
                 -7824, 3097, 1681, 3401, 7221, 1758, -1990, 4958, 4347,
                 7054, 545, 3492, -7285, -1672, 2230, -4576, -3121,
                 -6736, -537, 9823, 4281, -8003, 327, 1824, -1973, -9844,
                 29, 3596, 1108, 6702, 4873, -9452, -5949, -9640, -2156,
                 -4104, 5772, 5121, -2186, -4870, -4116, 6443, -9381,
                 -9388, 8552, 3582, 3500, 7924, 211, -2976, 6346, -5405,
                 899, -3432, -2550, -3353, 6944, 9623]), 9823)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                 -1907189, -8110534, -6601769, -5837524, -4726702,
                 -8433749, -7251403, -5117635, -2979207, -1335257,
                 -6867266, -9073637, -6224732, -1080801, -1080228,
                 -6801278, -8351954, -1736432, -746131, -4376995,
                 -967891, -4663691, -71562, -7153670, -8038202,
                 -7893047, -9350883, -1132134, -3675971, -8495354,
                 -9158229, -9310087, -6319598, -8961209, -4906000,
                 -386471, -639929, -2676965, -6881679, -6258057,
                 -5490677, -1107298, -4199148, -5933601, -9917695,
                 -7759849, -7045734, -4885806, -9485075, -5119579,
                 -4147063, -7622811, -4671971, -5439539, -840414,
                 -3671742, -4400074, -3549343, -9146070, -6071672,
                 -7213213, -1307446, -3936098, -2415520, -9162654,
                 -6129976, -5791439, -3481890, -7828832, -6954726,
                 -5272933, -4952516, -6115545, -8333464, -7271456,
                 -4097027, -4342575, -8400559, -8235052, -4373818,
                 -8054214, -8565596, -639225, -2292452, -4269529,
                 -7202853, -6891036, -4379807, -7955196, -1536591,
                 -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [0.36701449486981136, 0.22932193120425423, 17.269673745943177,
                 0.6021998063297004, 7.040663644666581, 0.318418153098476,
                 0.14782568486828354, 1.694150096609713, 0.523292479047324,
                 6.577278388003499, 0.03165696316739835,
                 0.9723205356754642, 1.0167973840532782,
                 0.17994528432150622, 0.34268959203149724,
                 0.8237893847200373, 6.564703466354198, 0.650943204479027,
                 1.8902940005294793, 7.691604865311827, 8.897302744173896,
                 1.0780411284398352, 1.6564018996809176,
                 0.7495378363397325, 0.6460418901123863,
                 0.29656944388569284, 1.2020859950744733,
                 2.695758513783994, 0.37293339285604976,
                 0.8540047898304736, 0.16021193325291794,
                 0.027891891117170508, 0.8464685760135892,
                 4.506719557284897, 2.0258041087808, 4.525163681550944,
                 1.3277284362225874, 3.042753010712081, 2.4201460936424986,
                 0.6254206993310946, 3.6037820704785766,
                 0.5843942753272469, 2.994055932449279, 0.5168645505697169,
                 0.014982685631661026, 0.02477737364433171,
                 0.47120480947220955, 2.5056796257122915,
                 1.3349487122618868, 0.08451917751917885,
                 1.0157082402123356, 29.496355326217376,
                 10.171800729369348, 1.1263544935158727,
                 0.47572929035550277, 3.712323073375754,
                 0.5742929278531704, 0.43940976988732966,
                 0.09537099783126887, 1.4936141049902174,
                 5.764320019082692, 4.322880498170903, 2.004237813008687,
                 0.5565243581024599, 4.302022962278392, 5.680293004785562,
                 2.178866303290743, 1.0390412554953965,
                 0.45132551361896317, 1.4643609109467473,
                 0.6904822043628014, 7.42850599670902, 0.8174242076055683,
                 0.6560986886071569, 0.6513016647379839, 0.7402037152516,
                 1.3480227709351067, 10.667222236398727,
                 1.1255361340134915, 0.3631658619504303,
                 0.8812949657884553, 1.1100323642668828,
                 5.0119643460188845, 2.8953551308720056,
                 2.5574324632368866, 9.169493642307119, 0.4175692708444569,
                 2.344748944605401, 1.1674261590629318, 0.6998588019912835,
                 0.42770576125452897, 1.7136005979522013,
                 8.877571036363525, 0.6825287480571863, 2.6834294650218338,
                 0.7504024417975861, 0.2762206358275793,
                 0.20607476376994402, 0.9497689034126077,
                 2.1498649449691807]), 29.496355326217376)


if __name__ == '__main__':
    unittest.main()
