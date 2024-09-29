from .models import Users
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def add_stata(nameuser, question, answer):
    Users.objects.create(name = nameuser,
                         question = question,
                         answer = answer)
    return f"Create:\nName - {nameuser}\nQuestion - {question}\nAnswer - {answer}\n"

def get_stata():
    stata = {}
    return stata