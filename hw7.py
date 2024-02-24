# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
# ---

# %% [markdown]
"""
<div style="text-align: left;">
    <h1>Week 7 - Laboratory</h1>
    <h4>ECON441B</h3>
    <div style="padding: 20px 0;">
        <hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));">
        <p><em>Mauricio Vargas-Estrada</em><br>
        Master in Quantitative Economics<br>
        University of California - Los Angeles</p>
        <hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));">
    </div>
</div>
"""
# %%
import openai
import os
import wikipedia

from tmp import api_key
# %% [markdown]
"""
1. Set up OpenAI and the environment.
"""
# %%
client = openai.Client(
    api_key=api_key()
)

# %% [markdown]
"""
2. Use the `wikipedia` API to get a function that pulls in the text of a `wikipedia` page.
"""

# %%
# get_wiki = lambda page: wikipedia.page(page).content
get_wiki = lambda term: wikipedia.summary(term, sentences=10)
# %% [markdown]
"""
3. Build a `chatgpt` bot that will analyze the text given and try to locate any false info.
"""
# %%
def check_info_wikipedia(text, role):
    tmp = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': role
            },
            {
                'role': 'user',
                'content': text
            }
        ]
    )
    return tmp.choices[0].message.content
# %% [markdown]
"""
4. Make a for loop and check a few wikipedia pages and return a report of any potentially false info via wikipedia.
"""
# %%
terms = [
    'Machine learning',
    'Statistical learning',
    'Deep learning'
]
# %%
temp_role_definition = f"""
- You have to locate FALSE information from a a serie of sentences. 
- If a sentence seems TRUE, return 1, otherwise return 0.
- If you are not sure, return a value between 0 and 1 that represents your confidence level.
- Return the sequence of values like a python list.
"""
# %%
responses = []

for t in terms:
    print(f'Checking veracity for: {t} ...')
    responses.append(
        check_info_wikipedia(
            get_wiki(t),
            temp_role_definition
        )
    )
    print(responses[-1])
