#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Testing numeric types """

import decimal

import fractions


INTVAL = 1

print INTVAL

FLOATVAL = 0.1

print FLOATVAL


DECVAL = decimal.Decimal('0.1')

print DECVAL


FRACVAL = fractions.Fraction(1, 10)

print FRACVAL
