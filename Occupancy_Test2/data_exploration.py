#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

df = pd.read_csv('datafulloccupied.csv')
print(df.describe())

df2 = df.loc[0:799]

print(df2.describe())

df3 = df.loc[800:999]
print(df3.describe())