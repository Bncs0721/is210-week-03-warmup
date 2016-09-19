#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Testing numeric types """

INTVAL = 1

print INTVAL

FLOATVAL = 0.1

print FLOATVAL

import decimal

DECVAL = decimal.Decimal('0.1')

print DECVAL

import fractions

FRACVAL = fractions.Fraction(1, 10)

print FRACVAL
