import os
import streamlit as st
from neo4j import GraphDatabase
from together import Together

## Connexion Neo4J
uri = "bolt://localhost:7687"
user = "neo4j"
password = "4Uxlz6fQfmQl6aDFPZlrRlkMdub1gxoZYQ9EnOjMRSM"

##Instance to use Neo4J

driver = GraphDatabase.driver(uri, auth=(user, password))

##Client together (Deploy web)

client = Together(api_key="0015914a73cf1accd15317c1e9d51d06707e47362c3e76bb4cb77369f00fbe46")

## First function to use cypher request

def query_neo4j(tx, query, params=None):
    try:
        result=tx.run(query, params or {})
        return[record for record in result]
    except Exception as e:
        st.error(f"Error neo4j request: {str(e)}")
        return[]
    
## Function to save film data

def retrieve_information():
    query="""
    MATCH (m:Movie)
    RETURN m.title AS title, m.tagline AS tagline, m.released AS released
    LIMIT 30 """

    with driver.session() as session:
        results = session.execute_read(query_neo4j, query)
    
    if results:
        return "\\\\n".join([f"Title: {r['title']}, Tagline: {r['tagline']}, Released: {r['released']}" for r in results])
    else:
        return "There isn't film data"
    
## Fuction to create a promp
def create_prompt(retrieved_info, user_query): ##Using RAG
    prompt= f"Taking this film data as base to respond the next question:\\\
        \n{retrieved_info}\\\\n\\\\nRespond this question: {user_query}"
    return prompt

## Generate the response

def generate_response(propmt):
    try:
        stream=client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[{"role":"user", "content":propmt}],
            stream=True,
            max_tokens=1000,
            temperature=0.1,
            top_p=0.9,
            top_k=50
        )

        generated_text=''
        for chunk in stream:
            if chunk.choices:
                content = chunk.choices[0].delta.content
                if content:
                    generated_text+=content
                    yield content
    
        if not generated_text:
            yield "Model without response"
    except Exception as e:
        yield f"Model Error: {str(e)}"

def main():
    st.title("Graph of film knowledge with LLM")
    st.write("Ask any question about the film database !")

    user_query=st.text_input("Question...")
    if st.button("Ask!"):
        with st.spinner("Loading Neo4J Data...  "):
            retrieved_info=retrieve_information()
        with st.spinner("Response generating..."):
            prompt= create_prompt(retrieved_info, user_query)
            response=generate_response(prompt)
        for r in response:
            st.write(r)

if __name__ is "__main__":
    main()