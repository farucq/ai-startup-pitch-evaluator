from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from prompts.prompt_templates import market_prompt

def analyze_market(llm, retriever):

    prompt = PromptTemplate(template=market_prompt, input_variables=["context", "question"])
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke(market_prompt)

    return result