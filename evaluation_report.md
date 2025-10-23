EVALUATION REPORT

--> Evaluation Report – Retail Shelf Object Detection

->  Evaluation Summary

- Validation Dataset Size : 280 images
- Total Detected Instances: 1346

| Metric         | Value   |
|----------------|---------|
| Precision      | 50.6%   |
| Recall         | 75.8%   |
| mAP@0.5        | 66.4%   |
| mAP@0.5:0.95   | 54.7%   |

--------------------------------------------------------------------

->  Per-Class Breakdown

| Class Name     | Precision | Recall | AP@0.5 | AP@0.5:0.95 |
|----------------|-----------|--------|--------|-------------|
| Coke           | 64.5%     | 68.4%  | 71.1%  | 63.3%       |
| Pepsi          | 35.7%     | 91.3%  | 61.4%  | 53.7%       |
| Sprite         | 36.4%     | 43.1%  | 36.5%  | 31.6%       |
| 1-5L_Pet       | 70.6%     | 91.2%  | 81.9%  | 58.8%       |
| 270_Sparking   | 45.9%     | 85.2%  | 80.9%  | 66.1%       |

---------------------------------------------------------------------

->  Performance Insights

- Coke                     : Consistent performance with solid AP and precision
- Pepsi                    : Very high recall but lower precision (model tends to over-predict it)
- Sprite                   : Poorer performance, possibly due to visual similarity to other soda cans
- 1-5L_Pet and 270_Sparking: Achieved the highest APs, thanks to large and clear features

----------------------------------------------------------------------

->  Qualitative Observations

- Model detects multiple object types accurately in most cases.
- Some small or occluded cereal boxes are missed.
- Sprite is the hardest class to differentiate due to size and overlap with others.

-----------------------------------------------------------------------

->  Challenges Faced

- Real-world shelf conditions introduced clutter and occlusion
- Lighting variation impacts detection
- Overlap and similarity between soda classes reduce class separability

-----------------------------------------------------------------------

->  Recommendation

- Use targeted data augmentation to improve Sprite detection
- Apply non-max suppression tuning to reduce false positives
- Consider class rebalancing or focal loss

------------------------------------------------------------------------

~ This evaluation was run using `yolo task=detect mode=val` with the best.pt model on validation set. ~

