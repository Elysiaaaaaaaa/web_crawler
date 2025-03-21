import numpy as np
import pandas as pd
import torch
import os
import torch.nn as nn
from torch.utils import data
from torch.optim import lr_scheduler
import requests
from bs4 import BeautifulSoup as bs
from transformers import AutoModel
from sentence_transformers import SentenceTransformer, util