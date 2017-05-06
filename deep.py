import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import inception

inception.data_dir = 'inception/'
inception.maybe_download()