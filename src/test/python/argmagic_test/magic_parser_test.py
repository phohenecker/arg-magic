#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import sys

from argmagic import magic_parser
from argmagic_test import dummy_config
from argmagic_test import dummy_config_2
from argmagic_test import dummy_config_3


__author__ = "Patrick Hohenecker"
__copyright__ = (
        "Copyright (c) 2017, Patrick Hohenecker\n"
        "All rights reserved.\n"
        "\n"
        "Redistribution and use in source and binary forms, with or without\n"
        "modification, are permitted provided that the following conditions are met:\n"
        "\n"
        "1. Redistributions of source code must retain the above copyright notice, this\n"
        "   list of conditions and the following disclaimer.\n"
        "2. Redistributions in binary form must reproduce the above copyright notice,\n"
        "   this list of conditions and the following disclaimer in the documentation\n"
        "   and/or other materials provided with the distribution.\n"
        "\n"
        "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" AND\n"
        "ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED\n"
        "WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n"
        "DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR\n"
        "ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n"
        "(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n"
        "LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n"
        "ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n"
        "(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\n"
        "SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
)
__license__ = "Simplified BSD License"
__version__ = "2017.1"
__date__ = "Nov 09, 2017"
__maintainer__ = "Patrick Hohenecker"
__email__ = "mail@paho.at"
__status__ = "Development"


class MagicParserTest(unittest.TestCase):
    
    def test_parser_args(self):
        # create target config object
        target = dummy_config.DummyConfig()
        target.x = 3
        target.y = "abc"
        # z is NOT specified
        
        # CHECK: parse config using positional args
        sys.argv = "test --x TRES abc".split(" ")
        self.assertEqual(
                target,
                magic_parser.MagicParser(dummy_config.DummyConfig, positional_args=True).parse_args()
        )
        
        # CHECK: parse config without positional args
        sys.argv = "test --y abc --x TRES".split(" ")
        self.assertEqual(
                target,
                magic_parser.MagicParser(dummy_config.DummyConfig, positional_args=False).parse_args()
        )
        
        # create target config object
        target = dummy_config_2.DummyConfig2()
        target.a = "1"
        target.b = "2"
        target.c = "3"

        # CHECK: positional args with specified order are parsed correctly
        sys.argv = "test 3 1 2".split(" ")
        self.assertEqual(
                target,
                magic_parser.MagicParser(dummy_config_2.DummyConfig2).parse_args()
        )
        
        # create target config object
        target = dummy_config_3.DummyConfig3()
        target.a = "1"
        target.b = 2.0

        # CHECK: optional args without default value are parsed correctly
        sys.argv = "test --a 1 2".split(" ")
        self.assertEqual(
                target,
                magic_parser.MagicParser(dummy_config_3.DummyConfig3).parse_args()
        )
        target.c = 3
        sys.argv = "test --a 1 --c 3 2".split(" ")
        self.assertEqual(
                target,
                magic_parser.MagicParser(dummy_config_3.DummyConfig3).parse_args()
        )
    

if __name__ == "__main__":
    unittest.main()
