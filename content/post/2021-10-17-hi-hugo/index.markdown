---
title: Hi Hugo
author: ''
date: '2021-10-17'
slug: hi-hugo
categories:
  - category
  - subcategory
tags:
  - tag1
  - tag2
keywords:
  - tech
---



What ???



```r
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library(vctrs)
```

```
## 
## Attaching package: 'vctrs'
```

```
## The following object is masked from 'package:dplyr':
## 
##     data_frame
```

```r
library(purrr)
```



```r
summarise(mtcars, across(.f = n_distinct))
```

```
##   mpg cyl disp hp drat wt qsec vs am gear carb
## 1  25   3   27 22   22 29   30  2  2    3    6
```


```r
purrr::map_int(mtcars, .f = vctrs::vec_unique_count)
```

```
##  mpg  cyl disp   hp drat   wt qsec   vs   am gear carb 
##   25    3   27   22   22   29   30    2    2    3    6
```



```r
mbm <- microbenchmark::microbenchmark(
  summarise(mtcars, across(.f = n_distinct)),
  map_int(mtcars, .f = vec_unique_count)
)
```



```r
mbm
```

```
## Unit: microseconds
##                                        expr    min      lq     mean  median
##  summarise(mtcars, across(.f = n_distinct)) 3506.8 4359.25 5623.673 5199.40
##      map_int(mtcars, .f = vec_unique_count)   86.5  123.65  164.513  147.75
##       uq     max neval
##  6809.80 10914.9   100
##   208.75   296.1   100
```


```r
ggplot2::autoplot(mbm)
```

```
## Coordinate system already present. Adding new coordinate system, which will replace the existing one.
```

<img src="https://i.imgur.com/jpMzSru.png" width="672" />




```r
mbm <- microbenchmark::microbenchmark(
  summarise(ggplot2::diamonds, across(.f = n_distinct)),
  map_int(ggplot2::diamonds, .f = vec_unique_count)
)
```




```r
mbm
```

```
## Unit: milliseconds
##                                                   expr     min       lq
##  summarise(ggplot2::diamonds, across(.f = n_distinct)) 11.4828 13.07260
##      map_int(ggplot2::diamonds, .f = vec_unique_count)  6.7155  7.12475
##       mean   median      uq     max neval
##  16.353275 15.44085 19.1405 30.7827   100
##   9.861705  9.20540 11.6624 20.6551   100
```


```r
ggplot2::autoplot(mbm)
```

```
## Coordinate system already present. Adding new coordinate system, which will replace the existing one.
```

<img src="https://i.imgur.com/qmBmybw.png" width="672" />


