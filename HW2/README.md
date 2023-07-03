
## Output
```
BagOfWords:  {'Hiroshima', 'Kyoto', 'Japan', 'Saijo', 'sake', 'alcohol'}
P(class):  {'HRS': 0.75, 'KYT': 0.25}
Word Count for HRS :  8.0
Word Count for KYT :  4.0
P(word|HRS)  {'Hiroshima': 0.16666666666666666, 'Kyoto': 0.05555555555555555, 'Japan': 0.1111111111111111, 'Saijo': 0.2222222222222222, 'sake': 0.16666666666666666, 'alcohol': 0.05555555555555555}
P(word|KYT)  {'Hiroshima': 0.07142857142857142, 'Kyoto': 0.14285714285714285, 'Japan': 0.14285714285714285, 'Saijo': 0.07142857142857142, 'sake': 0.14285714285714285, 'alcohol': 0.14285714285714285}

P(HRS|Japan sake tasting):  0.0007716049382716049 [('Japan', 0.1111111111111111), ('sake', 0.16666666666666666), ('tasting', 0.05555555555555555)]
P(KYT|Japan sake tasting):  0.0003644314868804664 [('Japan', 0.14285714285714285), ('sake', 0.14285714285714285), ('tasting', 0.07142857142857142)]
['(Japan sake tasting) is more probable to be (HRS)']
```
