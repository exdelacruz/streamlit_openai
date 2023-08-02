import streamlit as st
import openai

[secrets]
api_key = "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"
another_secret = "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"

# Set up the OpenAI API
openai.api_key = st.secrets["api_key"]


def generate_code(input_string):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_string +"\n",
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.set_page_config(page_title="C++ Tutorial App")
    st.title("C++ Tutorial App - Generate Code for Basic Programming Tasks")
    st.text("by: Ellan V. Flores BSCS 3A")
    instructions = ['1. Code for a factorial function',
                    '2. Code to sort an array using bubble sort algorithm',
                    '3. Code for a linked list data structure',
                    '4. Code to read and write files in C++']

    str_inst = ''
    count = 0
    for i in instructions:
        str_inst = str_inst + i
        if count < len(instructions)-1:
            str_inst = str_inst + ',\n'
        count += 1

    input_string = "Generate C++ code for the following tasks:\n" + str_inst
    output = generate_code(input_string)

    print(f"Input: {input_string}\nOutput:\n{output}")

    task = st.selectbox("Select task:", instructions)

    if st.button("Generate code"):
        output = generate_code(task)
        st.code(output, language="cpp")

if __name__ == "__main__":
    main()

