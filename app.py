import gradio as gr
from agent import agent

demo = gr.Interface(
    fn=agent,
    inputs=gr.Textbox(
        label="Ask the Shop Assistant"
    ),
    outputs=gr.Textbox(
        label="Response"
    ),
    title="AI Shop Assistant",
    description="Ask about product prices."
)

demo.launch()