import pandas as pd
import numpy as np
import re
import json
from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions
from datetime import datetime, timedelta, date
import openpyxl
import xlsxwriter
from collections import deque
import dat
import sqlite3
import os
import glob
import re
import sys



dat.multiple_dataset_apply_containing_cols_sqlite("Chinook.db")