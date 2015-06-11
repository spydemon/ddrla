# Copyright (c) 2015 Kevin Hagner
#
# ddrla is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ddrla is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ddrla.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname, abspath, join
import unittest

from ddrla.logParser import LogParser

class TestLogParser(unittest.TestCase):

    package = dirname(dirname(abspath(__file__)))
    parser = None

    def setUp(self):
        testFile = join(self.package, 'data', 'ddrescue_sample.log')
        self.parser = LogParser(testFile)

    def test_get_log_dictionary(self):
        log_dict = self.parser.get_log_dictionary()
        self.assertEqual(len(log_dict), 30204)
        map(lambda e: self.assertTrue(len(e) == 3), log_dict)
        self.assertEqual(log_dict[0], ['0x00000000', '0xC2629000', '+'])
        self.assertEqual(log_dict[-1], ['0xE8D4A51000', '0x0C365000', '?'])

    def test_get_log_statistics(self):
        log_stat = self.parser.get_log_statistics()
        self.assertEqual(log_stat, {
          'total': 1000204886016,
          'rescued': 886719395136,
          'nontried': 113238912320,
          'bad': 639744,
          'nontrimmed': 244389504,
          'nonsplit': 1549312
        })

    def test_get_current_status(self):
        current_status = self.parser.get_current_status()
        self.assertEqual(current_status, ['0x75F3BC0000', '?'])

    def test_get_current_status_position(self):
        current_status_position = self.parser.get_current_status_position()
        self.assertEqual(current_status_position, '0x75F3BC0000')

    def test_get_current_status_state(self):
        current_status_state = self.parser.get_current_status_state()
        self.assertEqual(current_status_state, '?')

    def test_get_rescued_bytes(self):
        rescuedBytes = self.parser.get_rescued_bytes()
        self.assertEqual(rescuedBytes, 886719395136)

    def test_get_nontried_bytes(self):
        nontriedBytes = self.parser.get_nontried_bytes()
        self.assertEqual(nontriedBytes, 113238912320)

    def test_get_nontrimmed_bytes(self):
        nontrimmedBytes = self.parser.get_nontrimmed_bytes()
        self.assertEqual(nontrimmedBytes, 244389504)

    def test_get_nonsplit_bytes(self):
        nonsplitBytes = self.parser.get_nonsplit_bytes()
        self.assertEqual(nonsplitBytes, 1549312)

    def test_get_bad_bytes(self):
        badBytes = self.parser.get_bad_bytes()
        self.assertEqual(badBytes, 639744)

    def test_get_percentage_of(self):
        nontrimmed_ratio = self.parser.get_percentage_of('nontrimmed')
        self.assertEqual(nontrimmed_ratio, 0.024433944226512263)
        rescued_ratio = self.parser.get_percentage_of('rescued')
        self.assertEqual(rescued_ratio, 88.65377559471504)
