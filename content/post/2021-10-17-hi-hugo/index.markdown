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
##                                        expr    min      lq     mean median
##  summarise(mtcars, across(.f = n_distinct)) 3457.7 4167.55 5464.507 4825.0
##      map_int(mtcars, .f = vec_unique_count)   82.5   92.20  166.536  120.8
##       uq     max neval
##  6652.85 13304.1   100
##   146.70  2369.8   100
```


```r
ggplot2::autoplot(mbm)
```

```
## Coordinate system already present. Adding new coordinate system, which will replace the existing one.
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-6-1.png" width="672" />




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
##                                                   expr     min      lq
##  summarise(ggplot2::diamonds, across(.f = n_distinct)) 11.9632 13.6995
##      map_int(ggplot2::diamonds, .f = vec_unique_count)  6.8085  7.4775
##       mean   median       uq     max neval
##  18.050561 17.09485 21.02225 55.4891   100
##   9.833397  9.21795 11.21605 20.4642   100
```


```r
ggplot2::autoplot(mbm)
```

```
## Coordinate system already present. Adding new coordinate system, which will replace the existing one.
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-9-1.png" width="672" />


