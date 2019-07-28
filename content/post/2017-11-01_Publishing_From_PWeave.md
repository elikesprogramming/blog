---
title: Publishing blog posts from PWeave
author: elikesprogramming
date: '2017-11-01'
categories:
  - Python
tags:
  - PWeave
---

This blog started mostly as an archive for R-related things as I was starting
to use R as my main tool / language for data analysis. For a while I've been
also using Python. Looking for a literate programming alterative in Python
I found [Pweave](http://mpastell.com/pweave). So I'd like to also use this blog
as an archive for Python-related things, starting with how to use PWeave to
write blog posts. Yeah, I guess I can keep using RMarkdown to write
Python-related blog posts, but I find Python support still limited and
therefore I prefer to write the posts in the main editor I use to write python
code (currently Atom).

# PWeave

Using PWeave you can write using several formats and then compile the notebook
into, also, several formats (e.g. markdown, html). It seems it was inspired by
Sweave, which was the most common literate programming approach before
RmarkDown came to the scene.

% ```python
% ```


```python
# Import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Initialize Figure and Axes object
fig, ax = plt.subplots()

# Load in data
tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Create violinplot
ax.violinplot(tips["total_bill"], vert=False)

# Show the plot
plt.show()
```

![](/post/PWeave_Figures/2017-11-01_Publishing_From_PWeave_figure1_1.png)\


The Hamming window:
$w(n) = \alpha - \beta\cos\frac{2\pi n}{N-1}$, where $\alpha=0.54$ and $\beta=0.46$

The next code chunk is executed in term mode, see the [Python script](FIR_design.py) for syntax.
Notice also that Pweave can now catch multiple figures/code chunk.


python, term=True
n = 61



python, caption="Bandpass FIR filter."
n = 1001
