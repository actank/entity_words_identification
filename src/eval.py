#coding:utf-8


tp = 0
fp = 0
fn = 0

input_file = "./result"
for line in open(input_file):
    ll = line.strip().split("\t")
    if len(ll) != 4:
        continue
    label = ll[2]
    pred = ll[3]
    target = "B-NP"

    if label == target and pred == target:
        tp += 1
        continue
    elif label != target and pred == target:
        fp += 1
        continue
    elif label == target and pred != target:
        fn += 1
precision = float(tp)/(tp+fp)
recall = float(tp)/(tp+fn)
f1=2 * precision * recall / (precision + recall)
print("precision:%f recall:%f f1:%f" % (precision, recall, f1))
