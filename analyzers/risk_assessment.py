from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from prompts.prompt_templates import risk_prompt

def assess_risk(llm, retriever):

    prompt = PromptTemplate(template=risk_prompt, input_variables=["context", "question"])
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke(risk_prompt)

    return result