import gradio as gr

def search(query):
    results = search_courses(query)
    return results.to_dict("records")

iface = gr.Interface(
    fn=search,
    inputs=gr.Textbox(label="Enter your query"),
    outputs=gr.Dataframe(headers=["Title", "Description", "Link"]),
    title="Smart Course Search"
)

iface.launch()
