from question_generation_robust import GPT3_Question_Generator
from reasoner_robust import Fact_Reasoner
from question_answering_robust import GPT3_T5_Question_Answering
import pandas as pd
import csv
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report


class QAFV_Fact_Checker:
    def __init__(self, args):
        # load model
        self.args = args

        # initialize sub-modules
        API_KEY = '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'
        model_name = 'gpt-3.5-turbo'
        self.question_generator = GPT3_Question_Generator(API_KEY, model_name)
        self.QA_module = GPT3_T5_Question_Answering(API_KEY, model_name)
        self.reasoner = Fact_Reasoner(API_KEY, model_name)
        print(f"New Robust Individual modules initialized.")

    '''
    This one collabrates with GPT3
    '''
    def verify_single_claim_GPT3(self, claim, MAX_ROUND = 5):
        contexts_history = []
        qa_contexts = []
        for round_ind in range(MAX_ROUND):
            Should_Stop = False
            # Question Generation
            sub_question = ""
            if round_ind == 0:
                sub_question = self.question_generator.generate_first_question(claim)
            else:
                # Whether we should stop here. 
                Should_Stop = self.reasoner.is_information_sufficient(claim, qa_contexts)
                # print(Should_Stop)
                if Should_Stop == True:
                    break
                # otherwise, generate the next subquestion
                sub_question = self.question_generator.generate_next_question(claim, qa_contexts)
            
            # Question Answering
            answer = self.QA_module.answer_question(sub_question)
            answer_text = answer['answer_text']
            answer_rationale = answer['rationale']

            # Save Result
            qa_result = {'round': round_ind, 
                         'target_entity': "", 
                         'generated_question': sub_question, 
                         'answer': answer_text, 
                         'rationale': answer_rationale}
            
            contexts_history.append(qa_result)
            qa_contexts.append([sub_question, answer_text])

        # reason the label
        prediction_with_rationale = self.reasoner.CoT_claim_verification(claim, qa_contexts)

        return prediction_with_rationale, contexts_history


if __name__ == "__main__":
    # Example arguments
    args = {
        "API_KEY": "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",
        "model_name": "gpt-3.5-turbo"
    }
    fact_checker = QAFV_Fact_Checker(args)
    # testing_claims = pd.read_csv("/Users/tarunchadaram/Library/CloudStorage/OneDrive-GeorgeMasonUniversity-O365Production/Gmu/sem2/678/main_project/QACheck_CS678project/qafv_model/updated_datasets/2-hop.csv")
    # claims = testing_claims['claim']
    # true_values = testing_claims['label']
    # print(list(true_values))

    claim = "Skagen Paniter Peder Severin Kr√∏yer prerfered natuarlism alon gwith Tehodo rEsbern Philipsen and Kristian Zahrtmann"
    # testing_claims = pd.read_csv("/Users/tarunchadaram/Library/CloudStorage/OneDrive-GeorgeMasonUniversity-O365Production/Gmu/sem2/678/main_project/QACheck_CS678project/qafv_model/updated_datasets/2-hop.csv")
    # claims = testing_claims['claim']
    # prediction_dict = []
    # Verify the claim using the GPT3 method
    # for claim in claims:

    prediction, history = fact_checker.verify_single_claim_GPT3(claim)
    # Print the result
    print("Claim verification result:", prediction)

    # Print the history of question generation and answering
    print("\nContexts history:")
    for qa_result in history:
        print("Round:", qa_result['round'])
        print("Generated question:", qa_result['generated_question'])
        print("Answer:", qa_result['answer'])
        print("Rationale:", qa_result['rationale'])
        print()

    # f1 = f1_score(true_values, prediction_dict)
    # print("F1 Score:", f1)


    




    
