import pandas as pd
import numpy as np
from faker import Faker
import random

np.random.seed(42)
random.seed(42)
Faker.seed(42)

faker = Faker()

NUM_STUDENTS = 1000

DEPARTMENTS = ['CSE', 'IT', 'ECE', 'EEE', 'MECH', 'AI_DS']

GENDERS = ['Male', 'Female']

