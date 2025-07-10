import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv()

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query = gr.Textbox(label="what topic would you like to research?")
    run_button = gr.Button("RUN",variant="primary")
    report = gr.Markdown(label="Report")
    run_button.click(fn=run,inputs=query,outputs=report)
    query.submit(fn=run,inputs=query,outputs=report)

ui.launch(inbrowser=True)