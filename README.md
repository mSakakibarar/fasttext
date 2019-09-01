# fasttext
fasttextの学習用

## 学習
/fasttext supervised -input data/train.txt -output results/result -dim 50 -lr 1.0 -epoch 25

## 予測
/fasttext predict-prob results/result.bin mytests/test.txt
