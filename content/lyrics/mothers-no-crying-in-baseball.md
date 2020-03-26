Title:    No Crying in Baseball
Date:     2018-09-13 07:35
Category: lyric
Tags:     indie, 2010s
Slug:     mothers-no-crying-in-baseball
Author:   Mothers

There's no crying in baseball.  
Try to understand.

    :::haskell
    -- Layout Hook
    commonLayout = renamed [Replace "common"]
        $ avoidStruts 
        $ gaps [(U,5), (D,5)] 
        $ spacing 10
        $ Tall 1 (5/100) (1/3)
