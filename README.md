# QACheck

This is Data and Codes for The original paper we considered
["QACHECK: A Demonstration System for Question-Guided Multi-Hop Fact-Checking"](https://arxiv.org/abs/2310.07609) (EMNLP 2023, System Demonstrations).

Firsty install all the dependencies
```bash
pip install flask
pip install openai
pip install backoff
```
In the Datasets_Hov_Fev we have all the datasets we considered of 200 records each.
## For Robustness approach and improvement
In the PerturbationData_Evaluation directory there is file named Testing_Normal_Pertubateddata.ipynb where we checked the models robustness initially.In the PerturbationData_Evaluation there is all_pertubation directory where you have all perturbation dataset including typos,synonyms and no puctuations.There is 3typos directory which has files typos errors in it which used.There is synonyms directory where it has data with perturbated synonyms for all 2hop ,3hop ,4hop and feverous

There is a robustness_improved directory where you can find for_robustness.ipynb where we clearly demonstrated data from 3typos directory.

## For Multilinguality and improvement
Inside the MultilingualData_Evaluation directory there will be datasets of each language we considered and there will be a file testing_multilingualdata.ipynb where we used these datasets got evaluation done various languages on the existing model.

We have multiligualitytesting_improved.ipynb where we used back_translation to english language and evaluated using hindi converted dataset.

Note:
While trying to run the ipynb notebooks or fact_checker.py files.Please give your API key removing the existing one as it wont work.


## Reference
This is the reference paper which we used to do this reasearch:

```
@inproceedings{PanQACheck23,
  author       = {Liangming Pan, Xinyuan Lu, Min-Yen Kan, Preslav Nakov},
  title        = {QACHECK: A Demonstration System for Question-Guided Multi-Hop Fact-Checking},
  booktitle    = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing System Demonstrations Track (EMNLP 2023 Demo Track)},
  address      = {Singapore},
  year         = {2023},
  month        = {Dec}
}
```

## Q&A
If you encounter any problem, please either directly contact the [Tarun Naga Sai Chadaram](tchadara@gmu.edu) or leave an issue in the github repo.


