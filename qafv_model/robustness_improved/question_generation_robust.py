import backoff  # for exponential backoff
import openai
from spellchecker import SpellChecker
from gpt3_template_robust import GPT3_Template

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

class GPT3_Question_Generator:
    def __init__(self, API_KEY, model_name) -> None:
        self.API_KEY = API_KEY
        self.model_name = model_name
        openai.api_key = API_KEY
        self.gpt3_template = GPT3_Template()
        self.spell_checker = SpellChecker()

    def generate(self, input_string):
        response = chat_completions_with_backoff(
            model=self.model_name,
            messages=[
                {"role": "user", "content": input_string}
            ],
            max_tokens=64,
            temperature=0.01,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        generated_text = response['choices'][0]['message']['content'].strip()
        return generated_text

    def clean_claim(self, claim):
        # Correct spelling
        corrected_claim = self.correct_spelling(claim)
        print(corrected_claim)
        return corrected_claim

    def correct_spelling(self, claim):
        # Create a SpellChecker instance
        spell = SpellChecker()

        # Split the claim into words
        words = claim.split()

        # Find misspelled words
        misspelled = spell.unknown(words)

        # Correct misspelled words
        for word in misspelled:
            corrected_word = spell.correction(word)
            if corrected_word is not None:
                claim = claim.replace(word, corrected_word)
        print(claim)
        return claim

    def generate_first_question(self, claim):
        # Clean the claim
        claim = self.clean_claim(claim)
        example = self.gpt3_template.fill_QG_template_start(claim)
        generated_text = self.generate(example)
        return generated_text

    def generate_next_question(self, claim, qa_contexts):
        # Clean the claim
        claim = self.clean_claim(claim)
        example = self.gpt3_template.fill_QG_template_followup(claim, qa_contexts)
        generated_text = self.generate(example)
        return generated_text